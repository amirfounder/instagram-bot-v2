from threading import Thread, enumerate
from typing import Any

def spawn_thread(target, args: tuple[Any] = ())-> Thread:
    thread = Thread(target=target, args=args)
    thread.start()

    return thread


def terminate_process_by_pid(ident: int):
    threads = enumerate()
    for thread in threads:
        if thread.ident == ident:
            thread._stop()