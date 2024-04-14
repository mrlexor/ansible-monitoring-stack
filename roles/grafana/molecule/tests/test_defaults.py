import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("dirs", [
    "/etc/grafana",
    "/etc/grafana/provisioning",
    "/etc/grafana/provisioning/dashboards",
    "/etc/grafana/provisioning/datasources",
    "/var/lib/grafana",
])
def test_directories(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("files", [
    "/etc/grafana/provisioning/dashboards/dashboards.yml",
    "/etc/grafana/provisioning/datasources/datasources.yml",
])
def test_files(host, files):
    f = host.file(files)
    assert f.is_file
    assert f.exists


def test_grafana_operating(host):
    curl = host.ansible('uri', 'url=http://localhost:3000'
                               'validate_certs=False',
                        check=False)
    assert (curl['status'] == 200)

    r = host.socket('tcp://0.0.0.0:3000')
    assert (r.is_listening)
