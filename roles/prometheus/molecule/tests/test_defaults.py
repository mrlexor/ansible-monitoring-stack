import json
import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("dirs", [
    "/etc/prometheus",
    "/etc/prometheus/rules",
    "/etc/prometheus/targets",
    "/var/lib/prometheus",
])
def test_directories(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("files", [
    "/etc/prometheus/prometheus.yml",
    "/etc/prometheus/rules/default.rules.yml",
    "/etc/prometheus/rules/custom.rules.yml",
    "/etc/prometheus/targets/custom.targets.yml",
])
def test_files(host, files):
    f = host.file(files)
    assert f.is_file
    assert f.exists


@pytest.mark.parametrize("jobname", [
    'prometheus',
])
def test_prometheus_targets_up(host, jobname):
    out = host.check_output('curl http://localhost:9090/api/v1/targets')
    targets = json.loads(out)['data']['activeTargets']
    found = False
    for t in targets:
        if t['labels']['job'] == jobname:
            found = True
            assert t['health'] == 'up'
    assert found


def test_prometheus_metrics_up(host):
    out = host.check_output(
        'curl http://localhost:9090/api/v1/query?query=up')
    assert 'up' in out
