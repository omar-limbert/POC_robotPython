import base64


# Get "Username - Password" in base64
# @param [String] username
# @param [String] password
# @return [String] base64 code
def get_base64_auth(username, password):
    string_bytes = (username + ":" + password).encode("ascii")
    base64_bytes = base64.b64encode(string_bytes)
    return base64_bytes.decode("ascii")
