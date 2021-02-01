*** Settings ***
Library      RequestsLibrary
Library      Collections
Resource     ../../keywords/common/common_keywords.robot
Resource     ../../keywords/common/validation_keywords.robot
Resource     ../../keywords/project/project_keywords.robot
*** Variables ***
${project_without_required_field}=    {"Reference":"@post_project", "Body":{"Icon":4, "Deleted": False }}
${project_with_empty_body}=    {"Reference":"@post_project", "Body":{}}
${error_message_post}=    {"Reference":"@post_project", "Body":{"ErrorMessage":"Too Short Project Name", "ErrorCode": 305 }}

${post_project_body}=    {"Reference":"@post_project", "Body":{"Content":"Api Project Test", "Icon":4, "Deleted": False }}
${put_with_invalid_fields}=    {"Reference":"@post_project", "Body":{"ContentINVALID":"Api Project Test", "IconINVALID":4 }}
*** Test Cases ***

Scenario: Negative Cases - POST Project without required fields as User 1
    Given I get token as:  User 1
    When I create Project with following information  ${project_without_required_field}
    Then I expect HTTP status code:  200
      And The project should be contains following data  ${error_message_post}


Scenario: Negative Cases - POST Project with empty body as User 1
    Given I get token as:  User 1
    When I create Project with following information  ${project_with_empty_body}
    Then I expect HTTP status code:  200
      And The project should be contains following data  ${error_message_post}


Scenario: Negative Cases - PUT Project with invalid fields as User 1
    Given I get token as:  User 1
      # Precondittion: create project
      And I create Project with following information  ${post_project_body}

    When I update Project with following information     @post_project  ${put_with_invalid_fields}
    Then I expect HTTP status code:  200
      And The project should be contains following data  ${post_project_body}
