import builtins
import sys


def open(file):
    return sys.stdin if file == '-' else builtins.open(file, newline='')
