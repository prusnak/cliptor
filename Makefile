NAME=cliptor

# pyuic4 or pyside-uic
PYUIC=pyuic4
# pyrcc4 or pyside-rcc
PYRCC=pyrcc4

all: bin/$(NAME) bin/images bin/main_ui.py bin/result_ui.py bin/output_ui.py bin/main_rc.py bin/main.py bin/output.py bin/result.py bin/utils.py
	python -c 'import compileall; compileall.compile_dir("bin")'

bin/$(NAME): src/$(NAME).py
	cp src/$(NAME).py bin/$(NAME)
	chmod +x bin/$(NAME)

bin/images: src/images
	cp -r src/images bin/images

bin/main.py: src/main.py
	cp src/main.py bin/main.py

bin/output.py: src/output.py
	cp src/output.py bin/output.py

bin/result.py: src/result.py
	cp src/result.py bin/result.py

bin/utils.py: src/utils.py
	cp src/utils.py bin/utils.py

bin/main_ui.py: src/main.ui
	$(PYUIC) src/main.ui -o bin/main_ui.py

bin/result_ui.py: src/result.ui
	$(PYUIC) src/result.ui -o bin/result_ui.py

bin/output_ui.py: src/output.ui
	$(PYUIC) src/output.ui -o bin/output_ui.py

bin/main_rc.py: src/main.qrc
	$(PYRCC) src/main.qrc -o bin/main_rc.py

clean:
	rm -rf bin/*

run: all
	bin/cliptor
