import os
import subprocess

def jdCli(jarPath, savePath):

    print(jarPath)
    subprocess.call(["jd-cli.bat", jarPath, "-od", savePath])

def classToJava(dirName):

    for root, dirs, files in os.walk(dirName):

        for file in files:

            if(file.endswith(".jar")):

                jarPath = "{}/{}".format(root,file.replace("\\","//"))
                savePath = "{}/{}".format(root,file.replace("\\","//")[:-4])
                jdCli(jarPath, savePath)

if __name__ == '__main__':

    dirName = "C:/NGA/Study/CMS/Confluence8.0/"
    classToJava(dirName)