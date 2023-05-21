## Resume-screening URLs

### Info


### Repo Reference
1. https://github.com/aarshps/photo-gallery-python-flask
2. [Test](https://github.com/aarshps/linked-eed)

### Flask Learn Reference
#### 31-Dec-2022
1. https://flask.palletsprojects.com/en/2.2.x/quickstart/
2. https://phoenixnap.com/kb/install-flask
3. https://testdriven.io/courses/learn-flask/intro/
4. https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
#### 1-Jan-2023
1. https://www.digitalocean.com/community/tutorials/how-to-create-your-first-web-application-using-flask-and-python-3
2. https://pemagrg.medium.com/build-a-web-app-using-pythons-flask-for-beginners-f28315256893
#### 30-Jan-2023
1. https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application
#### 14-Feb-2023
1. https://www.geeksforgeeks.org/how-to-upload-file-in-python-flask/

### Resume-screening Reference
1. https://towardsdatascience.com/resume-screening-with-python-1dea360be49b

### Mail-sending Reference
#### 14-May-2023
1. https://youtu.be/ejLGwHiyqGU
2. https://www.w3schools.com/html/html_form_attributes_form.asp
#### 15-May-2023
1. https://youtu.be/1oOefRD8jek

### Keywords
- Git
- Source Control
- Jinja Templates
- Python Package
- Tortoise Git
- Visual Studio Code
- Flask
- Web Application, HTTP, Port, Web Server
- Github, Gitlab, TFS
- Github Pages
- Controller, Service, MVC in Flask
- md, html
- base64

### Installation
### STEP 1 - Install Visual Studio Code
https://www.geeksforgeeks.org/how-to-install-visual-studio-code-on-windows/

### STEP 2 - Install Python
Install Python from python.org. You can typically use the Download Python button that appears first on the page to download the latest version.

While installing python make sure that you install pip alone with it:
https://youtu.be/dYfKJMPNMDw

### STEP 3 - Verify the Python installation
To verify that you've installed Python successfully on your machine, run the following command
Open a command prompt and run the following command:

py -3 --version

if the above code doesn't work then open Windows Powershell, and enter the following:
python --version

If the installation was successful, the output window should show the version of Python that you installed.

### STEP 4 - Install Flask
https://phoenixnap.com/kb/install-flask

### STEP 6 - Code
Clone the code and download required libraries
pip install < required library >

    Libraries:
    1. PyPDF2
    2. pandas
    3. matplotlib.pyplot
    4. re
    5. base64
    6. flask_mail
    7. werkzeug.utils (A bug related to the current version 1.0.0 of workzeug. It's merged but not yet published in pypi. The workaround know until now is to downgrade from werkzeug=1.0.0 to werkzeug==0.16.0

    So for do that you just need run the command:

    pip install -U Werkzeug==0.16.0)

if pip doesn't work, then upgrade pip using following command:
py -m pip install --upgrade pip

### STEP 7 - Run the code
First activate the environment, to actiavte the environment:
C:\users\Documents\Source\resume-screener\<environment name>\Scripts\activate

After the environment is activated get the path back to app.py
C:\users\Documents\Source\resume-screener\resume-screener\app

Then run the following command to get the output:
flask run or python -m flask run
