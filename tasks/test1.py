import pytest
import requests


def test_get_status_code_equals_200():
    response = requests.get("http://172.26.66.74:1026/v2")
    assert response.status_code == 200


def test_get_check_content_type_equals_json():
    response = requests.get("http://172.26.66.74:1026/v2")
    assert response.headers['Content-Type'] == "application/json"


def test_get_entities_url_equals_entities():
    response = requests.get("http://172.26.66.74:1026/v2")
    response_body = response.json()
    assert response_body["entities_url"] == "/v2/entities"


def test_get_types_url_equals_types():
    response = requests.get("http://172.26.66.74:1026/v2")
    response_body = response.json()
    assert response_body["types_url"] == "/v2/types"


def test_get_subscriptions_url_equals_subscriptions():
    response = requests.get("http://172.26.66.74:1026/v2")
    response_body = response.json()
    assert response_body["subscriptions_url"] == "/v2/subscriptions"


def test_get_registrations_url_equals_registrations():
    response = requests.get("http://172.26.66.74:1026/v2")
    response_body = response.json()
    assert response_body["registrations_url"] == "/v2/registrations"
