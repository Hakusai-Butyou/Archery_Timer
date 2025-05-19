print("起動中...",end="",flush=True)
from GenericPackage.PyQt6.advancedWidget import*
from PyQt6.QtWidgets import*
from Component.Paths import*
from sys import argv
setCurrentDirectory(__file__)
if __name__=="__main__":
    global app
    app=QApplication(argv)
    setattr(app,"GlobalData",None)
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
from Component.DataProcessor import*
from Component.Data import*
from Component.Screen import *
SplashUpdate("オブジェクトを読み込む中")
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ScreenManager=ScreenManager(self,ScreenList)
        self.SetWindowSize()
        GetGlobalDataManager().AddGlobalFunction("close",self.close)
    def SetWindowSize(self):
        geometry=GetGlobalDataManager().SoftwareSetting.get_setting_value("LastWindowGeometry")
        if geometry is None:
            self.resize(800,500)
        else:
            self.setGeometry(geometry)
        if GetGlobalDataManager().SoftwareSetting.get_setting_value("IsWindowMaximum"):
            self.showMaximized()
    def saveGeometry(self):
        """
        ウィンドウの位置を保存する。
        """
        if self.windowState()==Qt.WindowState.WindowMaximized:
            GetGlobalDataManager().SoftwareSetting.set_setting_value("IsWindowMaximum",True)
        else:
            GetGlobalDataManager().SoftwareSetting.set_setting_value("IsWindowMaximum",False)
            GetGlobalDataManager().SoftwareSetting.set_setting_value("LastWindowGeometry",self.geometry())
    def resizeEvent(self,event:QResizeEvent)->None:
        self.ScreenManager.setGeometry(0,0,event.size().width(),event.size().height())
    def closeEvent(self, event:QCloseEvent) -> None:
        self.saveGeometry()
    def close(self)->None:
        def quit():
            self.saveGeometry()
            self.hide()
            self.deleteLater()
            app.quit()
        ConfirmDialog(title="確認",message="終了しますか？",acceptButtonLabel="はい",rejectButtonLabel="いいえ",acceptCommand=quit,focus_accept=False).exec()
SplashUpdate("UI初期化中")
if __name__=="__main__":
    app.GlobalData=GlobalDataManager()
    main=Main()
    SplashUpdate("完了")
    main.show()
    Splash.hide()
    Splash.deleteLater()
    app.exec()
    print("データを保存しています。")
    GetGlobalDataManager().SaveAll()
    print("ソフトウェアは正常に終了しました。")