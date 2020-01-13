createvirt:
	virtualenv venv
	./venv/Scripts/python -m pip install -r requirements.txt

create:
	python -m pip install -r requirements.txt
