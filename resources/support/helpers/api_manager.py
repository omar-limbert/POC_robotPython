import requests
from resources.support.utilities import utility
from resources.support.controllers import data_controller


# Method to execute GET request.
# @param url [String]: URI where the request is sent.
# @param body [JSON file]: payload information to send on body.
# @param header [JSON file]: header information.
def get(url, body={}, headers=None):
    if headers is None:
        headers = {'Token': data_controller.get_data_by_key('@token')}
    response = requests.get(url, headers=headers)
    utility.keep_and_print_request_information('GET', url, body, response)


# Method to execute POST request.
# @param url [String]: URI where the request is sent.
# @param body [JSON file]: payload information to send on body.
# @param header [JSON file]: header information.
def post(url, body, headers=None):
    if headers is None:
        headers = {'Token': data_controller.get_data_by_key('@token'), 'Content-Type': 'application/json'}
    response = requests.post(url, data=body, headers=headers)
    utility.keep_and_print_request_information('POST', url, body, response)


# Method to execute PUT request.
# @param url [String]: URI where the request is sent.
# @param body [JSON file]: payload information to send on body.
# @param header [JSON file]: header information.
def put(url, body, headers=None):
    if headers is None:
        headers = {'Token': data_controller.get_data_by_key('@token'), 'Content-Type': 'application/json'}
    response = requests.put(url, data=body, headers=headers)
    utility.keep_and_print_request_information('PUT', url, body, response)


# Method to execute DELETE request.
# @param url [String]: URI where the request is sent.
# @param body [JSON file]: payload information to send on body.
# @param header [JSON file]: header information.
def delete(url, body={}, headers=None):
    if headers is None:
        headers = {'Token': data_controller.get_data_by_key('@token'), 'Content-Type': 'application/json'}
    response = requests.delete(url, data=body, headers=headers)
    utility.keep_and_print_request_information('DELETE', url, body, response)
