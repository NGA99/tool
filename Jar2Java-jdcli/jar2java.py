import os
import sys
import subprocess

def toJava(sourcePath, destPath):

    global jdCliPath
    print(sourcePath)
    subprocess.call([jdCliPath, sourcePath, "-od", destPath])

def decompile(targetPath):

    for root, dirs, files in os.walk(targetPath):

        for file in files:

            if(file.endswith(".jar")):

                sourcePath = os.path.join(root,file).replace("\\","/")
                destPath = os.path.join(root,file).replace("\\","/")[:-4]
                toJava(sourcePath, destPath)
                decompile(destPath)

            if(file.endswith(".class")):

                sourcePath = os.path.join(root, file).replace("\\","/")
                destPath = os.path.join(root).replace("\\","/")
                toJava(sourcePath, destPath)

if __name__ == '__main__':

    jdCliPath = "jd-cli.bat"
    targetPath = sys.argv[1]
    decompile(targetPath)
