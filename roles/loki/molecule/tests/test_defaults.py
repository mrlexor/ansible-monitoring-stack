import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("dirs", [
    "/etc/loki",
    "/var/lib/loki",
    "/var/lib/loki/rules",
])
def test_directories(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("files", [
    "/etc/loki/config.yml",
])
def test_files(host, files):
    f = host.file(files)
    assert f.is_file
    assert f.exists
