*** Settings ***
Library  ../../resources/support/controllers/project_controller.py
Library  Collections
*** Variables ***
${URL}  http://www.google.com

*** Keywords ***
I create Project with following information
    [Arguments]    @{project_information}
    ${dictionary}=          evaluate  @{project_information}
    ${dictionary}=          convert to dictionary  ${dictionary}
    post project       ${dictionary}


I update Project with following information
    [Arguments]    ${project_reference}     @{project_information}
    ${dictionary}=          evaluate  @{project_information}
    ${dictionary}=          convert to dictionary  ${dictionary}
    put project  ${project_reference}   ${dictionary}


I get Project and keep response:
    [Arguments]     ${project_reference}    ${project_reference_to_keep}
    get project  ${project_reference}   ${project_reference_to_keep}

I delete Project:
    [Arguments]     ${project_reference}
    delete project  ${project_reference}