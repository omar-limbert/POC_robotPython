from resources.support.common.singleton_manager import DataManager


# Build url to do a authentication request
# @return [String] that contains authentication url
def auth_url():
    return DataManager().api_config['TODOLY']['api_url_base'] + DataManager().api_config['TODOLY']['api_token_endpoint']


# Build url do a POST request
# @return [String] that contains the endpoint to do a post request
def post_url(endpoint):
    return DataManager().api_config['TODOLY']['api_url_base'] + \
           "/" + endpoint + DataManager().api_config['TODOLY']['format_type']


# Build url do a PUT request
# @return [String] that contains the endpoint to do a get request
# @return [String] that contains the id to do a get request
def put_url(endpoint, object_id):
    return DataManager().api_config['TODOLY']['api_url_base'] + \
           "/" + endpoint + \
           "/" + str(object_id) + DataManager().api_config['TODOLY']['format_type']


# Build url do a GET request
# @return [String] that contains the endpoint to do a get request
# @return [String] that contains the id to do a get request
def get_url(endpoint, object_id):
    return DataManager().api_config['TODOLY']['api_url_base'] + \
           "/" + endpoint + \
           "/" + str(object_id) + DataManager().api_config['TODOLY']['format_type']


# Build url do a DELETE request
# @return [String] that contains the endpoint to do a delete request
# @return [String] that contains the id to do a get request
def delete_url(endpoint, object_id):
    return DataManager().api_config['TODOLY']['api_url_base'] + \
           "/" + endpoint + \
           "/" + str(object_id) + DataManager().api_config['TODOLY']['format_type']
