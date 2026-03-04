import json
from data_processing.event_extractor import extract_events_from_text

def main():
    with open("Logs.txt", "r", encoding="utf-8") as f:
        text = f.read()
    
    print("Extracting events from text...")
    result = extract_events_from_text(text)
    events = result.get("events", [])
    
    print(f"Found {len(events)} events")
    
    # Save to JSON
    with open("events.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    
    # Print summary
    for i, event in enumerate(events, 1):
        print(f"\n{i}. {event.get('title', 'Untitled')} ({event.get('event_type', 'unknown')})")
        if event.get('participants'):
            print(f"   Participants: {', '.join(event['participants'])}")

if __name__ == "__main__":
    main()