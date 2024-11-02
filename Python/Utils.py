import requests
import os
import sys
import re
import shutil

def checkFolder(outFile):
    if not os.path.exists(outFile):
        os.makedirs(outFile)


def formatAmount(amount):
    if amount < 1024:
        return str(round(amount,2)) + " B"
    elif amount < 1024*1024:
        return str(round(amount/1024,2)) + " KB"
    elif amount < 1024*1024*1024:
        return str(round(amount/(1024*1024),2)) + " MB"
    else:
        return str(round(amount/(1024*1024*1024),2)) + " GB"


def downloadFile(url,outputFile):
    if os.path.exists(outputFile):
        print("File already exists %s" % outputFile)
        return
    checkFolder(os.path.dirname(outputFile))
    with open(outputFile, "wb") as f:
        print("Downloading %s" % outputFile)
        response = requests.get(url, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None: # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s] %s/%s %s" % ('=' * done, ' ' * (50-done),formatAmount(dl),formatAmount(total_length),' '*5) )    
                sys.stdout.flush()
            print("")
            
def extractTar(archivePath,outPath):
    import tarfile        
    checkFolder(outPath)
    with tarfile.open(archivePath, 'r') as tar_ref:
        tar_ref.extractall(outPath)

def extractZip(archivePath,outPath):
    import zipfile
    checkFolder(outPath)
    with zipfile.ZipFile(archivePath, 'r') as zip_ref:
        zip_ref.extractall(outPath)  
            
def extract(archivePath,outPath):
    if os.name == "posix":
        extractTar(archivePath,outPath)
    if os.name == "nt":
        extractZip(archivePath,outPath)
        
def moveContent(fromDir, toDir):
    print(fromDir)
    print(toDir)
    for item in os.listdir(fromDir):
        s = os.path.join(fromDir, item)
        d = os.path.join(toDir, item)
        if os.path.isdir(s):
            if not os.path.exists(d):
                shutil.move(s,d)
        else:
            if not os.path.exists(d):
                shutil.move(s,d)
    


def findFolder(searchDir,key):
   for dir in os.listdir(searchDir):
       if re.match(key,dir):
           return dir