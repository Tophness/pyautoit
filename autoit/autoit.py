# -*- coding: utf-8 -*-

__author__ = 'Jace Xu'

import os
import platform
from ctypes.wintypes import *
from functools import wraps
import sys
if sys.version_info[0] == 3:
    from functools import reduce
else:
    import ctypes

dll = "AutoItX3.dll"
bit, _ = platform.architecture()

if bit == "64bit":
    # if 64bit version of python within 64bit version of Windows,
    # load AutoItX3_x64.dll
    dll = "AutoItX3_x64.dll"

dll_path = os.path.join(os.path.dirname(__file__), "lib", dll)

if not os.path.exists(dll_path):
    raise IOError("Cannot load AutoItX from path: %s" % dll_path)

AUTO_IT = ctypes.windll.LoadLibrary(dll_path)


class AutoItError(Exception):
    pass


def Error():
    return AUTO_IT.AU3_error()


class AutoItAPI(object):

    def __init__(self):
        self.msg = {}

    @staticmethod
    def _has_error():
        return True if Error() == 1 else False

    @staticmethod
    def _has_unexpected_ret(ret, unexpected):
        if ret in unexpected:
            return True
        return False

    @staticmethod
    def _parser(x, y):
        if x["num"] >= y:
            x["flags"].append(y)
            x["num"] -= y
        return x

    def check(self, mark=0, err_msg="", **kwds):
        """
        :param mark:
            0 - do not need check return value or Error()
            1 - check Error()
            2 - check return value
        """
        unexpected_ret = kwds.get("unexpected_ret", (0,))

                      

        def _check(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                ret = fn(*args, **kwargs)

                flags = reduce(
                    self._parser, [dict(num=mark, flags=[]), 2, 1])["flags"]

                if 1 in flags:
                    if self._has_error():
                        raise AutoItError(err_msg)

                if 2 in flags:
                    if self._has_unexpected_ret(ret, unexpected_ret):
                        raise AutoItError(err_msg)

                return ret
            return wrapper
        return _check


api = AutoItAPI()


@api.check()
def AutoItSetOption(option, param):
    """
    Changes the operation of various AutoIt functions/parameters
    :param option: The option to change
    :param param: The parameter (varies by option).
    :return:
    """
    pre_value = AUTO_IT.AU3_AutoItSetOption(LPCWSTR(option), INT(param))
    return pre_value


class Properties(object):
    """
    Below is an list of all the properties available in AutoItX.
    """
    SW_HIDE = 0
    SW_MAXIMIZE = 3
    SW_MINIMIZE = 6
    SW_RESTORE = 9
    SW_SHOW = 5
    SW_SHOWDEFAULT = 10
    SW_SHOWMAXIMIZED = 3
    SW_SHOWMINIMIZED = 2
    SW_SHOWMINNOACTIVE = 7
    SW_SHOWNA = 8
    SW_SHOWNOACTIVATE = 4
    SW_SHOWNORMAL = 1


class _Options(object):

    def __init__(self):
        self._caret_coord_mode = 1
        self._mouse_click_delay = 10
        self._mouse_click_down_delay = 10
        self._mouse_click_drag_delay = 250
        self._mouse_coord_mode = 1
        self._pixel_coord_mode = 1
        self._send_attach_mode = 0
        self._send_capslock_mode = 1
        self._send_key_delay = 5
        self._send_key_down_delay = 10
        self._win_detect_hidden_text = 0
        self._win_search_children = 0
        self._win_text_match_mode = 1
        self._win_title_match_mode = 1
        self._win_wait_delay = 250

    @property
    def CaretCoordMode(self):
        return self._caret_coord_mode

    @CaretCoordMode.setter
    def CaretCoordMode(self, value):
        auto_it_set_option('CaretCoordMode', value)
        self._caret_coord_mode = value

    @property
    def MouseClickDelay(self):
        return self._mouse_click_delay

    @MouseClickDelay.setter
    def MouseClickDelay(self, value):
        auto_it_set_option('MouseClickDelay', value)
        self._mouse_click_delay = value

    @property
    def MouseClickDownDelay(self):
        return self._mouse_click_down_delay

    @MouseClickDownDelay.setter
    def MouseClickDownDelay(self, value):
        auto_it_set_option('MouseClickDownDelay', value)
        self._mouse_click_down_delay = value

    @property
    def MouseClickDragDelay(self):
        return self._mouse_click_drag_delay

    @MouseClickDragDelay.setter
    def MouseClickDragDelay(self, value):
        auto_it_set_option('MouseClickDragDelay', value)
        self._mouse_click_drag_delay = value

    @property
    def MouseCoordMode(self):
        return self._mouse_coord_mode

    @MouseCoordMode.setter
    def MouseCoordMode(self, value):
        auto_it_set_option('MouseCoordMode', value)
        self._mouse_coord_mode = value

    @property
    def PixelCoordMode(self):
        return self._pixel_coord_mode

    @PixelCoordMode.setter
    def PixelCoordMode(self, value):
        auto_it_set_option('PixelCoordMode', value)
        self._pixel_coord_mode = value

    @property
    def SendAttachMode(self):
        return self._send_attach_mode

    @SendAttachMode.setter
    def SendAttachMode(self, value):
        auto_it_set_option('SendAttachMode', INT(value))
        self._send_attach_mode = value

    @property
    def SendCapslockMode(self):
        return self._send_capslock_mode

    @SendCapslockMode.setter
    def SendCapslockMode(self, value):
        auto_it_set_option('SendCapslockMode', value)
        self._send_capslock_mode = value

    @property
    def SendKeyDelay(self):
        return self._send_key_delay

    @SendKeyDelay.setter
    def SendKeyDelay(self, value):
        auto_it_set_option('SendKeyDelay', value)
        self._send_key_delay = value

    @property
    def SendKeyDownDelay(self):
        return self._send_key_down_delay

    @SendKeyDownDelay.setter
    def SendKeyDownDelay(self, value):
        auto_it_set_option('SendKeyDownDelay', value)
        self._send_key_down_delay = value

    @property
    def WinDetectHiddenText(self):
        return self._win_detect_hidden_text

    @WinDetectHiddenText.setter
    def WinDetectHiddenText(self, value):
        auto_it_set_option('WinDetectHiddenText', value)
        self._win_detect_hidden_text = value

    @property
    def WinSearchChildren(self):
        return self._win_search_children

    @WinSearchChildren.setter
    def WinSearchChildren(self, value):
        auto_it_set_option('WinSearchChildren', value)
        self._win_search_children = value

    @property
    def WinTextMatchMode(self):
        return self._win_text_match_mode

    @WinTextMatchMode.setter
    def WinTextMatchMode(self, value):
        auto_it_set_option('WinTextMatchMode', value)
        self._win_text_match_mode = value

    @property
    def WinTitleMatchMode(self):
        return self._win_title_match_mode

    @WinTitleMatchMode.setter
    def WinTitleMatchMode(self, value):
        auto_it_set_option('WinTitleMatchMode', value)
        self._win_title_match_mode = value

    @property
    def WinWaitDelay(self):
        return self._win_wait_delay

    @WinWaitDelay.setter
    def WinWaitDelay(self, value):
        auto_it_set_option('WinWaitDelay', value)
        self._win_wait_delay = value

class Commands(object):

    is_visible = "IsVisible"
    is_enabled = "IsEnabled"
    show_drop_down = "ShowDropDown"
    hide_drop_down = "HideDropDown"
    add_string = "AddString"
    del_string = "DelString"
    find_string = "FindString"
    set_current_selection = "SetCurrentSelection"
    is_checked = "IsChecked"
    check = "Check"
    un_check = "UnCheck"
    get_current_line = "GetCurrentLine"
    get_current_col = "GetCurrentCol"
    get_current_selection = "GetCurrentSelection"
    get_line_count = "GetLineCount"
    get_line = "GetLine"
    get_selected = "GetSelected"
    edit_paste = "EditPaste"
    current_tab = "CurrentTab"
    tab_right = "TabRight"
    tab_left = "TabLeft"
    de_select = "DeSelect"
    find_item = "FindItem"
    get_item_count = "GetItemCount"
    get_selected_count = "GetSelectedCount"
    get_sub_item_count = "GetSubItemCount"
    get_text = "GetText"
    is_selected = "IsSelected"
    select = "Select"
    select_all = "SelectAll"
    select_clear = "SelectClear"
    select_invert = "SelectInvert"
    view_change = "ViewChange"
    collapse = "Collapse"
    exists = "Exists"
    expand = "Expand"
    uncheck = "Uncheck"
options = _Options()
properties = Properties
commands = Commands
INTDEFAULT = -2147483647

@api.check(1, err_msg='clipboard is empty or contains a non-text entry')
def ClipGet(buf_size=256):
    """

    :param buf_size:
    :return:
    """
    clip = ctypes.create_unicode_buffer(buf_size)
    AUTO_IT.AU3_ClipGet(clip, INT(buf_size))
    return clip.value.rstrip()

@api.check(2, err_msg='Write text to clipboard failed')
def ClipPut(value):
    """

    :param value:
    :return:
    """
    ret = AUTO_IT.AU3_ClipPut(LPCWSTR(value))
    return ret

def IsAdmin():
    """

    :return:
    """
    ret = AUTO_IT.AU3_IsAdmin()
    return ret

def DriveMapAdd(device, share, flag=0, user='', pwd='', buf_size=256):
    """

    :param device:
    :param share:
    :param flag: 0 = default
        1 = Persistant mapping
        8 = Show authentication dialog if required
    :param user:
    :param pwd:
    :param buf_size:
    :return:
    """
    result = ctypes.create_unicode_buffer(buf_size)

    err_code = {
        1: "Undefined / Other error",
        2: "Access to the remote share was denied",
        3: "The device is already assigned",
        4: "Invalid device name",
        5: "Invalid remote share",
        6: "Invalid password"
    }
    AUTO_IT.AU3_DriveMapAdd(
        LPCWSTR(device), LPCWSTR(share), INT(flag), LPCWSTR(user),
        LPCWSTR(pwd), result, INT(buf_size))
    if Error():
        raise AutoItError(err_code.get(Error(), None))
    return result.value.rstrip()

@api.check(2, err_msg='the disconnection was unsuccessful')
def DriveMapDel(device):
    """

    :param device:
    :return:
    """
    ret = AUTO_IT.AU3_DriveMapDel(LPCWSTR(device))
    return ret

@api.check(1, err_msg='get the details of a mapped drive failed')
def DriveMapGet(device, buf_size=256):
    """

    :param device:
    :param buf_size:
    :return:
    """
    mapping = ctypes.create_unicode_buffer(buf_size)
    AUTO_IT.AU3_DriveMapGet(LPCWSTR(device), mapping, INT(buf_size))
    return mapping.value.rstrip()

def MouseClick(button='left', x=INTDEFAULT, y=INTDEFAULT, clicks=1, speed=-1):
    """

    :param button:
    :param x:
    :param y:
    :param clicks:
    :param speed:
    :return:
    """
    ret = AUTO_IT.AU3_MouseClick(LPCWSTR(button), INT(x), INT(y), INT(clicks), INT(speed))
    return ret

def MouseClickDrag(x1, y1, x2, y2, button='left', speed=-1):
    """

    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :param button:
    :param speed:
    :return:
    """

    ret = AUTO_IT.AU3_MouseClickDrag(
        LPCWSTR(button), INT(x1), INT(y1), INT(x2), INT(y2), INT(speed)
    )
    return ret

def MouseDown(button='left'):
    """

    :param button:
    :return:
    """
    AUTO_IT.AU3_MouseDown(LPCWSTR(button))

def MouseGetCursor():
    """

    :return:
    """
    ret = AUTO_IT.AU3_MouseGetCursor()
    return ret

def MouseGetPos():
    """

    :return:
    """
    p = POINT()
    AUTO_IT.AU3_MouseGetPos(ctypes.byref(p))
    return p.x, p.y

def MouseMove(x, y, speed=-1):
    """

    :param x:
    :param y:
    :param speed:
    :return:
    """
    ret = AUTO_IT.AU3_MouseMove(INT(x), INT(y), INT(speed))
    return ret

def MouseUp(button='left'):
    """

    :param button:
    :return:
    """
    AUTO_IT.AU3_MouseUp(LPCWSTR(button))

@api.check(1, err_msg='the direction is not recognized')
def MouseWheel(direction, clicks=-1):
    """

    :param direction: "up" or "down"
    :param clicks:
    :return:
    """
    AUTO_IT.AU3_MouseWheel(LPCWSTR(direction), INT(clicks))

def Opt(option, value):
    """

    :param option:
    :param value:
    :return:
    """
    return auto_it_set_option(option, value)

def PixelChecksum(left, top, right, bottom, step=1):
    """

    :param left:
    :param top:
    :param right:
    :param bottom:
    :param step:
    :return:
    """
    rect = RECT(left, top, right, bottom)
    ret = AUTO_IT.AU3_PixelChecksum(ctypes.byref(rect), INT(step))
    return ret

@api.check(2, unexpected_ret=(-1,), err_msg='invalid coordinates')
def PixelGetColor(x, y):
    """

    :param x:
    :param y:
    :return:
    """
    ret = AUTO_IT.AU3_PixelGetColor(INT(x), INT(y))
    return ret

@api.check(1, err_msg='color is not found')
def PixelSearch(left, top, right, bottom, col, var=1, step=1):
    """

    :param left:
    :param top:
    :param right:
    :param bottom:
    :param col:
    :param var:
    :param step:
    :return:
    """
    p = POINT()
    rect = RECT(left, top, right, bottom)
                                                                                               
                     

    AUTO_IT.AU3_PixelSearch(
        ctypes.byref(rect), INT(col), INT(var), INT(step), ctypes.byref(p)
    )
    return p.x, p.y

def Send(send_text, mode=0):
    """
    Sends simulated keystrokes to the active window.
    :param send_text:
    :param mode: Changes how "keys" is processed:
        flag = 0 (default), Text contains special characters like + and ! to
         indicate SHIFT and ALT key presses.
        flag = 1, keys are sent raw.
    :return:
    """
    AUTO_IT.AU3_Send(LPCWSTR(send_text), INT(mode))

def Tooltip(tip, x=INTDEFAULT, y=INTDEFAULT):
    """

    :param tip:
    :param x:
    :param y:
    :return:
    """
    AUTO_IT.AU3_ToolTip(LPCWSTR(tip), INT(x), INT(y))