NAME=cliptor

all: bin/$(NAME) bin/images bin/main_ui.py bin/result_ui.py bin/output_ui.py bin/main_rc.py bin/main.py bin/output.py bin/result.py bin/utils.py
	python -c 'import compileall; compileall.compile_dir("bin")'

bin/$(NAME): src/$(NAME)
	cp src/$(NAME) bin/$(NAME)

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
	pyuic4 src/main.ui -o bin/main_ui.py

bin/result_ui.py: src/result.ui
	pyuic4 src/result.ui -o bin/result_ui.py

bin/output_ui.py: src/output.ui
	pyuic4 src/output.ui -o bin/output_ui.py

bin/main_rc.py: src/main.qrc
	pyrcc4 src/main.qrc -o bin/main_rc.py

clean:
	rm -rf bin/*

run: all
	bin/cliptor
