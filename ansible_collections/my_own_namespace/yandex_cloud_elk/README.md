
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
ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz```markdown
```
### Шаг 4 & 6
![Здесь показан запуск и идемпотентность](https://github.com/pythonyandex/my_own_collection/blob/main/Ansible0806_step4_6.png)
### Шаг 15
![ansible-galaxy collection install](https://github.com/pythonyandex/my_own_collection/blob/main/Ansible0806_step15.png)

### Шаг 16
![Наличие модуля](https://github.com/pythonyandex/my_own_collection/blob/main/Ansible0806_step16.png)
