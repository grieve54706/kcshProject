import os
from kcsh.constants import *


def getenv(args):
    if len(args) > 0:
        print(os.getenv(args[0]))
