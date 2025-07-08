### Create virtual environment
```
python3 -m venv <venv_dir>
```

### Activate the virtual environment
```
source <venv_dir>/bin/activate
```

### Install packages
```
pip install <packages>
```

### Freeze the current package list into a file
```
pip freeze > requirements.txt
```

### Install packages from a file
```
pip install -r requirements.txt
```

### Deactivate the virtual environment
```
deactivate
```

### Check PEP8-Norm
```
flake8 <file.py>
```
