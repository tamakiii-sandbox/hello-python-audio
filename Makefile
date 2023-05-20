.PHONY: help install uninstall build clean check-ignore

help:
	@cat $(firstword $(MAKEFILE_LIST))

install:
	python -m pip install .

uninstall: requirements.txt
	python -m pip uninstall -y -r $<

build: \
	dist/sine_wave.wav

clean:
	rm -rf dist/sine_wave.wav

dist/sine_wave.wav: dist
	python sine.py $@

dist:
	test -d $@ || mkdir $@

check-ignore:
	git check-ignore *
