*** Settings ***
Library  ../resources/support/controllers/login_controller.py
Library  ../resources/support/controllers/data_controller.py

*** Variables ***

*** Keywords ***
I get token as:
    [Arguments]   ${user}
    generate token  ${user}
    ${token} =  get data by key  @token
    log to console  "Token: ${token}"
