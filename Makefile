BIN = leaden


.PHONY: all build clean install uninstall distclean


all: build


build:
	pyuic5 -x $(BIN)/ui.ui -o $(BIN)/ui.py


clean:
	$(RM) $(BIN)/ui.py
	$(RM) -dr $(BIN).egg-info
	$(RM) -dr $(BIN)/__pycache__
	$(RM) -dr build
	$(RM) -dr dist


install:
	python setup.py -v install --user


uninstall:
	pip uninstall -v -y $(BIN)


distclean: uninstall
distclean: clean
