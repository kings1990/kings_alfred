import sys
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
merge_id = mr.get_id()

