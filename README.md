# Home Kneads

A simple Django web application for hosting a pet adoption registry.

## Requirements

| Software | Installation |
| -------- | ------------ |
| Ubuntu 16.04 LTS+ | [Amazon LightSail](https://aws.amazon.com/getting-started/hands-on/launch-a-virtual-machine/) is recommended,<br> which can [upgrade to EC2](https://aws.amazon.com/lightsail/features/upgrade-to-ec2/) if necessary |
| Python 3.8 | See [troubleshooting](#troubleshooting) |
| Django 3.1 | `pip3.8 install django` |
| Django Bootstrap: | `pip3.8 install django-bootstrap4` |
| Pillow | `pip3.8 install pillow` |
| **Recommended software** | |
| Apache2 | `sudo apt-get install apache2` |
| **Optional software** | |
| MySQL 5.6+ | `sudo apt-get install mysql-server` |
| MySQL client | `pip3.8 install mysqlclient` |

## Installation

1. Install all [required software](#requirements)
1. Create a MySQL database if MySQL will be used as the backing database:

    ```bash
    # Create a MySQL database.
    > mysql -u root -p
    mysql> CREATE DATABASE HomeKneadsDB CHARACTER SET utf8;
    # If necessary, create a user with permission to manage the database.
    mysql> CREATE USER 'remote-user'@'%' IDENTIFIED BY '<password>';
    mysql> GRANT ALL PRIVILEGES ON HomeKneadsDB.* TO 'remote-user'@'%';
    mysql> FLUSH PRIVILEGES;
    mysql> QUIT;
    ```

1. Install the web application on the server:

    ```bash
    # Install the web application on the server.
    > sudo su
    > mkdir /home/django
    > cd /home/django
    > git clone https://github.com/jonhermsen-UNO/homekneads.git
    # Fix file permissions needed by the web application.
    > chown -R username:username ./homekneads
    > find ./homekneads -type d -exec chmod 750 {} \;
    > find ./homekneads -type f -exec chmod 640 {} \;
    ```

1. [Configure](#configuration) the *Home Kneads* instance as desired
1. Prepare the *Home Kneads* instance for deployment:

    ```bash
    # Initialize the database and its tables.
    > cd /home/django/homekneads
    > python3.8 manage.py migrate --settings=local_settings
    # Create an admin user for the Django admin pages (optional).
    > python3.8 manage.py createsuperuser --settings=local_settings
    # Manually add the desired species to the Species table.
    > python3.8 manage.py shell --settings=local_settings
    >>> from app.models import Species
    >>> s = Species(name="Cat", weight_uom="lbs")
    >>> s.save()
    >>> s = Species(name="Dog", weight_uom="lbs")
    >>> s.save()
    >>> s = Species(name="Bird", weight_uom="oz")
    >>> s.save()
    >>> exit()
    ```

1. Deploy the *Home Kneads* instance:

    * Ubuntu 20.04 LTS+: see the Django documentation on [Apache's mod_wsgi module](https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/modwsgi/)
    * Ubuntu 18.04 LTS, and earlier:

      ```bash
      # Run the web application using Django's development server (not recommended).
      # Note that a firewall exception might be needed to use port 8000, otherwise the
      # Apache proxy and proxy_http modules can be used to route traffic over port 80.
      > python3.8 manage.py runserver 0.0.0.0:8000 --settings=local_settings
      ```

## Configuration

1. Create the configuration file for the *Home Kneads* instance:

    ```bash
    # Create a configuration file to overwrite defaults.
    > cd /home/django/homekneads/
    > touch ./local_settings.py
    > chmod 640 ./local_settings.py
    ```

1. Use a preferred text editor to configure `./local_settings.py` as desired:

    ```python
    # Example configuration file.
    import os
    from homekneads.settings import *

    # Overwrite the secret key for production.
    SECRET_KEY = 'some-super-secret-key'

    # Overwrite debug settings for production.
    DEBUG = False
    ALLOWED_HOSTS = ['example.com', 'localhost', '127.0.0.1']

    # Overwrite the database configuration for production.
    # This example replaces SQLite with MySQL.
    DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'HomeKneadsDB',
        'USER': 'remote-user',
        'PASSWORD': "password",
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
          'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        },
      }
    }

    # Add a new configuration to set the root directory of static files.
    MEDIA_ROOT = os.path.join('/var/www/', 'media')
    STATIC_ROOT = os.path.join('/var/www/', 'static')
    ```

## Troubleshooting

* I cannot install `python3.8` on my version of Ubuntu
  * Run `sudo apt-get install libsqlite3-dev` first if SQLite will be used as the backing database
  * See these instructions for [installing Python 3.8](https://websiteforstudents.com/how-to-install-python-3-8-on-ubuntu-18-04-16-04/) on older versions of Ubuntu
    * The manual method is required for `pip3.8` to work
* I cannot install `mysqlclient` on my version of Ubuntu
  * Run `sudo apt-get install libmysqlclient-dev`
  * Rerun `pip3.8 install mysqlclient`
    * If necessary, install `python3.8-dev` using the PPA method from `python3.8` troubleshooting
  * See [installing the MySQL client](https://stackoverflow.com/questions/42152729/error-installing-mysqlclient-on-ubuntu-16-04-using-pip-and-python-3-6) for more information
