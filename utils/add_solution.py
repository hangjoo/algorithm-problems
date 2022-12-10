import os
from collections import namedtuple, OrderedDict
import shutil
import sys

from rich import print
import json


SOLUTION_DIR = "./solutions"
SOLUTION_RECORD_FILE = "./solution_db.json"
SOLUTION_TEMPLATE = os.path.join(os.path.dirname(__file__), "solution_template.py")

PLATFORM_CLASS = namedtuple("PLATFORM", ("name", "platform_path"))

PLATFORM = {
    "0": PLATFORM_CLASS("Baekjoon", os.path.join(SOLUTION_DIR, "Baekjoon")),
}


def add_solution():
    # select platform
    print("\n[bold]Select platform id[/bold]:")
    for platform_id, platform in PLATFORM.items():
        print(f"  ({platform_id}) {platform.name}")
    selected_platform = input(">> ")
    try:
        selected_platform = PLATFORM[selected_platform]
    except KeyError:
        print("[red]!! ERROR !![/red] Invalid platform id")
        sys.exit()
    os.makedirs(selected_platform.platform_path, exist_ok=True)

    # write solution info
    print("\n[bold]Write problem information[/bold]:")
    problem_id = input(">> Problem ID: ")
    problem_name = input(">> Problem name: ")
    solution_path = os.path.join(selected_platform.platform_path, f"{problem_id}-{problem_name}.py")
    shutil.copy(SOLUTION_TEMPLATE, solution_path)

    # add to solution record file
    with open(SOLUTION_RECORD_FILE, "r") as f:
        solution_db = json.load(f)

    with open(SOLUTION_RECORD_FILE, "w") as f:
        info = {
            "problem_id": problem_id,
            "problem_name": problem_name,
            "solution_path": solution_path,
        }
        solution_db[selected_platform.name].append(OrderedDict(info))
        json.dump(solution_db, f, ensure_ascii=False, indent=4)
