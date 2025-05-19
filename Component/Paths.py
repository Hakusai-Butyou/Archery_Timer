from os import chdir,mkdir,curdir
from os.path import dirname,abspath,exists
def makeDirectory(path:str)->str:
    if not exists(path):
        mkdir(path)
    return path
def makeFile(path:str)->str:
    if not exists(path):
        with open(path,"w") as f:
            f.write("")
    return path
def setCurrentDirectory(filePath:str)->None:
    """
    カレントディレクトリをスクリプトのある場所に変更する。
    """
    chdir(dirname(abspath(filePath)))

setCurrentDirectory(__file__)
chdir("../")

HomeDir=abspath(curdir).replace("\\","/")
SettingDirectory=makeDirectory(f"{HomeDir}/settings")
SoftwareSettingPath=makeFile(f"{SettingDirectory}/SoftwareSetting.ini")
UUIDSettingPath=makeFile(f"{SettingDirectory}/UUIDSetting.ini")