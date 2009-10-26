NAME=cliptor

all: $(NAME) ui_main.py main.py main_rc.py

ui_main.py: main.ui
	pyuic4 main.ui -o ui_main.py

main_rc.py: main.qrc
	pyrcc4 main.qrc -o main_rc.py

clean:
	rm -f ui_main.py main_rc.py *.pyc *.pyo
