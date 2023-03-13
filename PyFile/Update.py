#!/usr/bin/env python
import urllib.request

YouTube = "https://raw.githubusercontent.com/ChristianHiland/PyFile/main/PyFile/YouTube.py"
File = "https://raw.githubusercontent.com/ChristianHiland/PyFile/main/PyFile/File.py"
Upload = "https://raw.githubusercontent.com/ChristianHiland/PyFile/main/PyFile/Upload.py"
Update = "https://raw.githubusercontent.com/ChristianHiland/PyFile/main/PyFile/Update.py"
init = "https://raw.githubusercontent.com/ChristianHiland/PyFile/main/PyFile/__init__.py"

def All():
    filename, headers = urllib.request.urlretrieve(YouTube)
    filename, headers = urllib.request.urlretrieve(File)
    filename, headers = urllib.request.urlretrieve(Upload)
    filename, headers = urllib.request.urlretrieve(init)
    filename, headers = urllib.request.urlretrieve(Update)
def Min():
    filename, headers = urllib.request.urlretrieve(YouTube)
    filename, headers = urllib.request.urlretrieve(File)
    filename, headers = urllib.request.urlretrieve(Upload)