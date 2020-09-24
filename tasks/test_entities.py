import pytest
import requests

url = "http://172.26.66.74:1026"
api = "/v2/entities"
test_json = {
        "type": "qwe111",
        "id": "qwer1",
        "temperature": {
            "value": 21.7
        },
        "humidity": {
            "value": 60
        },
        "location": {
            "value": "41.3763726, 2.1864475",
            "type": "geo:point",
            "metadata": {
                "crs": {
                    "value": "WGS84"
                }
            }
        }
    }


# @pytest.mark.skip()
def test_create_entity_and_get_code_204():
    response = requests.post((url + api), json=test_json)
    assert response.status_code == 201


# @pytest.mark.parametrize("api, expected_place_name", test_data_zip_codes)
def test_get_list_entities_and_code_200():
    response = requests.get(f"{url}{api}")
    assert response.status_code == 200

# def test_get_type_equals_Room():
#     response = requests.get(url + api)
#     response_body = response.json()
#     assert response_body[0]["type"] == "Room"


# def test_get_check_content_type_equals_json():
#     response = requests.get(url + api)
#     assert response.headers['Content-Type'] == "application/json"
#
#
# def test_get_type_equals_Room():
#     response = requests.get(url + api)
#     response_body = response.json()
#     assert response_body[0]["type"] == "Room"
#
#
# def test_get_types_url_equals_types():
#     response = requests.get(url + api)
#     response_body = response.json()
#     assert response_body["types_url"] == "/v2/types"
#
#
# def test_get_subscriptions_url_equals_subscriptions():
#     response = requests.get(url + api)
#     response_body = response.json()
#     assert response_body["subscriptions_url"] == "/v2/subscriptions"
#
#
# def test_get_registrations_url_equals_registrations():
#     response = requests.get(url + api)
#     response_body = response.json()
#     assert response_body["registrations_url"] == "/v2/registrations"
