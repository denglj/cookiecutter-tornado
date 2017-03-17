WITH_ENV = env `cat .env 2>/dev/null | xargs`

COMMANDS = help clean deps pip lint test docs
.PHONY: $(COMMANDS)

help:
	@echo "usage: make <option>"
	@echo "options and effects:"
	@echo "    clean:    delete unnecessary files. such as .pyc, __pycache__ ..."
	@echo "    docs :    generate documentations."
	@echo "    deps :    use pip-compile get all pypi dependences."
	@echo "    pip  :    upgrage pip and install pypi packages."
	@echo "    lint :    static code check with flake8, include code style and complexity and errors."
	@echo "    test :    make unittest with pytest."


clean:
	@find . -name '*.pyc' -type f -delete
	@find . -name '__pycache__' -type d -delete
	@find . -type d -empty -delete
	@rm -rf build dist htmlcov
	@rm -rf .cache
	@rm -rf .coverage


deps:
	@pip install -U pip-tools
	@pip-compile --output-file requirements/base.txt requirements/base.in
	@pip-compile --output-file requirements/dev.txt requirements/dev.in
	@pip-compile --output-file requirements/production.txt requirements/production.in
	@pip-compile --output-file requirements/test.txt requirements/test.in
	@echo "\033[31m!!! don't forget change the requirements.txt, fill in the correct file name\033[0m"

pip:
	@[ -n "$(VIRTUAL_ENV)" ] || (echo 'out of virtualenv'; exit 1)
	@pip install -U pip setuptools pip-tools
	@pip-sync requirements.txt

lint:
	@echo "\033[94m[lint]\033[0m , change config at .pylintrc"
	@$(WITH_ENV) pylint --load-plugins=pylint.extensions.mccabe --max-complexity=11 {{ cookiecutter.project_slug }}

test:
	@echo "\033[94m[test]\033[0m with coverage, change config at pytest.ini"
	@$(WITH_ENV) pytest --cov-config .coveragerc --cov-report term-missing --cov={{ cookiecutter.project_slug }}

docs:
	@$(WITH_ENV) $(MAKE) -C docs html
