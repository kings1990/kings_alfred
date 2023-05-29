#!/bin/bash
#
# Project specific settings value

if [ -n "${BASH_SOURCE}" ]
then
    dir_bin="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
else
    dir_bin="$( cd "$(dirname "$0")" ; pwd -P )"
fi
dir_project_root="$(dirname "${dir_bin}")"

package_name="src/translate"

# 替换workflow工作id
dir_workflow_root="/Users/wilson/Library/Application Support/Alfred/Alfred.alfredpreferences/workflows/"
dir_workflow_id="user.workflow.FC347E2D-73D6-47B5-AA8F-BCAA53BFB46C"
dir_workflow="${dir_workflow_root}${dir_workflow_id}"

