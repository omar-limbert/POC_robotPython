TODO.LY - AUTOMATION FRAMEWORK SAMPLE
Technologies

  * Robot Framework: <https://robotframework.org/>
  * Python 3.9: <https://www.python.org/>

FRAMEWORK REQUIREMENTS
CONFIGURE DEVELOPMENT ENVIRONMENT

    Install Python 3.9
    Clone the repository.
    Install required libraries.

Install required gem with Bundler gem
   
    Execute the following command:

    pip install robotframework
    
    pip install robotframework-requests
    
    pip install pyyaml
   

EXECUTE TEST FILES

    python.exe -m robot.run tests/
    python.exe -m robot.run -i Acceptance tests/
