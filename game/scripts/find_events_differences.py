from src.witch.events import load_events


PATH = "src/witch/events/"


def find_duplicate_positions(left, right):
    duplicate_positions = []
    for event in left:
        for other in right:
            if event.where == other.where:
                duplicate_positions.append(event.where)
                break

    return duplicate_positions


def filter_events(events, duplicates):
    result = []
    for event in events:
        valid = True
        for dupe in duplicates:
            if event.where == dupe:
                valid = False
                break
        if valid:
            result.append(event)
    return result


def find_differences(events1, events2):
    duplicates = find_duplicate_positions(events1, events2)
    only_in_first = filter_events(events1, duplicates)
    only_in_second = filter_events(events2, duplicates)

    return only_in_first, only_in_second



if __name__ == "__main__":
    lan1 = "polish"
    lan2 = "english"
    events1 = load_events(lan1)
    events2 = load_events(lan2)
    print(f"{len(events1)} events in {lan1}, {len(events2)} events in {lan2}.")
    only_in_first, only_in_second = find_differences(events1, events2)

    print(f"Events only in {lan1}:")
    for event in only_in_first:
        print(f"{event.where}")
    print()

    print(f"Events only in {lan2}:")
    for event in only_in_second:
        print(f"{event.where}")
    print()

