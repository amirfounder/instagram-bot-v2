from os import kill, name
from signal import CTRL_C_EVENT
from subprocess import PIPE, Popen


def kill_subprocess_by_pid(pid: int):
    kill(pid, CTRL_C_EVENT)


def kill_subprocess(process: Popen):
    process.terminate()


def spawn_subprocess(args: str, shell=None, stdout=None, stderr=None, stdin=None) -> Popen:
    popen = Popen(
        args,
        shell=shell or True,
        stdout=stdout or PIPE,
        stderr=stderr or PIPE,
        stdin=stdin or PIPE
    )

    return popen


def read_output(popen: Popen):
    output: bytes
    output = popen.stdout.readline()
    output = output.decode('utf-8')
    output = output.removesuffix('\n')

    return output