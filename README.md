# nephelaiio.chefdk

[![Build Status](https://travis-ci.org/nephelaiio/ansible-role-chefdk.svg?branch=master)](https://travis-ci.org/nephelaiio/ansible-role-chefdk)
[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-systemd--service-blue.svg)](https://galaxy.ansible.com/nephelaiio/chefdk/)

An [ansible role](https://galaxy.ansible.com/nephelaiio/chefdk) to install and configure [chefdk](https://downloads.chef.io/chefdk)

## Role Variables

Please refer to the [defaults file](/defaults/main.yml) for an up to date list of input parameters.

## Example Playbook

```
- hosts: servers
  roles:
     - role: chefdk
       chefdk_packages_state: latest
```

## Testing

Please make sure your environment has [docker](https://www.docker.com) installed in order to run role validation tests. Additional python dependencies are listed in the [requirements file](https://github.com/nephelaiio/ansible-role-requirements/blob/master/requirements.txt)

Role is tested against the following distributions (docker images):
  * Ubuntu Bionic
  * Ubuntu Xenial
  * CentOS 7
  * Debian Stretch

You can test the role directrly from sources using command ` molecule test `

## License

This project is licensed under the terms of the [MIT License](/LICENSE)
