import win32gui
import win32api
import win32con
import time


subHandles = []


def getWinHandle(windowsType='KCV'):
    # 滑鼠位置取得hwnd
    # mousePos = win32api.GetCursorPos
    # hwnd = win32gui.WindowFromPoint(mousePos)

    # Find KCV
    pHandle = win32gui.FindWindow(None, '提督業も忙しい！')
    win32gui.EnumChildWindows(pHandle, collectHandle, None)

    for tmpHwnd in subHandles:
        hwnd = win32gui.FindWindowEx(
            tmpHwnd, 0, 'Internet Explorer_Server', None)
        if hwnd:
            break
    # print(hwnd)
    # win32gui.SetForegroundWindow(hwnd)

    LeftClick(hwnd, 50, 50)

    # Find poi
    # pHandle = win32gui.FindWindow(None, 'poi')


def collectHandle(hwnd, param):
    subHandles.append(hwnd)


def LeftClick(hwnd, x, y):
    pos = win32api.MAKELONG(x, y)
    win32api.PostMessage(hwnd, win32con.WM_LBUTTONDOWN,
                         win32con.MK_LBUTTON, pos)
    win32api.PostMessage(hwnd, win32con.WM_LBUTTONUP,
                         win32con.MK_LBUTTON, pos)
