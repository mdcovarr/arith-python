all: init arith test

init:
	pip3 install -r requirements.txt

arith:
	pyinstaller --onefile --name arith ./src/__main__.py
	mv dist/arith ./
	rm -rf arith.spec build/ dist/

test:
	cp arith ./cse210A-asgtest/
	cd  ./cse210A-asgtest && ./test.sh

clean:
	rm -rf dist/ build/ arith.spec arith
