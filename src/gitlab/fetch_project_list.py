import sys
import os
import json
sys.path.append(os.path.join(os.path.dirname(__file__), "../libs"))

import gitlab

gitlab_url = sys.argv[1]
access_token = sys.argv[2]

project_keywords = ''
if len(sys.argv) == 4:
    project_keywords = sys.argv[3]

# 获取项目列表
gl = gitlab.Gitlab(url=gitlab_url, private_token=access_token)
projects = gl.projects.list(search=project_keywords, owned=True)

data = {"items": []}
for project in projects:
    item = {
        "title": project.name,
        "arg": project.id
    }
    data["items"].append(item)

print(json.dumps(data, indent=2, ensure_ascii=False))
