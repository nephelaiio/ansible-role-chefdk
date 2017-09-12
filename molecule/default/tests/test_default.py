import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_command(host):
    assert host.command('chef-client -v').rc == 0
    assert host.command('berks -v').rc == 0
    assert host.command('knife -v').rc == 0
