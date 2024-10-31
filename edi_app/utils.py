def parse_edifact_message(message):
    segments = message.split("'")
    parsed_segments = []

    for segment in segments:
        elements = segment.split("+")
        parsed_segments.append(elements)

    return parsed_segments

def validate_edifact_message(parsed_message):
    required_segments = {"UNH", "BGM", "DTM"}
    found_segments = {segment[0] for segment in parsed_message if segment}
    missing_segments = required_segments - found_segments
    return len(missing_segments) == 0, missing_segments
