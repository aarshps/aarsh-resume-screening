# Installation

- Install Visual Studio Code
    - https://www.geeksforgeeks.org/how-to-install-visual-studio-code-on-windows/
- Install Python
    - Install Python from python.org
    - You can typically use the Download Python button that appears first on the page to download the latest version
    - While installing python make sure that you install pip along with it
        - https://youtu.be/dYfKJMPNMDw
- Verify the Python installation
    - To verify that you've installed Python successfully on your machine, run the following command
    - Open a command prompt and run the following command:
        - ```py -3 --version```
    - If the installation was successful, the output window should show the version of Python that you installed.
- Install Flask
    - https://phoenixnap.com/kb/install-flask
- Code
    - Copy the code and download required libraries
        - ```pip install < required library >```
        Libraries:
    1. PyPDF2
    2. pandas
    3. matplotlib.pyplot
    4. re
    5. base64
    6. flask_mail
    7. werkzeug.utils (A bug related to the current version 1.0.0 of workzeug. It's merged but not yet published in pypi. The workaround know until now is to downgrade from        werkzeug=1.0.0 to werkzeug==0.16.0)
    So for do that you just need run the command:
        - ```pip install -U Werkzeug==0.16.0```
    - If pip doesn't work, then upgrade pip using following command:
        - ```py -m pip install --upgrade pip```
- Run the code
    - First activate the environment, to actiavte the environment:
        - ```C:\users\Documents\Source\resume-screener\<environment name>\Scripts\activate```
    - After the environment is activated get the path back to app.py
        - ```C:\users\Documents\Source\resume-screener\resume-screener\app```
    - Then run the following command to get the output:
        - ```flask run or python -m flask run```
