import re


REG_REPORT_START = re.compile(r"(?im)^\s*Intelligence provides that\b")

REG_NAME_LINE = re.compile(
    r"^\s*([A-Z][a-z]+)"
    r"(?:\s+(?:['‘’][^'‘’]{1,30}['‘’]))?"
    r"(?:\s+[A-Z][a-z]+)?"
    r"\s+([A-Z]{2,})"
    r"(?:\s+nee\s+([A-Z]{2,}))?"            # nee SURNAME 
    r"\s*$",
)

REG_DOB_LINE = re.compile(r"^\s*Bn\.?\s*[:\-]?\s*(\d{2}/\d{2}/\d{4})\s*$", re.I)
REG_POSTCODE_LINE = re.compile(r"^\s*([A-Z]{1,2}\d{1,2}[A-Z]?\s*\d[A-Z]{2})\s*$", re.I)

REG_ADDRESS_LINE = re.compile(
    r"^\s*(\d{1,4}\s+[A-Z][A-Za-z'’\-]*(?:\s+[A-Z][A-Za-z'’\-]*)*\s+"
    r"(?:Road|Street|Drive|Avenue|Lane|Place|Crescent|Court|Terrace))\s*$",
    re.I
)

REG_ALIAS_LINE = re.compile(
    r"^\s*(?:(may\s+be|possibly|believed\s+to\s+be|thought\s+to\s+be|reported\s+to\s+be)\s+)?"
    r"(aka|a\.k\.a\.|known\s+as|male\s+known\s+as)\s*[:\-]?\s*"
    r"([A-Za-z][A-Za-z0-9'’\-]{1,})\s*$",
    re.I
)

#starters for body bloc - however thinking that listing every possible narrative starter is impossible
# maybe make finite list for profile field lines?
REG_NARRATIVE_START = re.compile(
    r"^\s*(Is|Was|Has|Who|Plans|Regularly|Are|There|He|She|It|The|Note;|Owned by|Registered Keeper)\b",
    re.I
)

def split_reports(text: str) -> list[str]:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    parts = re.split(r"(?im)(?=^\s*Intelligence provides that\b)", text)
    return [p.strip() for p in parts if p.strip()]

def parse_profile_block(report_text: str):
    lines = report_text.replace("\r\n", "\n").replace("\r", "\n").splitlines()

    # find first name-line
    name_i = None
    for i, ln in enumerate(lines):
        if REG_NAME_LINE.match(ln.strip()):
            name_i = i  #record line number
            break

    #no profile block
    if name_i is None:
        return None, report_text.strip()

    #create profile object
    profile = {}
    m = REG_NAME_LINE.match(lines[name_i].strip())
    profile["name"] = f"{m.group(1)} {m.group(2)}"

    profile_lines = [lines[name_i].strip()]
    body_start = name_i + 1

    # collect subsequent lines that look like profile fields (stop when narrative begins)
    for j in range(name_i + 1, min(len(lines), name_i + 15)):
        ln = lines[j].strip()
        if not ln:
            # allow blank line inside block
            profile_lines.append("")
            continue
        #stop when narrativve begins
        if REG_NARRATIVE_START.match(ln):
            body_start = j
            break

        profile_lines.append(ln)
        body_start = j + 1

        # extract fields
        if "dob" not in profile:
            md = REG_DOB_LINE.match(ln)
            if md:
                profile["dob"] = md.group(1)
                continue

        if "alias" not in profile:
            ma = REG_ALIAS_LINE.match(ln)
            if ma:
                profile["alias"] = ma.group(3)
                profile["alias_uncertain"] = bool(ma.group(1))
                continue

        if "address" not in profile:
            madd = REG_ADDRESS_LINE.match(ln)
            if madd:
                profile["address"] = madd.group(1)
                continue

        if "postcode" not in profile:
            mp = REG_POSTCODE_LINE.match(ln)
            if mp:
                profile["postcode"] = mp.group(1)
                continue

    body = "\n".join(lines[body_start:]).strip()
    profile["raw_block"] = "\n".join(profile_lines).strip()

    return profile, body


if __name__ == "__main__":
    with open("logs.txt", encoding="utf-8") as f:
        text = f.read()

    reports = split_reports(text)

    for i, rep in enumerate(reports, 1):
        profile, body = parse_profile_block(rep)
        print(f"\n--- REPORT {i} ---")
        if profile:
            print("PROFILE:")
            for k, v in profile.items():
                print(f"  {k}: {v}")
        else:
            print("PROFILE: None")
        print("BODY (first 200 chars):")
        print(body[:200])