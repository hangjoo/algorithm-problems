# Algorithm Problems

## Features

- `solutions` 경로에 해결한 문제 소스코드 저장
- `python main.py` 명령어로 소스코드 템플릿 파일 생성
- [TODO] `README.md`에 플랫폼 별로 현재까지 푼 문제 목록 생성

## Script

`main.py`를 사용하여 여러 자동화 기능을 사용 가능.

### Create source code template

- 알고리즘 문제에서 주로 사용하는 소스 코드 템플릿을 생성하는 기능
- 스크립트 실행 후 `Add solution`을 선택하여 실행 가능
- 소스코드 템플릿은 `utils/solution_template.py`에서 수정

### Requirements

- `rich` : `pip install rich`

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
>> 0
```

#### 4. Write problem info

```text
Write problem information:
>> Problem ID: xxxx
>> Problem name: zzzz
```
