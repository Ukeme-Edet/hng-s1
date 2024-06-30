#!/usr/env/bin python
"""
This is the main file for the application server.
"""
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
