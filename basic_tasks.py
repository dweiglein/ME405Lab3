"""!
@file basic_tasks.py
    This file contains a demonstration program that runs some tasks, an
    inter-task shared variable, and a queue. The tasks don't really @b do
    anything; the example just shows how these elements are created and run.

@author JR Ridgely
@date   2021-Dec-15 JRR Created from the remains of previous example
@copyright (c) 2015-2021 by JR Ridgely and released under the GNU
    Public License, Version 2. 
"""

import gc
import pyb
import cotask
import task_share


def task1(shares):
    """!
    Task which puts things into a share and a queue.
    @param shares A list holding the share and queue used by this task
    """
    # Get references to the share and queue which have been passed to this task
    accel_q = shares
    # read accel
    while True:
        accel_q.put(read_accel)

        yield 0


def task2(shares):
    """!
    Task which takes things out of a queue and share and displays them.
    @param shares A tuple of a share and queue from which this task gets data
    """
    # Get references to the share and queue which have been passed to this task
    accel_display = shares
    

    while True:
        # Show everything currently in the queue and the value in the share
        print(accel_display.get())
        
        yield 0


# This code creates a share, a queue, and two tasks, then starts the tasks. The
# tasks run until somebody presses ENTER, at which time the scheduler stops and
# printouts show diagnostic information about the tasks, share, and queue.
if __name__ == "__main__":
    acQ = task_share.Queue('l', 1000, thread_protect=False, overwrite=True, name='x_accel')
    task_1 = cotask.Task(task1, name = 'get accel',
                         priority = 2, period = 500, profile = True, trace=False, shares=(acQ))
    task_2 = cotask.Task(task2, name = 'print accel',
                         priority = 1, period = 500, profile = True, trace=False, shares=(acQ))
    

