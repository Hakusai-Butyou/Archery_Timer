from PyQt6.QtWidgets import*
from PyQt6.QtCore import*
from PyQt6.QtGui import*
from GenericPackage.PyQt6.generalFunction import*
from GenericPackage.PyQt6.advancedWidget import *
from .DataProcessor import *
from abc import abstractmethod

class AbstractScreen(Screen):
    """
    スクリーンの基底クラス
    """
    def __init__(self, parent:ScreenManager):
        super().__init__(parent)
    def activate_shortcut(self):
        GetGlobalDataManager().ShortcutManager.DisableAll()
        GetGlobalDataManager().ShortcutManager.SetEnable(self.__class__.__name__)
    @abstractmethod
    def initialize_widget(self):
        """
        UIを初期化する。
        """
        ...
    @abstractmethod
    def positioning_widget(self):
        """
        UIの位置を決定する。
        """
        ...
    @abstractmethod
    def set_shortcut_key(self):
        """
        ショートカットキーを設定する。
        """
        ...
class StartScreen(AbstractScreen):
    def __init__(self,parent:QWidget)->None:
        super().__init__(parent)
        self.initialize_widget()
        self.positioning_widget()
        self.set_shortcut_key()
    def initialize_widget(self):
        self.setting_button=AdvancedPushButton(self,text="設定",fontSize=30,command=lambda:self.ScreenManager.changeScreenByScreenName("SettingScreen"))
    def positioning_widget(self):
        PO=PlacementObject(self.size())
        self.setting_button.move(PO.CentreX(self.setting_button),PO.BottomY(self.setting_button,-30))
    def recvArg(self,screenID_From,arg:tuple):
        self.activate_shortcut()
    def set_shortcut_key(self):
        GetGlobalDataManager().ShortcutManager.Add(self.__class__.__name__,Qt.Key.Key_I,lambda:self.ScreenManager.changeScreenByScreenName("SettingScreen"))
        GetGlobalDataManager().ShortcutManager.Add(self.__class__.__name__,Qt.Key.Key_Escape,GetGlobalDataManager().GetGlobalFunctionLazy("close"),exclusiveAll=True)
    def resizeEvent(self,event:QResizeEvent)->None:
        self.positioning_widget()
class SettingScreen(AbstractScreen):
    def __init__(self,parent:QWidget)->None:
        super().__init__(parent)
        self.initialize_widget()
        self.positioning_widget()
        self.set_shortcut_key()
    def initialize_widget(self):
        self.back_button=AdvancedPushButton(self,text="戻る",fontSize=30,command=lambda:self.ScreenManager.changeScreenByScreenName("StartScreen"))
        self.round_setting_combobox=AdvancedComboBox(self,Item={})
    def positioning_widget(self):
        PO=PlacementObject(self.size())
        self.back_button.move(PO.LeftX(),PO.UpperY())
    def recvArg(self,screenID_From,arg:tuple):
        self.activate_shortcut()
    def set_shortcut_key(self):
        add_shortcut=lambda key,command:GetGlobalDataManager().ShortcutManager.Add(self.__class__.__name__,key,command)
        add_shortcut(Qt.Key.Key_Escape,lambda:self.ScreenManager.changeScreenByScreenName("StartScreen"))
    def resizeEvent(self,event:QResizeEvent)->None:
        self.positioning_widget()

ScreenList=[StartScreen,SettingScreen]