from collections import namedtuple

from .add_solution import add_solution


TASK_CLASS = namedtuple("Task", ("name", "task_function"))


TASK = {
    "0": TASK_CLASS("Add Solution", add_solution),
}
