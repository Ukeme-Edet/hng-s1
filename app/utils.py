#!/usr/bin/env python
"""
This module contains utility functions for the application.
"""
import requests
# from requests.structures import CaseInsensitiveDict
from dotenv import load_dotenv
from os import getenv

load_dotenv(override=True)


# def get_client_location(ip_address):
#     """
#     Get the location of the client using their IP address.

#     Args:
#         ip_address (str): The IP address of the client.

#     Returns:
#         str: The location of the client.
#     """
#     url = f"https://api.geoapify.com/v1/ipinfo?ip={ip_address}&apiKey={getenv('GEOAPIFI_API_KEY')}"

#     headers = CaseInsensitiveDict()
#     headers["Accept"] = "application/json"

#     resp = requests.get(url, headers=headers)
#     data = resp.json()

#     return data.get("city").get("name")


# def get_client_location_temp(city):
#     """
#     Get the location of the client using their IP address.

#     Args:
#         city (str): The city of the client.

#     Returns:
#         str: The location of the client.
#     """
#     url = f"https://api.weatherapi.com/v1/current.json?key={getenv('WEATHER_API_KEY')}&q={city}"

#     resp = requests.get(url)
#     data = resp.json()

#     return data.get("current").get("temp_c")


def get_client_data(ip_address):
    """
    Get the location and temperature of the client using their IP address.

    Args:
        ip_address (str): The IP address of the client.

    Returns:
        dict: The location and temperature of the client.
    """
    url = f"https://api.weatherapi.com/v1/current.json?key={getenv('WEATHER_API_KEY')}&q={ip_address}"

    resp = requests.get(url)
    data = resp.json()

    return {
        "location": data.get("location").get("name"),
        "temp": data.get("current").get("temp_c"),
    }
