# -*- coding: utf-8 -*-
__author__ = 'Jace Xu'
from .autoit import AUTO_IT
from .autoit import api
from .autoit import AutoItError
from ctypes.wintypes import *
from ctypes import create_unicode_buffer, byref
from .autoit import properties

@api.check(2, "activate window failed, maybe the window doesn't exist")
def WinActivate(title, text=''):
    """
    Activates (gives focus to) a window.
    :param title:
    :param text:
    :return:
    """
    ret = AUTO_IT.AU3_WinActivate(LPCWSTR(title), LPCWSTR(text))
    return ret

@api.check(2, "activate window failed, maybe the window doesn't exist")
def WinActivateByHandle(handle):
    """

    :param handle:
    :return:
    """
    ret = AUTO_IT.AU3_WinActivateByHandle(HWND(handle))
    return ret

def WinActive(title, text=''):
    """

    :param title:
    :param text:
    :return:
    """
    ret = AUTO_IT.AU3_WinActive(LPCWSTR(title), LPCWSTR(text))
    return ret

def WinActiveByHandle(handle):
    """

    :param handle:
    :return:
    """
    ret = AUTO_IT.AU3_WinActiveByHandle(HWND(handle))
    return ret

@api.check(2, "close this window failed, maybe the window doesn't exist")
def WinClose(title, text=''):
    """

    :param title:
    :param text:
    :return:
    """
    ret = AUTO_IT.AU3_WinClose(LPCWSTR(title), LPCWSTR(text))
    return ret

@api.check(2, 'close window failed, maybe the window does not exist')
def WinCloseByHandle(handle):
    """

    :param handle:
    :return:
    """
    ret = AUTO_IT.AU3_WinCloseByHandle(HWND(handle))
    return ret

def WinExists(title, text=''):
    """
    Checks to see if a specified window exists.
    :param title: The title of the window to check.
    :param text: The text of the window to check.
    :return: Returns 1 if the window exists, otherwise returns 0.
    """
    ret = AUTO_IT.AU3_WinExists(LPCWSTR(title), LPCWSTR(text))
    return ret

def WinExistsByHandle(handle):
    """

    :param handle:
    :return:
    """
    ret = AUTO_IT.AU3_WinExistsByHandle(HWND(handle))
    return ret

@api.check(1, 'get the coordinates of the caret failed')
def WinGetCaretPos():
    """
    Returns the coordinates of the caret in the foreground window
    :return:
    """
    p = POINT()
    AUTO_IT.AU3_WinGetCaretPos(byref(p))
    return (p.x, p.y)

def WinGetClassList(title, text='', buf_size=200):
    """

    :param title:
    :param text:
    :param buf_size:
    :return:
    """
    rec_text = create_unicode_buffer(buf_size)
    AUTO_IT.AU3_WinGetClassList(LPCWSTR(title), LPCWSTR(text), rec_text, INT(buf_size))
    msg = rec_text.value.rstrip()
    return msg

def WinGetClassListByHandle(handle, buf_size=200):
    """

    :param handle:
    :param buf_size:
    :return:
    """
    rec_text = create_unicode_buffer(buf_size)
    AUTO_IT.AU3_WinGetClassListByHandle(HWND(handle), rec_text, INT(buf_size))
    msg = rec_text.value.rstrip()
    return msg

def WinGetClientSize(title, text=''):
    """

    :param title:
    :param text:
    :return:
    """
    rect = RECT()
    ret = AUTO_IT.AU3_WinGetClientSize(LPCWSTR(title), LPCWSTR(text), byref(rect))
    if ret == 1:
        raise AutoItError('get the size of client failed')
    return (rect.right, rect.bottom)

def WinGetClientSizeByHandle(handle):
    """

    :param handle:
    :return:
    """
    rect = RECT()
    ret = AUTO_IT.AU3_WinGetClientSizeByHandle(HWND(handle), byref(rect))
    if ret == 1:
        raise AutoItError('get the size of client failed')
    return (rect.right, rect.bottom)

@api.check(3, 'No window match the criteria')
def WinGetHandle(title, text=''):
    """

    :param title:
    :param text:
    :return:
    """
    ret = AUTO_IT.AU3_WinGetHandle(LPCWSTR(title), LPCWSTR(text))
    return ret

@api.check(1, 'No window match the criteria')
def WinGetHandleAsText(title, text='', buf_size=16):
    """

    :param title:
    :param text:
    :param buf_size:
    :return:
    """
    rec_text = create_unicode_buffer(buf_size)
    AUTO_IT.AU3_WinGetHandleAsText(LPCWSTR(title), LPCWSTR(text), rec_text, INT(buf_size))
    msg = rec_text.value
    return msg

def WinGetPos(title, text=''):
    """

    :param title:
    :param text:
    :return:
    """
    rect = RECT()
    res = AUTO_IT.AU3_WinGetPos(LPCWSTR(title), LPCWSTR(text), byref(rect))
    if res == 1:
        raise AutoItError('No window match the criteria')
    return (rect.left, rect.top, rect.right, rect.bottom)

def WinGetPosByHandle(handle):
    """

    :param handle:
    :return:
    """
    rect = RECT()
    res = AUTO_IT.AU3_WinGetPosByHandle(HWND(handle), byref(rect))
    if res == 1:
        raise AutoItError('No window match the handle: %s' % str(handle))
    return (rect.left, rect.top, rect.right, rect.bottom)

@api.check(2, 'No window match the criteria', unexpected_ret=(-1,))
def WinGetProcess(title, text=''):
    """

    :param title:
    :param text:
    :return:
    """
    res = AUTO_IT.AU3_WinGetProcess(LPCWSTR(title), LPCWSTR(text))
    return res

@api.check(2, 'No window match the criteria', unexpected_ret=(-1,))
def WinGetProcessByHandle(handle):
    """

    :param handle:
    :return:
    """
    res = AUTO_IT.AU3_WinGetProcessByHandle(HWND(handle))
    return res

@api.check(2, 'No window match the criteria')
def WinGetState(title, text=''):
    """
    Retrieves the state of a given window.
    :param title:
    :param text:
    :return:
    1 = Window exists
    2 = Window is visible
    4 = Windows is enabled
    8 = Window is active
    16 = Window is minimized
    32 = Windows is maximized
    """
    res = AUTO_IT.AU3_WinGetState(LPCWSTR(title), LPCWSTR(text))
    return res

@api.check(2, 'No window match the criteria')
def WinGetStateByHandle(handle):
    """

    :param handle:
    :return:
    """
    res = AUTO_IT.AU3_WinGetStateByHandle(HWND(handle))
    return res

def WinGetText(title, text='', buf_size=256):
    """

    :param title:
    :param text:
    :param buf_size:
    :return:
    """
    ret_text = create_unicode_buffer(buf_size)
    AUTO_IT.AU3_WinGetText(LPCWSTR(title), LPCWSTR(text), ret_text, INT(buf_size))
    val = ret_text.value.rstrip()
    return val

def WinGetTextByHandle(handle, buf_size=256):
    """

    :param handle:
    :return:
    """
    ret_text = create_unicode_buffer(buf_size)
    AUTO_IT.AU3_WinGetTextByHandle(HWND(handle), ret_text, INT(buf_size))
    return ret_text.value.rstrip()

def WinGetTitle(title, text='', buf_size=256):
    """

    :param title:
    :param text:
    :return:
    """
    ret_text = create_unicode_buffer(buf_size)
    AUTO_IT.AU3_WinGetTitle(LPCWSTR(title), LPCWSTR(text), ret_text, INT(buf_size))
    val = ret_text.value.rstrip()
    return val

def WinGetTitleByHandle(handle, buf_size=256):
    """

    :param handle:
    :param buf_size:
    :return:
    """
    ret_text = create_unicode_buffer(buf_size)
    AUTO_IT.AU3_WinGetTitleByHandle(HWND(handle), ret_text, INT(buf_size))
    val = ret_text.value.rstrip()
    return val

@api.check(2, 'No window match the criteria')
def WinKill(title, text=''):
    """

    :param title:
    :param text:
    :return:
    """
    ret = AUTO_IT.AU3_WinKill(LPCWSTR(title), LPCWSTR(text))
    return ret

@api.check(2, 'No window match the criteria')
def WinKillByHandle(handle):
    """

    :param handle:
    :return:
    """
    ret = AUTO_IT.AU3_WinKillByHandle(HWND(handle))
    return ret

@api.check(2, 'the menu item could not be found')
def WinMenuSelectItem(title, text='', *items):
    """
    Usage:
        win_menu_select_item("[CLASS:Notepad]", "", u"文件(&F)", u"退出(&X)")
    :param title:
    :param text:
    :param items:
    :return:
    """
    if not 0 < len(items) < 8:
        raise ValueError('accepted none item or number of items exceed eight')
    f_items = [LPCWSTR(item) for item in items]
    for i in range(8 - len(f_items)):
        f_items.append(LPCWSTR(''))
    ret = AUTO_IT.AU3_WinMenuSelectItem(LPCWSTR(title), LPCWSTR(text), *f_items)
    return ret

@api.check(2, 'the menu item could not be found')
def WinMenuSelectItemByHandle(handle, *items):
    """

    :param handle:
    :param items:
    :return:
    """
    if not 0 < len(items) < 8:
        raise ValueError('accepted none item or number of items exceed eight')
    f_items = [LPCWSTR(item) for item in items]
    for i in range(8 - len(f_items)):
        f_items.append(LPCWSTR(''))
    ret = AUTO_IT.AU3_WinMenuSelectItemByHandle(HWND(handle), *f_items)
    return ret

def WinMinimizeAll():
    """

    :return:
    """
    AUTO_IT.AU3_WinMinimizeAll()

def WinMinimizeAllUndo():
    """

    :return:
    """
    AUTO_IT.AU3_WinMinimizeAllUndo()

@api.check(2, 'No window match the criteria')
def WinMove(title, text='', x=0, y=0, width=-1, height=-1):
    """

    :param title:
    :param text:
    :param x:
    :param y:
    :param width:
    :param height:
    :return:
    """
    ret = AUTO_IT.AU3_WinMove(LPCWSTR(title), LPCWSTR(text), INT(x), INT(y), INT(width), INT(height))
    return ret

@api.check(2, 'No window match the criteria')
def WinMoveByHandle(handle, x, y, width=-1, height=-1):
    """

    :param handle:
    :param x:
    :param y:
    :param width:
    :param height:
    :return:
    """
    ret = AUTO_IT.AU3_WinMoveByHandle(HWND(handle), INT(x), INT(y), INT(width), INT(height))
    return ret

@api.check(2, 'No window match the criteria')
def WinSetOnTop(title, text='', flag=1):
    """

    :param title:
    :param flag: 1=set on top flag, 0 = remove on top flag
    :param kwargs:
    :return:
    """
    ret = AUTO_IT.AU3_WinSetOnTop(LPCWSTR(title), LPCWSTR(text), INT(flag))
    return ret

@api.check(2, 'No window match the criteria')
def WinSetOnTopByHandle(handle, flag=1):
    """

    :param handle:
    :param flag:
    :return:
    """
    ret = AUTO_IT.AU3_WinSetOnTopByHandle(HWND(handle), INT(flag))
    return ret

@api.check(2, 'No window match the criteria')
def WinSetState(title, text='', flag=properties.SW_SHOW):
    """

    :param title:
    :param flag: The "show" flag of the executed program:
        SW_HIDE = Hide window
        SW_SHOW = Shows a previously hidden window
        SW_MINIMIZE = Minimize window
        SW_MAXIMIZE = Maximize window
        SW_RESTORE = Undoes a window minimization or maximization
    :param kwargs:
    :return:
    """
    ret = AUTO_IT.AU3_WinSetState(LPCWSTR(title), LPCWSTR(text), INT(flag))
    return ret

@api.check(2, 'No window match the criteria')
def WinSetStateByHandle(handle, flag=properties.SW_SHOW):
    """

    :param handle:
    :param flag:
    :return:
    """
    ret = AUTO_IT.AU3_WinSetStateByHandle(HWND(handle), INT(flag))
    return ret

@api.check(2, 'No window match the criteria')
def WinSetTitle(title, text='', new_title=''):
    """

    :param title:
    :param new_title:
    :param kwargs:
    :return:
    """
    ret = AUTO_IT.AU3_WinSetTitle(LPCWSTR(title), LPCWSTR(text), LPCWSTR(new_title))
    return ret

@api.check(2, 'No window match the criteria')
def WinSetTitleByHandle(handle, new_title):
    """

    :param handle:
    :param new_title:
    :return:
    """
    ret = AUTO_IT.AU3_WinSetTitleByHandle(HWND(handle), LPCWSTR(new_title))
    return ret

@api.check(2, 'No window match the criteria')
def WinSetTrans(title, text='', trans=255):
    """
    Sets the transparency of a window.
    :param title:
    :param trans: A number in the range 0 - 255. The larger the number,
        the more transparent the window will become.
    :param kwargs:
    :return:
    """
    ret = AUTO_IT.AU3_WinSetTrans(LPCWSTR(title), LPCWSTR(text), INT(trans))
    return ret

@api.check(2, 'No window match the criteria')
def WinSetTransByHandle(handle, trans):
    """

    :param handle:
    :param trans:
    :return:
    """
    ret = AUTO_IT.AU3_WinSetTransByHandle(HWND(handle), INT(trans))
    return ret

@api.check(2, 'timeout on wait for window exists')
def WinWait(title, text='', timeout=0):
    """

    :param title:
    :param timeout:
    :param kwargs:
    :return:
    """
    ret = AUTO_IT.AU3_WinWait(LPCWSTR(title), LPCWSTR(text), INT(timeout))
    return ret

@api.check(2, 'timeout on wait for window exists')
def WinWaitByHandle(handle, timeout):
    """

    :param handle:
    :param timeout:
    :return:
    """
    ret = AUTO_IT.AU3_WinWaitByHandle(HWND(handle), INT(timeout))
    return ret

@api.check(2, 'timeout on wait for activate window')
def WinWaitActive(title, text='', timeout=0):
    """

    :param title:
    :param timeout:
    :param kwargs:
    :return:
    """
    ret = AUTO_IT.AU3_WinWaitActive(LPCWSTR(title), LPCWSTR(text), INT(timeout))
    return ret

@api.check(2, 'timeout on wait for activate window')
def WinWaitActiveByHandle(handle, timeout):
    """

    :param handle:
    :param timeout:
    :return:
    """
    ret = AUTO_IT.AU3_WinWaitActiveByHandle(HWND(handle), INT(timeout))
    return ret

@api.check(2, 'timeout on wait for close window')
def WinWaitClose(title, text='', timeout=0):
    """

    :param title:
    :param timeout:
    :param kwargs:
    :return:
    """
    ret = AUTO_IT.AU3_WinWaitClose(LPCWSTR(title), LPCWSTR(text), INT(timeout))
    return ret

@api.check(2, 'timeout on wait for close window')
def WinWaitCloseByHandle(handle, timeout):
    """

    :param handle:
    :param timeout:
    :return:
    """
    ret = AUTO_IT.AU3_WinWaitCloseByHandle(HWND(handle), INT(timeout))
    return ret

@api.check(2, 'timeout on wait for deactivate window')
def WinWaitNotActive(title, text='', timeout=0):
    """

    :param title:
    :param timeout:
    :param kwargs:
    :return:
    """
    ret = AUTO_IT.AU3_WinWaitNotActive(LPCWSTR(title), LPCWSTR(text), INT(timeout))
    return ret

@api.check(2, 'timeout on wait for deactivate window')
def WinWaitNotActiveByHandle(handle, timeout):
    """

    :param handle:
    :param timeout:
    :return:
    """
    ret = AUTO_IT.AU3_WinWaitNotActiveByHandle(HWND(handle), INT(timeout))
    return ret