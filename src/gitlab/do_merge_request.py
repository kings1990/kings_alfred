import sys
import os
import time
sys.path.append(os.path.join(os.path.dirname(__file__), "../libs"))

import gitlab


# GitLab API相关信息
gitlab_url = sys.argv[1]
access_token = sys.argv[2]
project_id = sys.argv[3]
source_branch = sys.argv[4]
target_branch = sys.argv[5]

gl = gitlab.Gitlab(url=gitlab_url, private_token=access_token)
project = gl.projects.get(project_id)


mr = project.mergerequests.create({'source_branch': source_branch,
                                   'target_branch': target_branch,
                                   'title': 'merge by tool',
                                   })
time.sleep(2)

merge_id = mr.get_id()
mr = project.mergerequests.get(merge_id)
if mr.merge_status == 'can_be_merged':
    print("begin merge from [%s] to [%s]" % (source_branch, target_branch))
    mr.merge()
    print("merge success")
