"""Data loader for generator data."""
import json

def load_data(file_path, is_json=False):
    """Load data from a file."""
    if is_json:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    with open(file_path, 'r') as f:
        data = f.read()
    return data