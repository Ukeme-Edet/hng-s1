#!/usr/bin/env python
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

    Returns:
        str: A greeting message to the client.
    """
    request_data = request.args
    client_name = request_data.get("visitor_name")
    client_ip = request.remote_addr
    client_location = get_client_location(client_ip)
    client_temp = get_client_location_temp(client_location)

    return jsonify(
        {
            "client_ip": client_ip,
            "location": client_location,
            "greeting": f"Hello, {client_name}!, the temperature in \
                {client_location} is {client_temp} degrees celsius in {client_location}",
        }
    )
