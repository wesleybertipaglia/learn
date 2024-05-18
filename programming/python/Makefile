init: 
	@python3 -m venv venv

activate:
	@source venv/bin/activate

setup:	
	@pip3 install -r requirements.txt

freeze:
	@pip3 freeze > requirements.txt

test:
	@pytest
