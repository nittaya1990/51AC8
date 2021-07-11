default:
    @just --list

alias ex := example
example:
    python src/skRun.py src/test.sk --log
