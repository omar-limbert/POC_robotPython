*** Settings ***
Library           ../../../resources/support/controllers/login_controller.py
Library           ../../../resources/support/controllers/data_controller.py
Library           ../../../resources/support/controllers/validation_controller.py
Library           Collections
*** Variables ***

*** Keywords ***
I expect HTTP status code:
    [Arguments]     ${status_code}
    ${expected_status_code}=    convert to integer  ${status_code}
    ${actual_status_code}=      get data by key     @status_code
    should be equal  ${actual_status_code}   ${expected_status_code}


The project should be contains following data
    [Arguments]    @{project_information}
    ${dictionary}=              evaluate  @{project_information}
    ${dictionary}=              convert to dictionary  ${dictionary}
    ${expected_values} =        get from dictionary   ${dictionary}   Body
    ${validation_values}=       validate information  ${dictionary}
    should be true  ${validation_values[0]}    Expected Values: ${expected_values} \nNot Matched Values: ${validation_values[1]}


The response should be empty:
    [Arguments]    ${project_reference}
    ${response}=                get data by key     ${project_reference}
    ${actual_response}=         convert to string     ${response}
    should be equal     ${actual_response}  None    The response is not Empty:\n${response}
