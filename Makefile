.PHONY: help install uninstall check-ignore

help:
	@cat $(firstword $(MAKEFILE_LIST))

install:
	python -m pip install .

uninstall: requirements.txt
	python -m pip uninstall -y -r $<

check-ignore:
	git check-ignore *
