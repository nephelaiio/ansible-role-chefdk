from testinfra.utils.ansible_runner import AnsibleRunner


testinfra_hosts = \
    AnsibleRunner('.molecule/ansible_inventory').get_hosts('test')


def test_command(host):
    assert host.command('chef-client -v').rc == 0
    assert host.command('berks -v').rc == 0
    assert host.command('knife -v').rc == 0
