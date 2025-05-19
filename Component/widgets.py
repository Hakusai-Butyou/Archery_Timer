from PyQt6.QtWidgets import QFrame
from GenericPackage.PyQt6.advancedWidget import AdvancedPushButton
from GenericPackage.PyQt6.generalFunction import*
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QResizeEvent
from .Data import Point
class Key(AdvancedPushButton):
    clicked=pyqtSignal(Point)
    def __init__(self, parent:"PointKeyboard",point:int):
        self.point=Point(point)
        super().__init__(parent,text=self.point.text())
        super().clicked.connect(self.__clicked)
    def __clicked(self):
        self.clicked.emit(self.point)
class PointKeyboard(QFrame):
    entered=pyqtSignal(Point)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.Keys=[Key(i) for i in range(11)]
    def SetWidgetPosition(self,ratio:float):
        if ratio>=11:
            for i in range(11):
                self.Keys[i].setGeometry(QRect(i*100,0,100,100))
        elif ratio>=6:pass
        size=self.size()
    def resizeEvent(self, event:QResizeEvent):
        w,h=getSizeFromResizeEvent(event)
        ratio=w/h
        self.SetWidgetPosition(ratio)