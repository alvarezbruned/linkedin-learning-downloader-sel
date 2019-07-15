# linkedin-learning-downloader-sel


To run script your credentials and courses go inside the code (in the future it will be a yaml file with credentials and courses)

The courses in code are an array, taken the last part of URL:
example:
https://www.linkeidn.com/learning/python-para-data-science-y-big-data-esencial
in code only write 'python-para-data-science-y-big-data-esencial'

The baseVideoPath is necessary to change, is the destiny of videos courses, this in future it will be as a variable in yaml file.

## Necessary installs:
pip3 install -r requirements.txt

## Driver geckodriver is needed
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
tar -xvzf geckodriver*
mv geckodriver /usr/local/bin
rm geckodriver*
