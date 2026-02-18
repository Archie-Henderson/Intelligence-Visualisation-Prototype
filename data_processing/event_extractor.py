import json
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

EVENT_SCHEMA_INSTRUCTIONS = """
Return ONLY valid JSON (no markdown, no commentary).

Schema:
{
  "events": [
    {
      "event_type": "meeting|call|threat|assault|transaction|travel|arrest|unknown",
      "title": "short label",
      "datetime_start": "ISO-8601 string or null",
      "datetime_end": "ISO-8601 string or null",
      "location": "string or null",
      "people": ["string"],
      "organizations": ["string"],
      "vehicles": ["string"],
      "telecom": ["integer"],
      "objects": ["string"],
      "description": "1-3 sentences",
      "source_text_span": "short verbatim snippet from the input"
    }
  ]
}

Rules:
- Extract only events that are clearly stated or strongly implied.
- If time is vague/relative ("yesterday"), leave datetime_* as null unless a concrete date is present.
- If nothing is found, return {"events": []}.
"""

def extract_events_from_text(text: str) -> dict:
    prompt = f"{EVENT_SCHEMA_INSTRUCTIONS}\n\nTEXT:\n{text}"

    resp = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
    )

    raw = (resp.output_text or "").strip()
    return json.loads(raw)
