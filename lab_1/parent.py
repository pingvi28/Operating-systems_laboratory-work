#!/usr/bin/python3
import os
import sys
import random

N = int(sys.argv[1])

cnt_ch = N
while cnt_ch > 0:
    child = os.fork()

    if child > 0:
        print(f"Parent [{os.getpid()}]: I ran children process with PID {child}")
    else:
        os.execl("./child.py", "./child.py", str(random.randint(5, 10)))

    if child > 0:
        cnt_ch -= 1

cnt_ch = N
while cnt_ch > 0:
    ch_pid, status = os.wait()
    if status != 0:
        child = os.fork()

        if child > 0:
            print(f"Parent [{os.getpid()}]: I ran children process with PID {child}")
        else:
            os.execl("./child.py", "./child.py", str(random.randint(5, 10)))
    else:
        print(f"   Parent [{os.getpid()}]: Child with PID {ch_pid} terminated. Exit Status {status}")
        cnt_ch -= 1

os._exit(os.EX_OK)
