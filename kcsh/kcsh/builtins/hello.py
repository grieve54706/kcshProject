import sys
from kcsh.constants import *


def hello(args):
    sys.stdout.write('Hi! Grieve. May I help you ?' + '\n')
    return SHELL_STATUS_RUN
