# my_own_namespace.yandex_cloud_elk

Custom Ansible Collection created as a homework assignment.

## Description

This collection contains:
- a custom Ansible module for creating a text file on a target host
- an example playbook for using the module

The module creates a file at the specified path with the given content.
The module is idempotent and supports check mode.

## Requirements

- Ansible >= 2.13
- Python >= 3.8

## Installation

Install the collection from a local archive:

```bash
ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz
