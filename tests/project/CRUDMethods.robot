*** Settings ***
Library      RequestsLibrary
Library      Collections
Resource     ../../keywords/common/common_keywords.robot
Resource     ../../keywords/common/validation_keywords.robot
Resource     ../../keywords/project/project_keywords.robot
Library      DebugLibrary
*** Variables ***
${post_project_body}=       {"Reference":"@post_project", "Body":{"Content":"Api Project Test", "Icon":4, "Deleted": False }}
${get_project_body}=        {"Reference":"@get_project", "Body":{"Content":"Api Project Test", "ItemsCount":0, "Icon":4, "Deleted": False, "ItemType": 2, "ParentId": None, "Collapsed": False, "Children": [], "IsProjectShared": False, "ProjectShareOwnerName": None }}
${put_project_body}=        {"Reference":"@updated_project", "Body":{"Content":"Api Project Test UPDATED", "Icon":2}}
${delete_project_body}=     {"Reference":"@post_project", "Body":{"Content":"Api Project Test", "Icon":4, "Deleted": True }}
*** Test Cases ***

Scenario: POST Project as User 1
    [Tags]  Acceptance    Api
    Given I get token as:  User 1
    When I create Project with following information  ${post_project_body}
    Then I expect HTTP status code:  200
      And The project should be contains following data  ${post_project_body}


Scenario: PUT Project as User 1
    [Tags]  Acceptance    Api
    Given I get token as:  User 1
      # Precondittion: create project
      And I create Project with following information  ${post_project_body}

    When I update Project with following information     @post_project  ${put_project_body}
    Then I expect HTTP status code:  200
      And The project should be contains following data  ${put_project_body}


Scenario: GET Project as User 1
    [Tags]  Acceptance    Api
    Given I get token as:  User 1
      # Precondittion: create project
      And I create Project with following information  ${post_project_body}
      
    When I get Project and keep response:  @post_project  @get_project
    Then I expect HTTP status code:  200
      And The project should be contains following data  ${get_project_body}


Scenario: DELETE Project as User 1
    [Tags]  Acceptance    Api
    Given I get token as:  User 1
      # Precondittion: create project
      And I create Project with following information  ${post_project_body}

    When I delete Project:  @post_project
    Then I expect HTTP status code:  200
      And The project should be contains following data  ${delete_project_body}
    When I get Project and keep response:  @post_project  @deleted_project
    Then The response should be empty:  @deleted_project

Scenario: POST Project as User 2
    [Tags]  Acceptance    Api
    Given I get token as:  User 2
    When I create Project with following information  ${post_project_body}
    Then I expect HTTP status code:  200
      And The project should be contains following data  ${post_project_body}


Scenario: PUT Project as User 2
    [Tags]  Acceptance    Api
    Given I get token as:  User 2
      # Precondittion: create project
      And I create Project with following information  ${post_project_body}

    When I update Project with following information     @post_project  ${put_project_body}
    Then I expect HTTP status code:  200
      And The project should be contains following data  ${put_project_body}


Scenario: GET Project as User 2
    [Tags]  Acceptance    Api
    Given I get token as:  User 2
      # Precondittion: create project
      And I create Project with following information  ${post_project_body}

    When I get Project and keep response:  @post_project  @get_project
    Then I expect HTTP status code:  200
      And The project should be contains following data  ${get_project_body}


Scenario: DELETE Project as User 2
    [Tags]  Acceptance    Api
    Given I get token as:  User 2
      # Precondittion: create project
      And I create Project with following information  ${post_project_body}

    When I delete Project:  @post_project
    Then I expect HTTP status code:  200
      And The project should be contains following data  ${delete_project_body}
    When I get Project and keep response:  @post_project  @deleted_project
    Then The response should be empty:  @deleted_project
