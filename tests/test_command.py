from testinfra.utils.ansible_runner import AnsibleRunner


testinfra_hosts = \
    AnsibleRunner('.molecule/ansible_inventory').get_hosts('test')


def test_command(Command):
    assert Command('chef-client -v').rc == 0
    assert Command('berks -v').rc == 0
    assert Command('knife -v').rc == 0
