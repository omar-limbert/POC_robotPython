from resources.support.common.singleton_manager import DataManager


# Method to add data into api_data hash
# @param key [String], key
# @param value [String], value
def add_data(key, value):
    DataManager().get_api_data().update({key: value})


# Method to get data from api_data hash by key
# @param key [String], key
# @return [String] value
def get_data_by_key(key):
    return DataManager().get_api_data().get(key)


# Method to get api_data
# @return [String] hash
def get_data():
    return DataManager().get_api_data()
