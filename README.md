OpenNote
========

Introduction
--------------------------------------

OpenNote is an open-source note taking system, that you can host yourself.

--------------------------------------
__Installation__

1. Clone the repo to a local folder
2. Install the following packages:

| Package | Command |
| ------------- | ------------- |
|  __python__         |    pip install python            |
|  __eve__            |    pip install eve               |
|  __flask-boostrap__ |    pip install flask-bootstrap   |
|  __mongodb__        |    pip install mongodb           |


--------------------------------------
__Setup__

To start the server, first initialise mongodb (mongod --dbpath data/db)
Next, you want to start your python server (python run.py)


--------------------------------------
__Quick Start__

Your docs will be here: http://127.0.0.1:5000/docs
And you can hit the API from here: http://127.0.0.1:5000