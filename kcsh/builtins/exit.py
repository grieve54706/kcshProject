import sys
from clint.textui import colored, puts
from kcsh.exceptions import ExitShellException


def exit(args):
    puts(colored.green('電：提督我們下次再見'))
    raise ExitShellException('Exit')
