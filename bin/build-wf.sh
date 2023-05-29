#!/bin/bash

dir_here="$( cd "$(dirname "$0")" ; pwd -P )"
dir_project_root="$(dirname "${dir_here}")"

bin_pip="pip3"


source "${dir_here}/settings.sh"

rm -r "${dir_workflow}/libs"

${bin_pip} install "${dir_project_root}" --target="${dir_workflow}/libs"

cp -R "${dir_project_root}/${package_name}" "${dir_workflow}"

