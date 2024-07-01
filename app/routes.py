#!/usr/bin/env python
"""
This module contains the routes for the Flask application.

It defines a Blueprint named 'api' that handles API routes.
"""
from flask import Blueprint, jsonify, request
from dotenv import load_dotenv
from app.utils import get_client_location, get_client_location_temp

# Force the reload of the .env file
load_dotenv(override=True)

api = Blueprint("api", __name__)


@api.route("/hello", methods=["GET"])
def hello():
    """
    This route returns a greeting message to the client.

    It retrieves the client's name from the request arguments and the client's IP address from the request headers.
    It then uses the client's IP address to determine the client's location and fetches the temperature at that location.
    Finally, it returns a JSON response containing the client's IP address, location, and a greeting message.

    Returns:
        dict: A JSON response containing the client's IP address, location, and greeting message.
    """
    request_data = request.args
    client_name = request_data.get("visitor_name", "visitor")
    client_name = client_name.strip('"')
    client_ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    client_location = get_client_location(client_ip)
    client_temp = get_client_location_temp(client_location)

    return jsonify(
        {
            "client_ip": client_ip,
            "location": client_location,
            "greeting": f"Hello, {client_name}!, the temperature is {client_temp} degrees celsius in {client_location}",
        }
    )
