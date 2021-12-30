from os import kill
from signal import CTRL_C_EVENT
from subprocess import Popen


def kill_subprocess(process: Popen):
    process.terminate()
    # pid = process.pid
    # kill(pid, CTRL_C_EVENT)
