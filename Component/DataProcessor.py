from GenericPackage.PyQt6.Shortcut import ShortcutManager
from PyQt6.QtWidgets import QApplication
from .Data import*
from .Paths import*
from traceback import print_exception
__all__ = [
    "SoftwareSettingManager",
    "GlobalDataManager",
    "GetGlobalDataManager",
]
__app=None
class SoftwareSettingManager():
    def __init__(self) -> None:
        self._SoftwareSetting=SoftwareSetting()
    def Load(self):
        try:                    self._SoftwareSetting.Load(SoftwareSettingPath)
        except Exception as e:  print_exception(e)
    def SetSetting(self,setting:SoftwareSetting)->None:
        """
        ソフトウェアの設定を更新する。
        """
        if not isinstance(setting,SoftwareSetting):
            raise TypeError(f"settingは{SoftwareSetting.__name__}型である必要があります。受け取った型:{type(setting).__name__}")
        self._SoftwareSetting=setting
    def Save(self)->None:
        self._SoftwareSetting.Save(SoftwareSettingPath)
class GlobalDataManager():
    def __init__(self) -> None:
        self._SoftwareSetting=SoftwareSetting()
        self._ShortcutManager=ShortcutManager(QApplication.instance())
        self._GlobalFunctions=dict()
        self.Load()
    def Load(self):
        try:                    self._SoftwareSetting.Load(SoftwareSettingPath)
        except Exception as e:  print_exception(e)
    @property
    def SoftwareSetting(self)->SoftwareSetting:
        return self._SoftwareSetting
    @property
    def ShortcutManager(self)->ShortcutManager:
        return self._ShortcutManager
    def SaveAll(self)->None:
        self._SoftwareSetting.Save(SoftwareSettingPath)
    def GetGlobalFunction(self,name:str)->Callable:
        """
        グローバル関数を取得する。
        """
        if name not in self._GlobalFunctions:
            raise KeyError(f"{name}は登録されていません。")
        return self._GlobalFunctions[name]
    def GetGlobalFunctionLazy(self, name: str) -> Callable:
        """
        グローバル関数を遅延評価で取得する。
        このメソッド実行時点で未登録の場合でも関数呼び出し時に登録されていれば実行可能。
        """
        def factory(*args,**kwargs):
            func=self.GetGlobalFunction(name)
            if func is None:
                raise KeyError(f"{name}は登録されていません。")
            func(*args,**kwargs)
        return factory
    def AddGlobalFunction(self,name:str,function:Callable)->None:
        """
        グローバル関数を追加する。
        """
        if not callable(function):
            raise TypeError("functionは呼び出し可能なオブジェクトである必要があります。")
        if name in self._GlobalFunctions:
            raise KeyError(f"{name}はすでに登録されています。")
        self._GlobalFunctions[name]=function
def GetGlobalDataManager()->GlobalDataManager:
    global __app
    if __app is None:
        __app=QApplication.instance()
        if __app is None:
            raise RuntimeError("QApplicationのインスタンスが存在しません。")
    return __app.GlobalData