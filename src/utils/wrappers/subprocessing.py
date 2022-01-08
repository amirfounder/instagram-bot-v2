from os import kill
from signal import CTRL_C_EVENT
from subprocess import PIPE, STDOUT, Popen, DEVNULL


def kill_subprocess(process: Popen):
    process.terminate()
    # pid = process.pid
    # kill(pid, CTRL_C_EVENT)


def spawn_subprocess(args: str, shell=True, suppress_output=False):
    stdout = DEVNULL if suppress_output else PIPE
    stderr = DEVNULL if suppress_output else PIPE
    stdin = DEVNULL if suppress_output else PIPE

    popen = Popen(
        args,
        shell=shell,
        stdout=stdout,
        stderr=stderr,
        stdin=stdin
    )

    return popen


def process_output():
    pass