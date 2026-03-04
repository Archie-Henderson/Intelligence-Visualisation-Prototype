import json
import os
import types
import pytest
import spacy


# SPACY PIPELINE FIXTURES 

@pytest.fixture(scope="session")
def nlp_minimal():
    os.environ.setdefault("OPENAI_API_KEY", "test-key")
    import main

    nlp = spacy.blank("en")
    nlp.add_pipe("sentencizer")

    ruler = nlp.add_pipe("entity_ruler")
    ruler.add_patterns(
        [
            {"label": "PERSON", "pattern": "John Smith"},
            {"label": "PERSON", "pattern": "Alice Brown"},
            {"label": "GPE", "pattern": "London"},
            {"label": "GPE", "pattern": "Glasgow"},
            {"label": "ORG", "pattern": "ACME Ltd"},
        ]
    )

    nlp.add_pipe("regex_entities", last=True)
    return nlp


@pytest.fixture(scope="session")
def nlp_for_home_address():
    nlp = spacy.blank("en")
    nlp.add_pipe("sentencizer")
    ruler = nlp.add_pipe("entity_ruler")
    ruler.add_patterns(
        [
            {"label": "PERSON", "pattern": "John Smith"},
            {"label": "GPE", "pattern": "London"},
            {"label": "ADDRESS", "pattern": "10 High Street"},
            {"label": "ADDRESS", "pattern": "99 Low Street"},
        ]
    )
    return nlp


# PURE HELPERS 

def test_split_into_blocks_basic():
    os.environ.setdefault("OPENAI_API_KEY", "test-key")
    import main

    text = "A\n\nB\n\n\nC"
    assert main.split_into_blocks(text) == ["A", "B", "C"]


def test_split_into_blocks_trims_empty():
    os.environ.setdefault("OPENAI_API_KEY", "test-key")
    import main

    text = "\n\n  \nA\n\n \n\nB\n\n"
    assert main.split_into_blocks(text) == ["A", "B"]


# REGEX ENTITIES 

def test_regex_entities_extracts_dob_and_phone(nlp_minimal):
    doc = nlp_minimal("John Smith Bn: 12/05/1990 called 07123456789 in London.")
    labels = {ent.label_ for ent in doc.ents}
    texts = [ent.text for ent in doc.ents]

    assert "DOB" in labels
    assert any("12/05/1990" in t for t in texts)
    assert "PHONE" in labels
    assert any("07123456789" in t for t in texts)


# RULE-BASED EVENT EXTRACTION 

def test_rule_based_extract_events_finds_assault(nlp_minimal):
    os.environ.setdefault("OPENAI_API_KEY", "test-key")
    import main

    text = """
John Smith Bn: 12/05/1990 was seen in London.
He attacked a male at 21:30.
"""
    events = main.extract_events(text, nlp_minimal)
    assert isinstance(events, list)
    assert len(events) >= 1

    ev_texts = " ".join((e.get("evidence_text") or "") for e in events).lower()
    assert ("attack" in ev_texts) or ("attacked" in ev_texts)
    assert any(e.get("suspect") for e in events)


def test_extract_events_sets_home_address(nlp_for_home_address):
    os.environ.setdefault("OPENAI_API_KEY", "test-key")
    import main

    text = """
John Smith was seen in London. 10 High Street. 99 Low Street.
He attacked a male at 21:30.
"""
    events = main.extract_events(text, nlp_for_home_address)
    assert events
    assert any(ev.get("home_address") == "10 High Street" for ev in events)


# LLM EXTRACTOR (MOCKED CLIENT)

def test_llm_extractor_mocked(monkeypatch):
    os.environ.setdefault("OPENAI_API_KEY", "test-key")
    import data_processing.event_extractor as ex

    class FakeClient:
        class responses:
            @staticmethod
            def create(**kwargs):
                payload = {
                    "events": [
                        {
                            "event_type": "assault",
                            "title": "Attack",
                            "datetime_start": None,
                            "datetime_end": None,
                            "location": "London",
                            "home_address": None,
                            "people": ["John Smith"],
                            "organizations": [],
                            "vehicles": [],
                            "telecom": [],
                            "objects": [],
                            "description": "John attacked someone.",
                            "source_text_span": "attacked",
                        }
                    ]
                }
                return types.SimpleNamespace(output_text=json.dumps(payload))

    monkeypatch.setattr(ex, "client", FakeClient())

    out = ex.extract_events_from_text("John Smith attacked a male in London.")
    assert isinstance(out, dict)
    assert "events" in out and isinstance(out["events"], list)
    assert out["events"][0]["location"] == "London"


# LLM + SPACY ALIGNMENT (MOCKED LLM) 

def test_alignment_scoring_with_mocked_llm(nlp_minimal):
    os.environ.setdefault("OPENAI_API_KEY", "test-key")
    import main

    doc = nlp_minimal("John Smith attacked someone in London.")
    idx = main.build_entity_index(doc)

    llm_event = {
        "event_type": "assault",
        "title": "Attack",
        "location": "London",
        "participants": ["John Smith"],
        "people": ["John Smith"],
        "vehicles": [],
        "telecom": [],
        "objects": [],
        "description": "John attacked someone.",
        "source_text_span": "attacked",
    }

    scores = main.score_llm_event_against_spacy(llm_event, idx)
    assert isinstance(scores, dict)
    assert "participant_match_ratio" in scores

    decision = main.should_accept_llm_event(llm_event, scores)
    assert isinstance(decision, bool)


# PROFILE BLOCKS

def test_profile_blocks_split_and_parse():
    import profile_blocks as pb

    text = """
Intelligence provides that
John SMITH
Bn: 12/05/1990
aka: Johnny
10 High Street
SW1A 1AA
He is believed to be dealing drugs in London.

Intelligence provides that
No profile here, just narrative starts
He was seen in Glasgow.
""".strip()

    reports = pb.split_reports(text)
    assert len(reports) == 2

    profile1, body1 = pb.parse_profile_block(reports[0])
    assert profile1 is not None
    assert profile1["name"] == "John SMITH"
    assert profile1.get("dob") == "12/05/1990"
    assert profile1.get("alias") == "Johnny"
    assert profile1.get("address") == "10 High Street"
    assert profile1.get("postcode") == "SW1A 1AA"
    assert "dealing drugs" in body1.lower()

    profile2, body2 = pb.parse_profile_block(reports[1])
    assert profile2 is None
    assert "glasgow" in body2.lower()


def test_profile_blocks_edge_cases():
    import profile_blocks as pb

    reports = pb.split_reports("")
    assert isinstance(reports, list)

    reports2 = pb.split_reports("Random narrative only\nNo profile\n")
    assert reports2
    profile, body = pb.parse_profile_block(reports2[0])
    assert profile is None
    assert isinstance(body, str)

    reports3 = pb.split_reports("Intelligence provides that\nJane DOE\nSome narrative.\n")
    assert reports3
    profile3, body3 = pb.parse_profile_block(reports3[0])
    assert isinstance(body3, str)


# MAIN_F END-TO-END (WITHOUT NETWORK, MOCKED LLM) 

def test_main_main_runs_in_tmpdir_without_network(monkeypatch, tmp_path, capsys):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.chdir(tmp_path)

    (tmp_path / "Logs.txt").write_text(
        "John Smith Bn: 12/05/1990 was seen in London.\nHe attacked a male at 21:30.\n",
        encoding="utf-8",
    )

    import main
    monkeypatch.setattr(main, "llm_extract_events", lambda block: {"events": []})

    main.main()

    out_path = tmp_path / "events.json"
    assert out_path.exists()
    data = json.loads(out_path.read_text(encoding="utf-8"))
    assert isinstance(data, list)

    captured = capsys.readouterr()
    assert "EVENTS (JSON)" in captured.out


def test_main_runs_with_llm_events_and_alignment(monkeypatch, tmp_path):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.chdir(tmp_path)

    (tmp_path / "Logs.txt").write_text(
        "John Smith Bn: 12/05/1990 lives at 10 High Street.\n"
        "He attacked a male in London at 21:30.\n"
        "Vehicle: black car reg AB12CDE phone 07123456789.\n",
        encoding="utf-8",
    )

    import main

    llm_payload = {
        "events": [
            {
                "event_type": "assault",
                "title": "Attack outside shop",
                "datetime_start": None,
                "datetime_end": None,
                "location": "London",
                "home_address": "10 High Street",
                "participants": ["John Smith"],
                "people": ["John Smith"],
                "organizations": [],
                "vehicles": ["black car", "AB12CDE"],
                "telecom": ["07123456789"],
                "objects": ["knife"],
                "description": "John attacked a male.",
                "source_text_span": "attacked",
            }
        ]
    }

    monkeypatch.setattr(main, "llm_extract_events", lambda block: llm_payload)

    main.main()

    out_path = tmp_path / "events.json"
    assert out_path.exists()
    data = json.loads(out_path.read_text(encoding="utf-8"))
    assert isinstance(data, list)