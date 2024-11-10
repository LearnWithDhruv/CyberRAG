import json

def format_data(data):
    """Formats data into a JSON-friendly format."""
    return json.dumps(data, indent=4)

def check_response(response, expected):
    """Checks if the response contains the expected value."""
    return expected in response
