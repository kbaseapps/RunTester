from installed_clients.specialClient import special as special
import json
import os
import shutil


def wdl(callback_url, token):
    sr = special(callback_url, token=token)
    src = '/kb/module/workflow.wdl'
    wdl_file = 'workflow.wdl'
    shutil.copy(src, 'work/tmp/' + wdl_file)
    input_file = 'inputs.json'
    ins = {'name': 'KBase'}
    with open('/kb/module/work/tmp/' + input_file, 'w') as f:
        f.write(json.dumps(ins))

    p = {
        'workflow': wdl_file,
        'inputs': input_file
    }
    
    res = sr.wdl(p)
    print('wdl: '+str(res))
