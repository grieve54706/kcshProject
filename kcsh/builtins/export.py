import os
from kcsh.constants import *


def export(args):
    if len(args) > 0:
        var = args[0].split('=', 1)
        os.environ[var[0]] = var[1]
