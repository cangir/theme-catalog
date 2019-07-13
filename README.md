## Introduction
A simple web application that provides list of free web themes within a variety of categories and tags. 
Authenticated users have the ability to post, edit, and delete their own items.

## Preview
![Theme Catalog preview](https://github.com/cangir/theme-catalog/blob/master/screenshots/preview.jpg)

**[View Demo](https://cleanbootstrap.com)**

**Please note that:** *demo doesn't have authentication features.*

*In order to see demo pages, you need to run the project.*

*But you can still see the screenshots section.*

## Project Overview
This is the fourth project for the Udacity Full Stack Nanodegree. This project allows users to perform Create, Read, Update, and Delete operations.
Logging in is not required in order to read the categories or items uploaded. But, users need to log in to access CRUD operations such as adding, editing and removing items.
This program uses third-party auth with Facebook.

Some of the technologies used to build this application include Flask, Bootsrap, Jinja2, and SQLite.
Please see the [screenshots](https://github.com/cangir/theme-catalog#screenshots) section.


## JSON Endpoints
Endpoint | URL
------------ | -------------
Themes | /api/v1/themes
Categories | /api/v1/categories
Tags | /api/v1/tags
License Types | /api/v1/license-types
Theme Authors | /api/v1/theme-authors
Users | /api/v1/users


## Screenshots

### Home Page
![Home Page](https://github.com/cangir/theme-catalog/blob/master/screenshots/home.jpg)


### Login Page
![Login Page](https://github.com/cangir/theme-catalog/blob/master/screenshots/login.jpg)


### Category Page
![Category Page](https://github.com/cangir/theme-catalog/blob/master/screenshots/category.jpg)


### Tag Page
![Tag Page](https://github.com/cangir/theme-catalog/blob/master/screenshots/tag.jpg)


### License Types Page
![License Types Page](https://github.com/cangir/theme-catalog/blob/master/screenshots/license_type.jpg)


### Theme Authors Page
![Theme Authors Page](https://github.com/cangir/theme-catalog/blob/master/screenshots/theme_author.jpg)



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
7. If your command prompt does not start with vagrant after typing `vagrant ssh` then please try the `winpty vagrant ssh` on your Windows system.
8. The command line will now start with vagrant. Here get into to the shared /vagrant folder by command `cd /vagrant`.
9. Rename `config.py.example` file to `config.py` and adjust if you need any change.
10. Finally run `python3 manage.py runserver`.
11. Open `localhost:5000` in your web browser.

## Instructions without Vagrant
1. If you don't already have the latest version of python download it from the link in requirements.
2. Clone this repository.
3. Navigate to the `theme-catalog` folder in your bash interface.
4. Open bash terminal and install requirements with command `pip install -r requirements.txt`
5. Rename `config.py.example` file to `config.py` and adjust if you need any change.
6. Finally run `python manage.py runserver`.
7. Open `localhost:5000` in your web browser.

## Credits
First, let us take this opportunity to thank all the creative minds for their great products and hard work.

Name | URL | License
------------ | ------------- | -------------
Bootstrap | https://getbootstrap.com | [LICENSE](https://github.com/twbs/bootstrap/blob/master/LICENSE)
Tabler UI | https://github.com/tabler/tabler | [LICENSE](https://github.com/tabler/tabler/blob/master/LICENSE)
Font Awesome | https://fontawesome.com | [LICENSE](https://fontawesome.com/v4.7.0/license/)
Feather | https://feathericons.com/ | [LICENSE](https://github.com/feathericons/feather/blob/master/LICENSE)
jQuery | http://jquery.com | [LICENSE](https://github.com/jquery/jquery/blob/master/LICENSE.txt)
Simplelightbox | https://simplelightbox.com/ | [LICENSE](https://github.com/andreknieriem/simplelightbox/blob/master/LICENSE)
JQuery.Easing | https://github.com/gdsmith/jquery.easing/ | [LICENSE](https://github.com/gdsmith/jquery.easing/blob/master/LICENSE)
Waypoints | https://github.com/imakewebthings/waypoints/ | [LICENSE](https://github.com/imakewebthings/waypoints/blob/master/licenses.txt)

## Fonts & Images
- Google Fonts: http://www.google.com/fonts
- Startbootstrap: https://startbootstrap.com

## Release History
- 0.0.1 - Initial Release

## License
Licensed under [MIT](https://github.com/cangir/theme-catalog/blob/master/LICENSE) License.
