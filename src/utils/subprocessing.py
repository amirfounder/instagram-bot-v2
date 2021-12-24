from os import kill
from signal import CTRL_C_EVENT
from subprocess import Popen


def kill_subprocess(process: Popen):
    pid = process.pid
    kill(pid, CTRL_C_EVENT)


def spawn_subprocess(*args, **kwargs):
    Popen(*args, **kwargs)
