all: clean arith

init:
	sudo apt-get install python3-pip -y
	sudo pip3 install -r requirements.txt

arith:
	pyinstaller --onefile --name arith ./src/__main__.py
	cp dist/arith ./
	rm -rf arith.spec build/ dist/

clean:
	rm -rf dist/ build/ arith.spec arith
