import json


# Method to Create Project by API
# @param values [String], contains data to execute POST Action
# @return reference [String], reference
# @return body [JSON], payload to execute the request.
def get_body_and_reference(body):
    reference = body['Reference']
    del body['Reference']
    return reference, body['Body']


