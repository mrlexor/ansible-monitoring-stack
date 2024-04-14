import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("dirs", [
    "/etc/alertmanager",
    "/var/lib/alertmanager",
])
def test_directories(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("files", [
    "/etc/alertmanager/alertmanager.yml",
])
def test_files(host, files):
    f = host.file(files)
    assert f.is_file
    assert f.exists


def test_alertmanager_operating(host):
    curl = host.ansible('uri', 'url=http://localhost:9093 '
                               'validate_certs=False',
                        check=False)
    assert (curl['status'] == 200)

    r = host.socket('tcp://0.0.0.0:9093')
    assert (r.is_listening)
