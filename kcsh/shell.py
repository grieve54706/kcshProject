#!/usr/bin/python
# -*- coding: utf8 -*-
import os
import sys
import shlex
import getpass
import socket
import signal
import subprocess
import platform
from clint.textui import colored
from kcsh import shell
from kcsh.builtins import *
from kcsh.constants import *
from kcsh.exceptions import *

map_cmd = {}


if __name__ == "__main__":
    main()


def main():
    init()
    shell_loop()


def init():
    register_command("cd", cd)
    register_command("exit", exit)
    register_command("history", history)
    register_command("hello", hello)


def register_command(key, func):
    map_cmd[key] = func


def shell_loop():
    status = SHELL_STATUS_RUN

    while True:
        display_cmd_prompt()
        ignore_signals()
        try:
            # FIXME: 會有亂碼問題
            # cmd = input(str(colored.green('電：提督、請下命令') + ">"))
            cmd = sys.stdin.readline()
            cmd_tokens = tokenize(cmd)
            cmd_tokens = preprocess(cmd_tokens)
            execute(cmd_tokens)
        except ExitShellException:
            break
        except Exception as e:
            _, err, _ = sys.exc_info()
            print(err)


def display_cmd_prompt():
    sys.stdout.write(colored.green('電：提督、請下命令') + ">")
    sys.stdout.flush()


def ignore_signals():
    if platform.system() != "Windows":
        signal.signals(signal.SIGTSTP, signal.SIG_IGN)

    signal.signal(signal.SIGINT, signal.SIG_IGN)


def tokenize(string):
    return shlex.split(string)


def preprocess(tokens):
    processed_token = []
    for token in tokens:
        if token.startswith('>'):
            # 不確定os.getenv
            processed_token.append(os.getenv(token[1:]))
        else:
            processed_token.append(token)
    return processed_token


def execute(cmd_tokens):
    with open(HISTORY_PATH, 'a') as history_file:
        history_file.write(' '.join(cmd_tokens) + os.linesep)

    if cmd_tokens:
        cmd_key = cmd_tokens[0]  # 取第一個作指令
        cmd_args = cmd_tokens[1:]  # 第一個以後的都是參數

        if cmd_key in map_cmd:
            return map_cmd[cmd_key](cmd_args)  # 回傳動作後結束

        # 若找無動作為超出範圍，拋出exception
        signal.signal(signal.SIGINT, handler_kill)

        # 產生子執行緒執行原本的系統指令
        if platform.system() == "Windows":
            command = ""
            for i in cmd_tokens:
                command = command + " " + i
            os.system(command)
        else:
            p = subprocess.Popen(cmd_tokens)
            p.communicate()

    return SHELL_STATUS_RUN


def handler_kill(sigum, frame):
    raise OSError("Killed!")
