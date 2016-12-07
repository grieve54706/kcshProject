class ExitShellException(Exception):
    def __init__(self):

    def __str__(self):
        return repr('ExitShell')
