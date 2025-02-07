# fastapi_learn_tutorial_user_guide/first_steps/tutorial001.py/README.md

This repository contains artifacts generated when David and Dan (D&D) executed the tutorial at [FastAPI > Learn > Tutorial - User Guide > First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/).

<br>

## TODO
   DONE

<br>

## Setup
You must have python3 and git.

| OS | git | python3 |
| -------- | -------- | -------- |
| kubuntu 24.04.1 LTS   | 2.43.0, 2.45.2   | Python 3.12.3   |
| kubuntu 24.10   | 2.45.2   | Python 3.12.7   |
| macOS Sequoia 15.1.1   | 2.39.5 (Apple Git-154)   | Python 3.12.7   |

Git clone current repo to your local machine

​	`git clone https://github.com/pflagerd/fastapi_learn_tutorial_user_guide.git`

Change your working directory to fastapi_learn_tutorial_user_guide repository

​	`cd path/to/fastapi_learn_tutorial_user_guide`

Type

```commandline
./RUNME
```

In the shell from which you just executed `./RUNME` you should see something like:
```

   FastAPI   Starting development server 🚀
 
             Searching for package file structure from directories with __init__.py files
             Importing from /home/oy753c/desktops/neon-algorithms/fastapi_learn_tutorial_user_guide
 
    module   🐍 main.py
 
      code   Importing the FastAPI app object from the module with the following code:
 
             from main import app
 
       app   Using import string: main:app
 
    server   Server started at http://127.0.0.1:8000
    server   Documentation at http://127.0.0.1:8000/docs
 
       tip   Running in development mode, for production use: fastapi run
 
             Logs:
 
      INFO   Will watch for changes in these directories: ['/home/oy753c/desktops/neon-algorithms/fastapi_learn_tutorial_user_guide']
      INFO   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
      INFO   Started reloader process [65407] using WatchFiles
      INFO   Started server process [65477]
      INFO   Waiting for application startup.
      INFO   Application startup complete.
      INFO   127.0.0.1:46272 - "GET / HTTP/1.1" 200
      INFO   127.0.0.1:46272 - "GET /favicon.ico HTTP/1.1" 404
```

In a new browser window or tab, you should see something like this:

![image](https://github.com/user-attachments/assets/d2fc96ae-722b-464c-942d-5cb6f44d5ac4)
