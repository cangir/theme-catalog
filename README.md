## Introduction

A simple web application that provides list of free web themes within a variety of categories and tags. 
Authenticated users have the ability to post, edit, and delete their own items.

## Preview

![Theme Catalog preview](https://github.com/cangir/theme-catalog/blob/master/preview.jpg)

**[View Demo](https://cleanbootstrap.com)**

## Project Overview
Coming soon


## Requirements

- [Python 3](https://www.python.org/downloads/) - The code uses ver 3.7.3
- [VirtualBox](https://www.virtualbox.org/) - An open source virtualiztion product. (Optional)
- [Vagrant](https://www.vagrantup.com/) - A virtual environment builder and manager (Optional)

## Instructions using Vagrant

1. If you don't already have the latest version of python download it from the link in requirements.
2. Download and install Vagrant and VirtualBox.
3. Clone this repository.
4. Navigate to the `theme-catalog` folder in your bash interface.
5. Open bash terminal and launch the virtual machine with command `vagrant up`
6. Once Vagrant installs necessary files use `vagrant ssh` to continue.
7. The command line will now start with vagrant. Here get into to the shared /vagrant folder by command `cd /vagrant`.
8. Finally run `python3 manage.py runserver`.

## Instructions without Vagrant

1. If you don't already have the latest version of python download it from the link in requirements.
2. Download and install Vagrant and VirtualBox.
3. Clone this repository.
4. Navigate to the `theme-catalog` folder in your bash interface.
5. Open bash terminal and install requirements with command `pip install -r requirements.txt`
6. Finally run `python manage.py runserver`.



## Troubleshooting
If your command prompt does not start with vagrant after typing `vagrant ssh` then please try the `winpty vagrant ssh` on your Windows system.