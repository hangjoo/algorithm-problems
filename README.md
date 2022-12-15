# Algorithm Problems

## Features

- Create source code template for specified platform.
- Save solutions on `./solution_db.json`.
- [TODO] Generate solution list on README.md.

## Script

### Requirements

- `rich` : `pip install rich`

### Create source code template

- You can create source code template for each template.
- You can edit each template file from `./utils/templates/`.

### How to use

#### 1. Run script

```bash
python main.py
```

#### 2. Select 'Add Solution' task

```text
Select task id:
  (0) Add Solution
>> 0
```

#### 3. Select 'platform'

```text
Select platform id:
  (0) Baekjoon
  (1) LeetCode
>> 0
```

#### 4. Write problem info

```text
Write problem information:
>> Problem ID: xxxx
>> Problem name: zzzz
```
