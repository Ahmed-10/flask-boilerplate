# flask-boilerplate
a general boilerplate to start building flask app

## installation
----------------------------
- create a virtual environment and activate the virtual environment
```bash
python3 -m venv venv; source venv/bin/activate;
```
- install the dependencies
```bash
pip install -r requirements.txt
```
- create env file
```bash
touch .env
```
- generate a secret key using the following command
```bash
python -c "import os; print(os.urandom(24))"
```

- add the secret key to the _`.env`_ file

```
SECRET_KEY=<your_secret_key>
```

## run the application locally
----------------------------
```bash
flask run
```