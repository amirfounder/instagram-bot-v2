from multiprocessing import active_children
from multiprocessing.context import Process
from typing import Any

def spawn_process(target, args: tuple[Any] = ())-> Process:
    process = Process(target=target, args=args)
    process.start()

    return process


def terminate_process_by_pid(pid: int):
    processes = active_children()
    for p in processes:
        if p.pid == pid:
            p.terminate()
            p.close()