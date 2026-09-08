## Installation Process

- Download Python
- Download Code Editor ( I am choosing VS Code)

- open project folder
- inside I am making a directory app ( to make it a python package we will add init module)
- init.py
- main.py

Now we will create virtul environment to our project, because if we install any package, it will be installed globally, We can use such packages everywhere,
instead we will create virtual environment and install our packages inside the same. In this way, we can isolate our project.

We will use built-in virtual environment in Python

In terminal
```
python -m venv ./venv
```

It is used to create virtual environment for your Python Project.

1. python
```
python
```
This tells your computer:

**Use Python to execute a command/module.**

2. -m
```
python -m
```
-m means:

**Run a Python module as a program.**

3. venv
```
python -m venv
```
venv is Python's built-in module for creating virtual environments.

A virtual environment gives your project its own isolated Python environment and packages.

**Example:**
```
Project A
   ↓
venv
   ├── FastAPI 1.x
   └── Pydantic ...

Project B
   ↓
venv
   ├── FastAPI 2.x
   └── Pydantic ...
```

