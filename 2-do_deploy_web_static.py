#!/usr/bin/python3
"""
This file contains the do_deploy(archive_path) function
"""
from fabric.api import env, put, run
import os.path
env.hosts = ["35.229.24.103", "54.226.193.179"]


def do_deploy(archive_path):
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
