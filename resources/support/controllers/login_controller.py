from resources.support.helpers import api_manager
from resources.support.helpers import endpoint_manager
from resources.support.common.singleton_manager import DataManager
from resources.support.controllers import data_controller
from resources.support.utilities import token_generator


# Makes the Request to obtain the api' token
# @param [String] user
def generate_token(user):
    username = DataManager().api_config['CREDENTIALS'][user]['username']
    password = DataManager().api_config['CREDENTIALS'][user]['password']

    auth = token_generator.get_base64_auth(username, password)
    headers = {'Authorization': "Basic " + auth}
    api_manager.get(endpoint_manager.auth_url(), headers=headers)
    response = data_controller.get_data_by_key('@response')
    token = response['TokenString'] if 'TokenString' in response else response['ErrorMessage']
    data_controller.add_data('@token', token)
