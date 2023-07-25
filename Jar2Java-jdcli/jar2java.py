import os
import sys
import subprocess

def toJava(sourcePath, destPath):

    global jdCliPath
    print(sourcePath)
    try:
        proc = subprocess.Popen([jdCliPath, sourcePath, "-od", destPath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc.communicate(timeout=30)
    except subprocess.TimeoutExpired:

        print("Timeout", sourcePath)
        timeOutPath.append(sourcePath)
        proc.kill()
        return None


def decompile(targetPath):

    for root, dirs, files in os.walk(targetPath):

        for file in files:

            if(file.endswith(".jar")):

                sourcePath = os.path.join(root,file).replace("\\","/")
                destPath = os.path.join(root,file).replace("\\","/")[:-4]
                toJava(sourcePath, destPath)
                #decompile(destPath)

            if(file.endswith(".class")):

                sourcePath = os.path.join(root, file).replace("\\","/")
                destPath = os.path.join(root).replace("\\","/")
                toJava(sourcePath, destPath)

if __name__ == '__main__':

    timeOutPath = []
    jdCliPath = "jd-cli.bat"
    targetPath = "/"
    decompile(targetPath)
    print(timeOutPath)
