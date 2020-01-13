pyinstaller=pyinstaller

init:
	pip3 install -r requirements.txt

arith:
	$(pyinstaller) --onefile --name arith ./src/__main__.py
	mv dist/arith ./
	rm -rf arith.spec build/ dist/
