all: clean arith

arith:
	pyinstaller --onefile --name arith ./src/__main__.py
	cp dist/arith ./
	rm -rf arith.spec build/ dist/

clean:
	rm -rf dist/ build/ arith.spec arith
