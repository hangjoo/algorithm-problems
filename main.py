import sys
from utils import TASK
from rich import print


def main():
    print("[bold]Select task id[/bold]:")
    for task_id, task in TASK.items():
        print(f"  ({task_id}) {task.name}")
    selected_task_id = input(">> ")

    try:
        selected_task = TASK[selected_task_id]
    except KeyError:
        print("[red]!! ERROR !![/red] Invalid task id")
        sys.exit()

    selected_task.task_function()


if __name__ == "__main__":
    main()
