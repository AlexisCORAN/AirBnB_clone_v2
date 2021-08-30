#!/usr/bin/python3
"""
This file contains the do_deploy(archive_path) function
"""
from fabric.api import env, local, put, run
import os.path
from datetime import datetime
env.hosts = ["35.229.24.103", "54.226.193.179"]



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
    except Exception:
        return None
    else:
        return file_name

def do_deploy(archive_path):
    """
    do_deploy function
    """

    if os.path.isfile(archive_path) is False:
        return False

    try:
        file_n = archive_path.split("/")[-1]
        name = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/{}".format(file_n))
        run("mkdir -p {}{}/".format(path, name))
        run("tar -xzf /tmp/{} -C {}{}".format(file_n, path, name))
        run("rm /tmp/{}".format(file_n))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(name, name))
        run("rm -rf {}{}/web_static".format(path, name))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, name))
    except Exception:
        return False
    else:
        return True

def deploy():
    """
    Creates and distributes an archive to your web servers
    """

    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
