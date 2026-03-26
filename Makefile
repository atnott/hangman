.PHONY: all run install clean

all: run

run:
	python3 -m src.main

clean:
	rm -rf `find . -name "__pycache__"`
	rm -f .DS_Store

