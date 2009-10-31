NAME=cliptor

all: $(NAME) ui_main.py ui_result.py ui_output.py main.py main_rc.py

ui_main.py: main.ui
	pyuic4 main.ui -o ui_main.py

ui_result.py: result.ui
	pyuic4 result.ui -o ui_result.py

ui_output.py: output.ui
	pyuic4 output.ui -o ui_output.py

main_rc.py: main.qrc
	pyrcc4 main.qrc -o main_rc.py

clean:
	rm -f ui_*.py main_rc.py *.pyc *.pyo
