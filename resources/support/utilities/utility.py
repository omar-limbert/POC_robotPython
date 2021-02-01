import json
from resources.support.controllers import data_controller


def keep_and_print_request_information(method, url, body, response):
    data_controller.add_data('@status_code', response.status_code)
    try:
        message = json.loads(json.dumps(response.json()))
    except Exception:
        message = json.loads(json.dumps([])) if (len(response.content) == 0) else response.content

    data_controller.add_data('@response', message)
    print("%s => %s \n"
          "Body: %s \n"
          "Status Code: %s \n"
          "Response: %s" % (method, url, body, response.status_code, message))
