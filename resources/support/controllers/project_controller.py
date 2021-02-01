from resources.support.helpers import api_manager
from resources.support.helpers import endpoint_manager
from resources.support.helpers import payload_manager
from resources.support.controllers import data_controller
import json

__PROJECT_ENDPOINT__ = 'projects'


# Method to Create Project by API
# @param project_values [Dictionary], contains data to execute POST Action
def post_project(project_values):
    reference, body = payload_manager.get_body_and_reference(project_values)
    url = endpoint_manager.post_url(__PROJECT_ENDPOINT__)
    api_manager.post(url, json.dumps(body))
    if len(data_controller.get_data_by_key('@response')) > 0:
        data_controller.add_data(reference, data_controller.get_data_by_key('@response'))


# Method to Update Project by API
# @param project_reference [String], contains project reference
# @param project_values [Dictionary], contains data to execute POST Action
def put_project(object_reference, project_values):
    result_reference, body = payload_manager.get_body_and_reference(project_values)
    url = endpoint_manager.put_url(__PROJECT_ENDPOINT__, data_controller.get_data_by_key(object_reference)['Id'])
    api_manager.put(url, json.dumps(body))
    if 'Id' in data_controller.get_data_by_key('@response'):
        data_controller.add_data(result_reference, data_controller.get_data_by_key('@response'))


# Method to Get Project by API
# @param project_reference [String], contains project reference
# @param project_reference_to_keep [String], contains project reference to keep the response
def get_project(object_reference, project_reference_to_keep):
    url = endpoint_manager.get_url(__PROJECT_ENDPOINT__, data_controller.get_data_by_key(object_reference)['Id'])
    api_manager.get(url)
    if 'Id' in data_controller.get_data_by_key('@response'):
        data_controller.add_data(project_reference_to_keep, data_controller.get_data_by_key('@response'))


# Method to Delete Project by API
# @param project_reference [String], contains project reference to delete
def delete_project(object_reference):
    url = endpoint_manager.delete_url(__PROJECT_ENDPOINT__, data_controller.get_data_by_key(object_reference)['Id'])
    api_manager.delete(url)
    if 'Id' in data_controller.get_data_by_key('@response'):
        data_controller.add_data(object_reference, data_controller.get_data_by_key('@response'))
