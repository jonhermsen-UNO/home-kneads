# Home Kneads

A simple Django web application for hosting a pet adoption registry.

## Requirements

| Software | Installation |
| -------- | ------------ |
| Ubuntu 16.04 LTS+ | [Amazon LightSail](https://aws.amazon.com/getting-started/hands-on/launch-a-virtual-machine/) recommended<br>[Upgrade to EC2](https://aws.amazon.com/lightsail/features/upgrade-to-ec2/) if necessary |
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
1. If you are using a MySQL database, then create your database instance

    ```bash
    # Create a new MySQL database to store application data, for example:
    > mysql -p root -u
    mysql> CREATE DATABASE HomeKneadsDB CHARACTER SET utf8;
    # If necessary, create a user with permission to manage the database.
    mysql> CREATE USER 'remote-user'@'%' IDENTIFIED BY '<password>';
    mysql> GRANT ALL PRIVILEGES ON HomeKneadsDB.* TO 'remote-user'@'%';
    mysql> FLUSH PRIVILEGES;
    ```

1. TODO: instructions for installing the project itself
1. [Configure](#configuration) your instance of *Home Kneads*, as desired
1. Prepare your instance of *Home Kneads* for deployment

    ```bash
    # Prepare the database for use.
    > python3.8 manage.py migrate --settings=local_settings
    # Create an admin user for the Django admin pages (optional).
    > python3.8 manage.py createsuperuser --settings=local_settings

1. Deploy your instance of *Home Kneads*

    ```bash
    # TODO: add deployment instructions
    ```

## Configuration

1. TODO: config instructions for Django application
1. Verify that your instance of *Home Kneads* is functional

    ```bash
    # Test from your local machine.
    > python3.8 manage.py runserver --settings=local_settings
    # Test from your web server.
    # Note that you may need to allow port 8000 in your firewall.
    > python3.8 manage.py runserver 0.0.0.0:8000 --settings=local_settings
    ```

## Troubleshooting

* I cannot install `python3.8` on my version of Ubuntu
  * See these instructions for [installing Python 3.8](https://websiteforstudents.com/how-to-install-python-3-8-on-ubuntu-18-04-16-04/)
  * The PPA method is recommended
* I cannot install `mysqlclient` on my version of Ubuntu
  * Run `sudo apt-get install python3.8-dev libmysqlclient-dev`
  * Retry `pip3.8 install mysqlclient`
  * See [installing the MySQL client](https://stackoverflow.com/questions/42152729/error-installing-mysqlclient-on-ubuntu-16-04-using-pip-and-python-3-6) for more information
