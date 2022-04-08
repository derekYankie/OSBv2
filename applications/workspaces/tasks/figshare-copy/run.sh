#!/bin/bash

set -e

# remove the pvc from the path (if it has one)
# and append the folder
export download_path=`echo $shared_directory | cut -d ":" -f 2`/"${folder}"

mkdir -p "${download_path}"
cd "${download_path}"

# if a file url is passed
if grep -E "https://" "${url}"
then
    echo "${url}" > filelist
else
    # if the article id is passed, download all files
    curl -X GET "https://api.figshare.com/v2/articles/${url}/files" | tr "}" "\n" | grep -Eo "https://ndownloader.figshare.com/files/[[:digit:]]+" > filelist
fi

echo Figshare copy "${url}" to "${download_path}"
aria2c -i filelist -j 5 -x 10 --allow-overwrite "true"

# delete the file list
rm filelist -f

# fix permissions
chown -R 1000:1000 "${download_path}"
