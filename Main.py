print("起動中...",end="",flush=True)
from GenericPackage.PyQt6.advancedWidget import*
from PyQt6.QtWidgets import*
from Component.DataProcessor import*
from Component.Data import*
from Component.Paths import*
from sys import argv
setCurrentDirectory(__file__)
if __name__=="__main__":
    app=QApplication(argv)
    app.globalData=GlobalDataManager()
    Splash=SimpleSplashScreen()
    SplashUpdate=Splash.GetStatusUpdateFunction(app)
else:
    SplashUpdate=lambda x1,x2=None:None
SplashUpdate("モジュールを読み込み中")
print("\33[2K\r",end="",flush=True)
SplashUpdate("モジュールを読み込み中","PyQt6")
from PyQt6.QtCore import*
from PyQt6.QtGui import*
SplashUpdate("モジュールを読み込み中","Component")
SplashUpdate("オブジェクトを読み込む中")
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
    def closeEvent(self, event:QCloseEvent) -> None:
        GetGlobalDataManager().SoftwareSetting
SplashUpdate("UI初期化中")
if __name__=="__main__":
    main=Main()
    SplashUpdate("完了")
    main.show()
    Splash.hide()
    Splash.deleteLater()
    app.exec()
    app.globalData.SaveAll()