#!/usr/bin/python3.8
import hidden_4
import sys

if __name__ == "__main__":
    module_names = dir(hidden_4)

    for name in module_names:
        if not name.startswith("__"):
            print(name)
