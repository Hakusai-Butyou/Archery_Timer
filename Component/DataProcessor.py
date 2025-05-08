from GenericPackage.PyQt6.Shortcut import ShortcutManager
from PyQt6.QtWidgets import QApplication
from Data import*
from Paths import*
from traceback import print_exception
class SoftwareSettingManager():
    def __init__(self) -> None:
        self._SoftwareSetting=SoftWereSetting()
    def Load(self):
        try:                    self._SoftwareSetting.Load(SoftwareSettingPath)
        except Exception as e:  print_exception(e)
    def SetSetting(self,setting:SoftWereSetting)->None:
        """
        ソフトウェアの設定を更新する。
        """
        if not isinstance(setting,SoftWereSetting):
            raise TypeError(f"settingは{SoftWereSetting.__name__}型である必要があります。受け取った型:{type(setting).__name__}")
        self._SoftwareSetting=setting
    def Save(self)->None:
        self._SoftwareSetting.Save(SoftwareSettingPath)
class GlobalDataManager():
    def __init__(self) -> None:
        self._SoftwareSettingManager=SoftWereSetting()
        self._ShortcutManager=ShortcutManager(QApplication.instance())
    def Load(self):
        try:                    self._SoftwareSetting.Load(SoftwareSettingPath)
        except Exception as e:  print_exception(e)
    @property
    def SoftwareSetting(self)->SoftWereSetting:
        return self._SoftwareSetting
    @property
    def ShortcutManager(self)->ShortcutManager:
        return self._ShortcutManager
    def SaveAll(self)->None:
        self._SoftwareSetting.Save(SoftwareSettingPath)
def GetGlobalDataManager()->GlobalDataManager:
    return QApplication.instance().GlobalDataManager