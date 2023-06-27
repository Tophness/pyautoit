# -*- coding: utf-8 -*-
__author__ = 'Jace Xu'
from .autoit import INTDEFAULT, AUTO_IT
from .autoit import api
from ctypes.wintypes import *
import ctypes

@api.check(2, 'send click message failed')
def ControlClick(title, text, control, button="left", clicks=1, x="center", y="center"):
    """

    :param title:
    :param text:
    :param control:
    :param button:
    :param clicks:
    :param x:
    :param y:
    :return:
    """
    ret = AUTO_IT.AU3_ControlClick(LPCWSTR(title), LPCWSTR(text), LPCWSTR(control), LPCWSTR(button), INT(clicks), INT(x), INT(y))
    return ret

@api.check(2, 'send click message failed')
def ControlClickByHandle(hwnd, h_ctrl, button="left", clicks=1, x="center", y="center"):
    """

    :param handle:
    :param kwargs:
    :return:
    """
    ret = AUTO_IT.AU3_ControlClickByHandle(HWND(hwnd), HWND(h_ctrl), LPCWSTR(button), INT(clicks), INT(x), INT(y))
    return ret

@api.check(1, 'no window match the criteria')
def ControlCommand(title, text, control, command, extra="", buf_size=256):
    """

    :param title:
    :param control:
    :param command:
    :param extra:
    :param buf_size:
    :return:
    """
    result = ctypes.create_unicode_buffer(buf_size)
    AUTO_IT.AU3_ControlCommand(LPCWSTR(title), LPCWSTR(text), LPCWSTR(control), LPCWSTR(command), LPCWSTR(extra), result, INT(buf_size))
    return result.value.rstrip()

@api.check(1, 'no window match the criteria')
def ControlCommandByHandle(hwnd, h_ctrl, command, extra="", buf_size=256):
    """

    :param hwnd:
    :param h_ctrl:
    :param command:
    :param kwargs:
    :return:
    """
    result = ctypes.create_unicode_buffer(buf_size)
    AUTO_IT.AU3_ControlCommandByHandle(HWND(hwnd), HWND(h_ctrl), LPCWSTR(command), LPCWSTR(extra), result, INT(buf_size))
    return result.value.rstrip()

@api.check(1, 'Window/Control could not be found')
def ControlListView(title, text, control, command, extra1="", extra2="", buf_size=256):
    """

    :param title:
    :param control:
    :param command:
    :param args:
    :param kwargs:
    :return:
    """
    result = ctypes.create_unicode_buffer(buf_size)
    AUTO_IT.AU3_ControlListView(LPCWSTR(title), LPCWSTR(text), LPCWSTR(control), LPCWSTR(command), LPCWSTR(extra1), LPCWSTR(extra2), result, INT(buf_size))
    return result.value.rstrip()

@api.check(1, 'Window/Control could not be found')
def ControlListViewByHandle(hwnd, h_ctrl, command, extra1="", extra2="", buf_size=256):
    """

    :param hwnd:
    :param h_ctrl:
    :param command:
    :param kwargs:
    :return:
    """
    result = ctypes.create_unicode_buffer(buf_size)
    AUTO_IT.AU3_ControlListViewByHandle(HWND(hwnd), HWND(h_ctrl), LPCWSTR(command), LPCWSTR(extra1), LPCWSTR(extra2), result, INT(buf_size))
    return result.value.rstrip()

@api.check(2, 'Window/Control could not be found')
def ControlDisable(title, text, control):
    """

    :param title:
    :param control:
    :param kwargs:
    :return:
    """
    ret = AUTO_IT.AU3_ControlDisable(LPCWSTR(title), LPCWSTR(text), LPCWSTR(control))
    return ret

@api.check(2, 'Window/Control could not be found')
def ControlDisableByHandle(hwnd, h_ctrl):
    """

    :param hwnd:
    :param h_ctrl:
    :return:
    """
    ret = AUTO_IT.AU3_ControlDisableByHandle(HWND(hwnd), HWND(h_ctrl))
    return ret

@api.check(2, 'Window/Control could not be found')
def ControlEnable(title, text, control):
    """

    :param title:
    :param control:
    :param kwargs:
    :return:
    """
    ret = AUTO_IT.AU3_ControlEnable(LPCWSTR(title), LPCWSTR(text), LPCWSTR(control))
    return ret

@api.check(2, 'Window/Control could not be found')
def ControlEnableByHandle(hwnd, h_ctrl):
    """

    :param hwnd:
    :param h_ctrl:
    :return:
    """
    ret = AUTO_IT.AU3_ControlEnableByHandle(HWND(hwnd), HWND(h_ctrl))
    return ret

@api.check(2, 'Window/Control could not be found')
def ControlFocus(title, text, control):
    """

    :param title:
    :param control:
    :param kwargs:
    :return:
    """
    ret = AUTO_IT.AU3_ControlFocus(LPCWSTR(title), LPCWSTR(text), LPCWSTR(control))
    return ret

@api.check(2, 'Window/Control could not be found')
def ControlFocusByHandle(hwnd, h_ctrl):
    """

    :param hwnd:
    :param h_ctrl:
    :return:
    """
    ret = AUTO_IT.AU3_ControlFocusByHandle(HWND(hwnd), HWND(h_ctrl))
    return ret

@api.check(1, 'Window/Control could not be found')
def ControlGetFocus(title, text, buf_size=256):
    """

    :param title:
    :param kwargs:
    :return:
    """
    ctrl_with_focus = ctypes.create_unicode_buffer(buf_size)
    AUTO_IT.AU3_ControlGetFocus(LPCWSTR(title), LPCWSTR(text), ctrl_with_focus, INT(buf_size))
    return ctrl_with_focus.value.rstrip()

@api.check(1, 'Window/Control could not be found')
def ControlGetFocusByHandle(hwnd, buf_size=256):
    """

    :param hwnd:
    :param buf_size:
    :return:
    """
    ctrl_with_focus = ctypes.create_unicode_buffer(buf_size)
    AUTO_IT.AU3_ControlGetFocusByHandle(HWND(hwnd), ctrl_with_focus, INT(buf_size))
    return ctrl_with_focus.value.rstrip()

@api.check(1, 'Window/Control could not be found')
def ControlGetHandle(hwnd, control):
    """

    :param hwnd:
    :param control:
    :return:
    """
    ret = AUTO_IT.AU3_ControlGetHandle(HWND(hwnd), LPCWSTR(control))
    return ret

@api.check(1, 'Window/Control could not be found')
def ControlGetHandleAsText(title, text, control, buf_size=256):
    """

    :param title:
    :param control:
    :param kwargs:
    :return:
    """
    ret_text = ctypes.create_unicode_buffer(buf_size)
    AUTO_IT.AU3_ControlGetHandleAsText(LPCWSTR(title), LPCWSTR(text), LPCWSTR(control), ret_text, INT(buf_size))
    return ret_text.value.rstrip()

@api.check(1, 'Window/Control could not be found')
def ControlGetPos(title, text, control):
    """

    :param title:
    :param control:
    :param text:
    :return:
    """
    rect = RECT()
    AUTO_IT.AU3_ControlGetPos(LPCWSTR(title), LPCWSTR(text), LPCWSTR(control), ctypes.byref(rect))
    return (rect.left, rect.top, rect.right, rect.bottom)

@api.check(1, 'Window/Control could not be found')
def ControlGetPosByHandle(hwnd, h_ctrl):
    """

    :param hwnd:
    :param h_ctrl:
    :return:
    """
    rect = RECT()
    AUTO_IT.AU3_ControlGetPosByHandle(HWND(hwnd), HWND(h_ctrl), ctypes.byref(rect))
    return (rect.left, rect.top, rect.right, rect.bottom)

@api.check(1, 'Window/Control could not be found')
def ControlGetText(title, text, control, buf_size=256):
    """

    :param title:
    :param control:
    :param kwargs:
    :return:
    """
    ctrl_text = ctypes.create_unicode_buffer(buf_size)
    AUTO_IT.AU3_ControlGetText(LPCWSTR(title), LPCWSTR(text), LPCWSTR(control), ctrl_text, INT(buf_size))
    return ctrl_text.value.rstrip()

@api.check(1, 'Window/Control could not be found')
def ControlGetTextByHandle(hwnd, h_ctrl, buf_size=256):
    """

    :param hwnd:
    :param h_ctrl:
    :return:
    """
    ctrl_text = ctypes.create_unicode_buffer(buf_size)
    AUTO_IT.AU3_ControlGetTextByHandle(HWND(hwnd), HWND(h_ctrl), ctrl_text, INT(buf_size))
    return ctrl_text.value.rstrip()

@api.check(2, 'Window/Control could not be found')
def ControlHide(title, text, control):
    """

    :param title:
    :param control:
    :param kwargs:
    :return:
    """
    ret = AUTO_IT.AU3_ControlHide(LPCWSTR(title), LPCWSTR(text), LPCWSTR(control))
    return ret

@api.check(2, 'Window/Control could not be found')
def ControlHideByHandle(hwnd, h_ctrl):
    """

    :param hwnd:
    :param h_ctrl:
    :return:
    """
    ret = AUTO_IT.AU3_ControlHideByHandle(HWND(hwnd), HWND(h_ctrl))
    return ret

@api.check(2, 'Window/Control could not be found')
def ControlMove(title, text, control, x, y, width=-1, height=-1):
    """

    :param title:
    :param control:
    :param x:
    :param y:
    :param kwargs:
    :return:
    """
    ret = AUTO_IT.AU3_ControlMove(LPCWSTR(title), LPCWSTR(text), LPCWSTR(control), INT(x), INT(y), INT(width), INT(height))
    return ret

@api.check(2, 'Window/Control could not be found')
def ControlMoveByHandle(hwnd, h_ctrl, x, y, width=-1, height=-1):
    """

    :param hwnd:
    :param h_ctrl:
    :param x:
    :param y:
    :param width:
    :param height:
    :return:
    """
    ret = AUTO_IT.AU3_ControlMoveByHandle(HWND(hwnd), HWND(h_ctrl), INT(x), INT(y), INT(width), INT(height))
    return ret

@api.check(2, 'Window/Control could not be found')
def ControlSend(title, text, control, send_text, mode=0):
    """

    :param title:
    :param control:
    :param send_text:
    :param mode:
    flag = 0 (default), Text contains special characters like + to indicate
        SHIFT and {LEFT} to indicate left arrow.
    flag = 1, keys are sent raw.
    :param kwargs:
    :return:
    """
    ret = AUTO_IT.AU3_ControlSend(LPCWSTR(title), LPCWSTR(text), LPCWSTR(control), LPCWSTR(send_text), INT(mode))
    return ret

@api.check(2, 'Window/Control could not be found')
def ControlSendByHandle(hwnd, h_ctrl, send_text, mode=0):
    """

    :param hwnd:
    :param h_ctrl:
    :param send_text:
    :param mode:
    :return:
    """
    ret = AUTO_IT.AU3_ControlSendByHandle(HWND(hwnd), HWND(h_ctrl), LPCWSTR(send_text), INT(mode))
    return ret

@api.check(2, 'Window/Control could not be found')
def ControlSetText(title, text, control, control_text):
    """

    :param title:
    :param control:
    :param control_text:
    :param kwargs:
    :return:
    """
    ret = AUTO_IT.AU3_ControlSetText(LPCWSTR(title), LPCWSTR(text), LPCWSTR(control), LPCWSTR(control_text))
    return ret

@api.check(2, 'Window/Control could not be found')
def ControlSetTextByHandle(hwnd, h_ctrl, control_text):
    """

    :param hwnd:
    :param h_ctrl:
    :param control_text:
    :return:
    """
    ret = AUTO_IT.AU3_ControlSetTextByHandle(HWND(hwnd), HWND(h_ctrl), LPCWSTR(control_text))
    return ret

@api.check(2, 'Window/Control could not be found')
def ControlShow(title, text, control):
    """

    :param title:
    :param control:
    :param kwargs:
    :return:
    """
    ret = AUTO_IT.AU3_ControlShow(LPCWSTR(title), LPCWSTR(text), LPCWSTR(control))
    return ret

@api.check(2, 'Window/Control could not be found')
def ControlShowByHandle(hwnd, h_ctrl):
    """

    :param hwnd:
    :param h_ctrl:
    :return:
    """
    ret = AUTO_IT.AU3_ControlShowByHandle(HWND(hwnd), HWND(h_ctrl))
    return ret

@api.check(1, 'Window/Control could not be found')
def ControlTreeView(title, text, control, command, extra1='', extra2='', buf_size=256):
    """

    :param title:
    :param control:
    :param command:
    :param args:
    :param kwargs:
    :return:
    """
    result = ctypes.create_unicode_buffer(buf_size)
    AUTO_IT.AU3_ControlTreeView(LPCWSTR(title), LPCWSTR(text), LPCWSTR(control), LPCWSTR(command), LPCWSTR(extra1), LPCWSTR(extra2), result, INT(buf_size))
    return result.value.rstrip()

@api.check(1, 'Window/Control could not be found')
def ControlTreeViewByHandle(hwnd, h_ctrl, command, extra1='', extra2='', buf_size=256):
    """

    :param hwnd:
    :param h_ctrl:
    :param command:
    :param kwargs:
    :return:
    """
    result = ctypes.create_unicode_buffer(buf_size)
    AUTO_IT.AU3_ControlTreeViewByHandle(HWND(hwnd), HWND(h_ctrl), LPCWSTR(command), LPCWSTR(extra1), LPCWSTR(extra2), result, INT(buf_size))
    return result.value.rstrip()

@api.check(1, 'Window/Control could not be found')
def StatusbarGetText(title, text='', part=1, buf_size=256):
    """

    :param title:
    :param text:
    :param part: The "part" number of the status bar to read - the default
        is 1. 1 is the first possible part and usually the one that contains
        the useful messages like "Ready" "Loading...", etc.
    :param buf_size:
    :return:
    """
    sb_text = ctypes.create_unicode_buffer(buf_size)
    AUTO_IT.AU3_StatusbarGetText(LPCWSTR(title), LPCWSTR(text), INT(part), sb_text, INT(buf_size))
    return sb_text.value.rstrip()

@api.check(1, 'Window/Control could not be found')
def StatusbarGetTextByHandle(hwnd, part=1, buf_size=256):
    """

    :param hwnd:
    :param part:
    :param buf_size:
    :return:
    """
    statusbar_text = ctypes.create_unicode_buffer(buf_size)
    AUTO_IT.AU3_StatusbarGetTextByHandle(HWND(hwnd), INT(part), statusbar_text, INT(buf_size))
    return statusbar_text.value.rstrip()