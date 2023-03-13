#!/usr/bin/env python
import urllib.request

def Download(file, path):
    """
    Downloads a file from the web.
    File: the website of the file
    Path: The path to save it (Put the name of the file with the type.)
    """
    filename, headers = urllib.request.urlretrieve(file, filename=path)
    return
