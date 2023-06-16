#! /usr/bin/env python3
import requests
import zipfile
import io
import sys

OWNER     = ""
REPO      = ""
GH_TOKEN  = ""
CERT_PATH = ""

def get_latest_artifact():
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/artifacts"
    r = requests.get(url, headers={"Accept": "application/vnd.github+json",
                                   "Authorization":f"token {GH_TOKEN}",
                                   "X-GitHub-Api-Version": "2022-11-28"})
    r.raise_for_status()
    artifacts = r.json()["artifacts"]
    latest = artifacts[0]
    return latest

def get_cert(artifact):
    url = artifact["archive_download_url"]
    r = requests.get(url, headers={"Accept": "application/vnd.github+json",
                                   "Authorization":f"token {GH_TOKEN}",
                                   "X-GitHub-Api-Version": "2022-11-28"})
    r.raise_for_status()
    zip_file = zipfile.ZipFile(io.BytesIO(r.content))
    return zip_file.extractall(CERT_PATH)
    
def main():
    artifact = get_latest_artifact()
    if artifact:
        get_cert(artifact)
    else:
        print("No artifact found")

if __name__ == "__main__":
    if OWNER == '' or REPO == '' or GH_TOKEN == '' or CERT_PATH == '':
        if len(sys.argv) < 5:
            print(f"Usage: {sys.argv[0]} OWNER REPO GH_TOKEN CERT_PATH")
            sys.exit(1)
        else:
            OWNER     = sys.argv[1]
            REPO      = sys.argv[2]
            GH_TOKEN  = sys.argv[3]
            CERT_PATH = sys.argv[4]
    main()