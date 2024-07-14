import os
import pathlib
from dotenv import load_dotenv

dotenv_path = pathlib.Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path)

mysql_user = os.getenv("MYSQL_USER")
mysql_password = os.getenv("MYSQL_PASSWORD")
mysql_host = os.getenv("MYSQL_HOST")

if not all([mysql_user, mysql_password, mysql_host]):
    dsn = "mysql+pymysql://root:@localhost/nitka"
else:
    dsn = f'mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}:3306/nitka'
