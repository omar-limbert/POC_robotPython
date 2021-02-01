import json
from resources.support.helpers import payload_manager
from resources.support.controllers import data_controller


# Method to Create Project by API
# @param values [String], contains data to execute POST Action
# @return reference [Boolean], result
# @return body [Dictionary], payload to execute the request.
def validate_information(dictionary):
    reference, expected_body = payload_manager.get_body_and_reference(dictionary)
    actual_body = data_controller.get_data_by_key(reference)
    not_included_data = {}
    result = True
    for key in expected_body:
        if key not in actual_body or expected_body[key] != actual_body[key]:
            result = False
            not_included_data.update({key: actual_body[key]})

    return result, not_included_data
