#!/usr/bin/env python3
import os
import setmeup
import subprocess
import sys

def main(args, debug=False):
    setmeup.main([])

    launcher = "chromium-browser"
    if not setmeup.spawn('which chromium-browser').returncode:
        subprocess.Popen([launcher, "--user-data-dir=" + os.getcwd() + "/.chromium-browser", "--new-window"] + args[1:], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        if not setmeup.spawn('which open').returncode:
            launcher = "open"
        elif not setmeup.spawn('which gio').returncode:
            launcher = "gio"
        else:
            print('Neither chromium-browser, open nor gio is available in your PATH, cannot launch default browser', file=sys.stderr)

        for tab in tabs:
            subprocess.Popen([launcher, tab], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if os.path.exists("./main.py"):
        os.execvp(".venv/bin/fastapi", [".venv/bin/fastapi", "dev", "main.py"])

if __name__ == "__main__":
    sys.exit(main(sys.argv))

