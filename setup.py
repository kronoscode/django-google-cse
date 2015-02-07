from setuptools import setup

required = []
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name = "django_google_cse",
    version = "0.1",

    author = "Helmy Giacoman",
    author_email = "helmy@kronoscode.com",
    install_requires = required,
    classifiers=[
        "Framework :: Django",
    ],
)

