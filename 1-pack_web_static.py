#!/usr/bin/python3
"""
THis file contains do_pack() function
"""
from fabric.api import local
import os.path
from datetime import datetime

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    try:
        form = "%Y%m%d%H%M%S"
        date = datetime.now().strftime(form)
        file_name = "versions/web_static_{}.tgz".format(date)
        if os.path.isdir("versions") is False:
            local("mkdir versions")
        local("tar -cvzf {} web_static".format(file_name))
    except:
        return None
    else: 
        return file_name
