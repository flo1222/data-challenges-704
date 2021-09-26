# pylint: disable=missing-docstring

import os

def start():
    if 'FLASK_ENV' in os.environ:
        return f"Starting in {os.environ['FLASK_ENV']} mode..."
    return "Starting in production mode..."

if __name__ == "__main__":
    print(start())
