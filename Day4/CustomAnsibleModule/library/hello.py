#!/usr/bin/python

DOCUMENTATION = '''
---
module: hello 
version_added: just now 
short_description: Echoes whatever message you supply with some junk message 
description:
   - Trivial hello custom module.
options:
  msg:
    description:
      - Your custom message as string 
    type: str
'''

from ansible.module_utils.basic import AnsibleModule

def sayHello(message):
    return "Message echoed from Custom Ansible module @@@" + message 

def main():
    module = AnsibleModule(
        argument_spec=dict(
            msg=dict(type='str')
        )
    )

    msg = module.params['msg']

    message = sayHello( msg )

    result = dict(
        response=message,
    )

    #module.exit_json(**result,changed=False)
    module.fail_json(msg="Fatal error occurred")
   


if __name__ == '__main__':
    main()

