from dateutil.parser import isoparse
from django.utils.timezone import get_current_timezone, make_aware

from data_processing.event_extractor import extract_events_from_text
from data_processing.models import Event, Document

def _parse_dt(dt_str):
    if not dt_str:
        return None
    dt = isoparse(dt_str)
    if dt.tzinfo is None:
        dt = make_aware(dt, get_current_timezone())
    return dt


def extract_and_store_events(document_id: int) -> int:
    doc = Document.objects.get(id=document_id)

    result = extract_events_from_text(doc.text)
    events = result.get("events", [])

    created = 0
    for e in events:
        Event.objects.create(
            document=doc,
            event_type=e.get("event_type", "unknown"),
            title=(e.get("title") or "")[:200],
            datetime_start=_parse_dt(e.get("datetime_start")),
            datetime_end=_parse_dt(e.get("datetime_end")),
            location=e.get("location"),
            people=e.get("participants", []) or [],
            organizations=e.get("organizations", []) or [],
            vehicles=e.get("vehicles", []) or [],
            telecom=e.get("telecom", []) or [],
            objects=e.get("objects", []) or [],
            description=e.get("description", "") or "",
            confidence=float(e.get("confidence", 0.0) or 0.0),
            source_text_span=e.get("source_text_span", "") or "",
        )
        created += 1

    return created
