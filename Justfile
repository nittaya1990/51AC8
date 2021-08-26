set shell := ["bash.exe", "-c"]

parse:
    python ./src/stparser.py

test:
    pytest
