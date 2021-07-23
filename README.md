### Command to activate virtual environment:

This is an attempt to implement a bookshop api in Python using the Flask library.

Run the following 2 commands to install the virtual enviroment from requirements.txt:
```bash
python -m venv ./venv
```
```bash
python -m pip install -r requirements.txt
```

This command will activate the virtual environment:
```bash
source venv/bin/activate
```

### Command to run unit tests:

#### Note:
Before running the test, please start the server from the folder, app with the following command:

```bash
python app.py
```
Once the server has started, use the following command to run the tests
```bash
python -m unittest
```

### Below are commands to start the docker containers

command to start docker container locally
```bash
docker-compose --env-file ./dev.env up --build
```
