Nitka test case
===============

Prerequisites:
--------------
- Python 3.12
- MySQL with a database named `nitka`


Installation:
-------------

```bash
git clone <repo address>
cd <repo folder>
```

In the root of the cloned repo, create a `.env` file with the following content:
```
MYSQL_USER=<your mysql username>
MYSQL_PASSWORD=<your mysql password>
MYSQL_HOST=<your mysql host>
```


Create & activate a Python venv.

Finally,
```bash
pip install -e .

alembic upgrade head
```