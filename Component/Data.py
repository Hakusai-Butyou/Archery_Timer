from typing import *
from dataclasses import dataclass
from PyQt6.QtCore import QRect
from GenericPackage.IO.FileIO import SaveAndLoad_Binary
from typeguard import check_type
class Point():
    """
    アーチェリー用の得点クラス
    """
    def __init__(self, point:Union[int,"Point"]):
        if not isinstance(point,(int,Point)):
            raise TypeError(f"pointはint型またはPoint型で指定してください。指定された値:{point} 型:{type(point).__name__}")
        if isinstance(point,Point):
            self.point:int=point.point
            return
        if 0<=point<=11:
            self.point:int=point
        else:
            raise ValueError(f"pointは0から11の範囲で指定してください。指定された値:{point}")
    def text(self)->str:
        match self.point:
            case 0: return "M"
            case 11: return "X"
            case _: return str(self.point)
    def __int__(self)->int:
        return self.point
    def __str__(self)->str:
        return self.text()
class PointList(list):
    def __init__(self, pointList:Optional[list[Union[Point]]] = None):
        if pointList is None:
            super().__init__()
            return
        def mapping(point:Union[Point,int])->Point:
            if isinstance(point,Point):
                return point
            elif isinstance(point,int):
                return Point(point)
            else:
                raise TypeError(f"pointはint型またはPoint型で指定してください。指定された値:{point} 型:{type(point).__name__}")
        pointList=list(map(mapping,pointList))
        super().__init__(pointList)
    def ToStringList(self)->list[str]:
        return [str(point) for point in self]
    @override
    def append(self, object: Union[Point,int]) -> None:
        if isinstance(object,int):
            super().append(Point(object))
        elif isinstance(object,Point):
            super().append(object)
        else:
            raise TypeError(f"pointはint型またはPoint型で指定してください。指定された値:{object} 型:{type(object).__name__}")
    def __setitem__(self, index: int, object: Union[Point,int]) -> None:
        if isinstance(object,int):
            super().__setitem__(index,Point(object))
        elif isinstance(object,Point):
            super().__setitem__(index,object)
        else:
            raise TypeError(f"pointはint型またはPoint型で指定してください。指定された値:{object} 型:{type(object).__name__}")
@dataclass(slots=True)
class SoftwareSetting(SaveAndLoad_Binary):
    """
    ソフトウェアの設定を保存するクラス
    """
    LastWindowGeometry:Optional[QRect]=None
    IsWindowMaximum:bool=False
    def _init_value(self) -> None:
        LastWindowGeometry=None
        IsWindowMaximum=False
    def set_setting_value(self,settingName:str,value:Any)->None:
        """
        設定の値を更新する。
        """
        if not hasattr(self,settingName):
            raise AttributeError(f"{self.__class__.__name__}に{settingName}という属性は存在しません。")
        if not isinstance(value,self.__annotations__[settingName]):
            if not check_type(value,self.__annotations__[settingName]):
                raise TypeError(f"{self.__class__.__name__}の{settingName}の型が一致しません。型:{type(value).__name__} 型:{self.__annotations__[settingName].__name__}")
        return setattr(self,settingName,value)
    def get_setting_value(self,settingName:str)->Any:
        """
        設定の値を取得する。
        """
        if not hasattr(self,settingName):
            raise AttributeError(f"{self.__class__.__name__}に{settingName}という属性は存在しません。")
        return getattr(self,settingName)