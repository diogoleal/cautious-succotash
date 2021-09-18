import os

import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')
site = os.getenv('SITE')
url_t1api = "https://the-one-api.dev/v2/movie"


def test_get_status_code():
    headers = {"Authorization": 'Bearer {}'.format(token)}
    response = requests.request("GET", url_t1api, headers=headers)

    return_value = response.status_code
    if return_value == requests.codes.ok:
        assert True
    else:
        assert False


def test_user(host):
    d = host.user("diogo")
    assert d.exists
    assert d.name == "diogo"
    assert d.uid == 105
    assert d.gid == 65534
    assert d.group == "nogroup"
    assert d.gids == [65534]
    assert d.groups == ["nogroup"]
    assert d.shell == "/bin/bash"
    assert d.home == "/home/diogo"
    assert d.password == "*"


def test_file(host):
    d = host.file("/var/www/tools/")
    assert d.is_directory
    assert not d.is_file
    f = host.file("/var/www/tools/tools.log")
    assert f.exists
    assert f.is_file


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
