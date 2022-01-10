from os import kill
from signal import CTRL_C_EVENT
from subprocess import PIPE, Popen


def kill_subprocess_by_pid(pid: int):
    kill(pid, CTRL_C_EVENT)


def kill_subprocess(process: Popen):
    process.terminate()


def spawn_subprocess(args: str, shell=None, stdout=None, stderr=None, stdin=None):
    popen = Popen(
        args,
        shell=shell | True,
        stdout=stdout | PIPE,
        stderr=stderr | PIPE,
        stdin=stdin | PIPE
    )

    return popen


def read_output(popen: Popen):
    output: bytes
    output = popen.stdout.readline()
    output = output.decode('utf-8')
    output = output.removesuffix('\n')

    return output