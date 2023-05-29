import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../libs"))

import gitlab

gitlab_url = sys.argv[1]
access_token = sys.argv[2]
project_id = sys.argv[3]
ref = sys.argv[4]
branch_name = sys.argv[5]

gl = gitlab.Gitlab(url=gitlab_url, private_token=access_token)
project = gl.projects.get(project_id)

branch = project.branches.create({'branch': branch_name, 'ref': ref})
