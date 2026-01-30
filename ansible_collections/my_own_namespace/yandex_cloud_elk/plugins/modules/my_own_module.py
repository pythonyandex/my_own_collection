#!/usr/bin/python3

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
from email.policy import default
from pickle import FALSE
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Create or update a text file on the target host

version_added: "1.0.0"

description:
  - This module creates a text file at the specified path on the target host.
  - If the file already exists and the content differs, the file will be updated.
  - The module is idempotent and supports check mode.

options:
  path:
    description:
      - Absolute path to the file that should be created or updated.
    required: true
    type: str
  content:
    description:
      - Content that will be written to the file.
    required: true
    type: str

author:
  - Ruslan Mamedov
'''


EXAMPLES = r'''
- name: Create file using custom module
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/file.txt
    content: "Homework"
'''


RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
original_message:
    description: The original name param that was passed in.
    type: str
    returned: always
    sample: 'Homework'
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'File created'
'''


from ansible.module_utils.basic import AnsibleModule
import os.path


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=False, default = "homework")
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        if not os.path.exists(module.params['path']):
            result['changed'] = True
        module.exit_json(**result)

    if not os.path.exists(module.params['path']):
        with open(module.params['path'], 'w') as f:
            f.write(module.params['content'])
        result['changed'] = True
        result['original_message'] = 'File created'
        result['message'] = 'File created'
    else:
        result['original_message'] = 'File is already exists'
        result['message'] = 'File is already exists'

    module.exit_json(**result)

def main():
    run_module()


if __name__ == '__main__':
    main()
