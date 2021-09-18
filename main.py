import os

import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')
site = os.getenv('SITE')
URL1API = "https://the-one-api.dev/v2/movie"


def test_get_status_code():
    headers = {"Authorization": 'Bearer {}'.format(token)}
    response = requests.request("GET", URL1API, headers=headers)

    return_value = response.status_code
    if return_value == requests.codes.ok:
        assert True
    else:
        assert False


def test_user(host):
    usuarioname = host.user("diogo")
    assert usuarioname.exists
    assert usuarioname.name == "diogo"
    assert usuarioname.uid == 105
    assert usuarioname.gid == 65534
    assert usuarioname.group == "nogroup"
    assert usuarioname.gids == [65534]
    assert usuarioname.groups == ["nogroup"]
    assert usuarioname.shell == "/bin/bash"
    assert usuarioname.home == "/home/diogo"
    assert usuarioname.password == "*"


def test_file(host):
    dirname = host.file("/var/www/tools/")
    assert dirname.is_directory
    assert not dirname.is_file
    filename = host.file("/var/www/tools/tools.log")
    assert filename.exists
    assert filename.is_file


def test_git_is_installed(host):
    git = host.package("git")
    assert git.is_installed
    assert git.version.startswith("1:2")


def test_python_is_installed(host):
    git = host.package("python3")
    assert git.is_installed
    assert git.version.startswith("3.6")


def test_http(host):
    url_site = host.addr(site)
    assert url_site.port(80).is_reachable


def test_https(host):
    url_site = host.addr(site)
    assert url_site.port(443).is_reachable
