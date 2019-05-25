REQUIREMENTS_FILE = "requirements.txt"


.PHONY: dep test

all: dep test
dep:
	@echo "Start to install dependencies."
	pip3 install -r ${REQUIREMENTS_FILE}
	@echo "Necessary deps installed"		

test:
	@echo "Start to run test"
	pytest -v 
