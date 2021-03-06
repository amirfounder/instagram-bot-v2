from threading import Thread, enumerate
from typing import Any

def spawn_thread(target, args: tuple[Any] = ())-> Thread:
    thread = Thread(target=target, args=args, daemon=True)
    thread.start()

    return thread
