import os
import re
import shutil
import sys

import requests


def checkFolder(outFile):
    if not os.path.exists(outFile):
        os.makedirs(outFile)


def fileExists(file):
    return os.path.exists(file)


def dirExists(dir):
    return os.path.isdir(dir)


def formatAmount(amount):
    if amount < 1024:
        return str(round(amount, 2)) + " B"
    elif amount < 1024 * 1024:
        return str(round(amount / 1024, 2)) + " KB"
    elif amount < 1024 * 1024 * 1024:
        return str(round(amount / (1024 * 1024), 2)) + " MB"
    else:
        return str(round(amount / (1024 * 1024 * 1024), 2)) + " GB"


def downloadFile(url, outputFile):
    if os.path.exists(outputFile):
        print("File already exists %s" % outputFile)
        return
    checkFolder(os.path.dirname(outputFile))
    with open(outputFile, "wb") as f:
        print("Downloading %s" % outputFile)
        response = requests.get(url, stream=True)
        total_length = response.headers.get("content-length")

        if total_length is None:  # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write(
                    "\r[%s%s] %s/%s %s"
                    % (
                        "=" * done,
                        " " * (50 - done),
                        formatAmount(dl),
                        formatAmount(total_length),
                        " " * 5,
                    )
                )
                sys.stdout.flush()
            print("")


def copyFile(source, destination):
    if os.path.isfile(source):
        shutil.copy2(source, destination)


def extractTar(archivePath, outPath):
    print(f"Extracting {archivePath} to {outPath}")
    import tarfile

    checkFolder(outPath)
    with tarfile.open(archivePath, "r") as tar_ref:
        tar_ref.extractall(outPath)
    print(f"Extracted {archivePath} to {outPath}")


def extractZip(archivePath, outPath):
    print(f"Extracting {archivePath} to {outPath}")
    import zipfile

    checkFolder(outPath)
    with zipfile.ZipFile(archivePath, "r") as zip_ref:
        zip_ref.extractall(outPath)
    print(f"Extracted {archivePath} to {outPath}")


def extract(archivePath, outPath):
    if archivePath.endswith(".zip"):
        extractZip(archivePath, outPath)
    elif archivePath.endswith((".tar.gz", ".tgz", ".tar.bz2", ".tar.xz")):
        extractTar(archivePath, outPath)
    else:
        raise ValueError(f"Unknown archive type: {archivePath}")


def moveContent(fromDir, toDir):
    print(fromDir)
    print(toDir)
    for item in os.listdir(fromDir):
        s = os.path.join(fromDir, item)
        d = os.path.join(toDir, item)
        if os.path.isdir(s):
            if not os.path.exists(d):
                shutil.move(s, d)
        else:
            if not os.path.exists(d):
                shutil.move(s, d)


def findFolder(searchDir, key):
    for dir in os.listdir(searchDir):
        if re.match(key, dir):
            return dir


def get_os_name():
    system = sys.platform.system().lower()
    if system == "windows":
        return "windows"
    elif system == "linux":
        return "linux"
    elif system == "darwin":
        return "macosx"
    else:
        return "unknown"
