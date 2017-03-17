# Cookiecutter Tornado
Use me to build  python-tornado projects. Make life easier.

## Usage
### Create New Project
```shell
# install cookiecutter for your native OS, which need python >= 2.7
pip install cookiecutter

# Switch to your working directory
cd ~/workspace

# Execute the following command and follow the prompts
cookiecutter https://github.com/denglj/cookiecutter-tornado.git

So far, a new project has been created in your working directory
```

### Create virtual environment
I recommend that you create a separate virtual environment for each project.
View [pyenv](https://github.com/pyenv/pyenv) for more infomation.

Suppose you have installed `pyenv` by [pyenv-installer](https://github.com/pyenv/pyenv-installer)

```shell
# 2.7.13 just an example, use whatever you want
pyenv virtualenv --no-site-packages 2.7.13 your_project_name

# enter virtualenv
pyenv activate your_project_name

# exit virtualenv
pyenv deactivate
```

### Install pypi dependencies
```shell
# Switch to your project root directory which is the same level as Makefile
cd /path/to/project_dir

# edit requirements/xxx.in as you need

# edit requirements.txt

make deps

make pip
```

### Lint your code
```shell
make lint
```

### Run unit test
```shell
make test
```

### Run your project
```shell
python your_project_name/run.py

# check server
curl http//127.0.0.1:8000

# you'll see the index.html source code
```

### Clean up junk files
```shell
make clean
```
