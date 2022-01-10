from subprocess import PIPE, Popen


def kill_subprocess(process: Popen):
    process.terminate()


def spawn_subprocess(args: str, shell=True):
    popen = Popen(
        args,
        shell=shell,
        stdout=PIPE,
        stderr=PIPE,
        stdin=PIPE
    )

    return popen
