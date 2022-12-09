import os
import sys
import subprocess

def jdCli(jarPath, savePath):

    global jdCliPath
    print(jarPath)
    subprocess.call([jdCliPath, jarPath, "-od", savePath])

def classToJava(dirName):

    for root, dirs, files in os.walk(dirName):

        for file in files:

            if(file.endswith(".jar")):

                jarPath = "{}/{}".format(root,file.replace("\\","//"))
                savePath = "{}/{}".format(root,file.replace("\\","//")[:-4])
                jdCli(jarPath, savePath)

if __name__ == '__main__':

    jdCliPath = "./jd-cli.bat"
    dirName = sys.argv[1]
    classToJava(dirName)
