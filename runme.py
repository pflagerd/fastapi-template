#!/usr/bin/env python3
import os
import setmeup
import subprocess
import sys

def main(args, debug=False):
    setmeup.main([])

    if os.path.exists("./main.py"):
        os.execvp(".venv/bin/fastapi", [".venv/bin/fastapi", "dev", "main.py"])

if __name__ == "__main__":
    sys.exit(main(sys.argv))

