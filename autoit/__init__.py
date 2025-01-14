# -*- coding: utf-8 -*-
__author__ = 'Jace Xu'
__version__ = "0.6.5"

from .autoit import options, properties, commands
from .autoit import AutoItError

from .autoit import Error
from .autoit import AutoItSetOption
from .autoit import ClipGet
from .autoit import ClipPut
from .autoit import IsAdmin
from .autoit import DriveMapAdd
from .autoit import DriveMapDel
from .autoit import DriveMapGet
from .autoit import MouseClick
from .autoit import MouseClickDrag
from .autoit import MouseDown
from .autoit import MouseGetCursor
from .autoit import MouseGetPos
from .autoit import MouseMove
from .autoit import MouseUp
from .autoit import MouseWheel
from .autoit import Opt
from .autoit import PixelChecksum
from .autoit import PixelGetColor
from .autoit import PixelSearch
from .autoit import Send
from .autoit import Tooltip

from .process import Run
from .process import RunWait
from .process import ProcessClose
from .process import ProcessExists
from .process import ProcessSetPriority
from .process import ProcessWait
from .process import ProcessWaitClose
from .process import RunAs
from .process import RunAsWait
from .process import Shutdown

from .win import WinActivate
from .win import WinActivateByHandle
from .win import WinActive
from .win import WinActiveByHandle
from .win import WinClose
from .win import WinCloseByHandle
from .win import WinExists
from .win import WinExistsByHandle
from .win import WinGetCaretPos
from .win import WinGetClassList
from .win import WinGetClassListByHandle
from .win import WinGetClientSize
from .win import WinGetClientSizeByHandle
from .win import WinGetHandle
from .win import WinGetHandleAsText
from .win import WinGetPos
from .win import WinGetPosByHandle
from .win import WinGetProcess
from .win import WinGetProcessByHandle
from .win import WinGetState
from .win import WinGetStateByHandle
from .win import WinGetText
from .win import WinGetTextByHandle
from .win import WinGetTitle
from .win import WinGetTitleByHandle
from .win import WinKill
from .win import WinKillByHandle
from .win import WinMenuSelectItem
from .win import WinMenuSelectItemByHandle
from .win import WinMinimizeAll
from .win import WinMinimizeAllUndo
from .win import WinMove
from .win import WinMoveByHandle
from .win import WinSetOnTop
from .win import WinSetOnTopByHandle
from .win import WinSetState
from .win import WinSetStateByHandle
from .win import WinSetTitle
from .win import WinSetTitleByHandle
from .win import WinSetTrans
from .win import WinSetTransByHandle
from .win import WinWait
from .win import WinWaitByHandle
from .win import WinWaitActive
from .win import WinWaitActiveByHandle
from .win import WinWaitClose
from .win import WinWaitCloseByHandle
from .win import WinWaitNotActive
from .win import WinWaitNotActiveByHandle

from .control import ControlClick
from .control import ControlClickByHandle
from .control import ControlCommand
from .control import ControlCommandByHandle
from .control import ControlListView
from .control import ControlListViewByHandle
from .control import ControlDisable
from .control import ControlDisableByHandle
from .control import ControlEnable
from .control import ControlEnableByHandle
from .control import ControlFocus
from .control import ControlFocusByHandle
from .control import ControlGetFocus
from .control import ControlGetFocusByHandle
from .control import ControlGetHandle
from .control import ControlGetHandleAsText
from .control import ControlGetPos
from .control import ControlGetPosByHandle
from .control import ControlGetText
from .control import ControlGetTextByHandle
from .control import ControlHide
from .control import ControlHideByHandle
from .control import ControlMove
from .control import ControlMoveByHandle
from .control import ControlSend
from .control import ControlSendByHandle
from .control import ControlSetText
from .control import ControlSetTextByHandle
from .control import ControlShow
from .control import ControlShowByHandle
from .control import ControlTreeView
from .control import ControlTreeViewByHandle
from .control import StatusbarGetText
from .control import StatusbarGetTextByHandle