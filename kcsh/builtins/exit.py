from kcsh.constants import *
from kcsh.exceptions.ExitShellException import ExitShellException


def exit(args):
    raise ExitShellException()
    return SHELL_STATUS_STOP
