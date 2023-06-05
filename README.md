# Introduction
This project is an API developped with for an issue tracking system.
The endpoints of this API and their usage are described in the [Postman documentation]()

## Prerequisites

You must have Python 3.6 or higher installed in order to execute this code.

## Installation

1 - Clone the github Repository.

```bash
git clone https://github.com/HaroldHaldemann/DjangoApp
```

2 - Create your virtual environment.

```bash
python -m venv name-virtual-env
```

3 - Activate your virtual environment.

On Windows
```windows
name-virtual-env\Scripts\activate.bat #In cmd
name-virtual-env\Scripts\Activate.ps1 #In Powershell
```

NB: If you activate your environment with Powershell, don't forget to enable running script :
```windows
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
```

On Unix/MacOs
```bash
source name-virtual-env/bin/activate
```

4 - Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required modules.

```bash
pip install -r ./requirements.txt
```

5 - Make the migrations for Django to enable the database

First go to the softdesk folder
```bash
cd ./softdesk
```

Then excute the migrations
```bash
python ./manage.py makemigrations
python ./manage.py migrate
```

## Usage

To execute this application, stay on the softdesk folder

Then execute the following command to launch the local server:

```bash
python ./manage.py runserver
```

The server will be available at http://127.0.0.1:8000/

Every endpoints and their documentation are available in the [Postman documentation]()
