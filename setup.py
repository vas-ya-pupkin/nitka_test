from setuptools import find_packages, setup

NAME = "nitka-test"
PACKAGE = "nitka"

requirements = [
    # main requirements
    "alembic==1.13.1",
    "asyncpg==0.29.0",
    "fastapi==0.111.0",
    "pymysql==1.1.1",
    "python-dotenv==1.0.1",
    "pyyaml==6.0.1",
    "sqlalchemy==2.0.30",

    # test requirements
    "pytest==8.2.2",
]

setup(
    name=NAME,
    version="1.0.0",
    description="Nitka Test case",
    long_description="",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    author="Egor Dedov",
    author_email="afftarius@gmail.com",
    license="Proprietary",
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    install_requires=requirements,
)
