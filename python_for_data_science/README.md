## 1. Python Virtual Environment Setup

### Create a virtual environment
```bash
python3 -m venv <venv_dir>
```
---

### Activate the virtual environment
```bash
source <venv_dir>/bin/activate
```
---

### Install packages
```bash
pip install <package1> <package2> ...
```
---

### Freeze installed packages to a file
```bash
pip freeze > requirements.txt
```
---

### Install packages from a file
```bash
pip install -r requirements.txt
```
---

### Deactivate the virtual environment
```bash
deactivate
```
---

<br>

## 2. Code Style Check with flake8

### Install flake8:
```bash
pip install flake8
```
---
### Check if the Python code follows the [PEP8](https://peps.python.org/pep-0008/) style guide:
```bash
flake8 <file.py>
```

<br>

## 3. Build & Install Your Own Package

### Install the build tool:
```bash
pip install build
```
---

### Build the package:
From the project root (where `pyproject.toml` is located):
```bash
python -m build
```
This will generate a `dist/` folder containing:
* `.tar.gz` (source archive)
* `.whl` (wheel file)
---

### Install the package:
```bash
pip install ./dist/ft_package-0.0.1.tar.gz
# or
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```
---

### Verify installation:
```bash
pip list
pip show -v ft_package
```
---
