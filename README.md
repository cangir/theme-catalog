## Introduction
A simple web application that provides list of free web themes within a variety of categories and tags. 
Authenticated users have the ability to post, edit, and delete their own items.

## Preview
![Theme Catalog preview](https://github.com/cangir/theme-catalog/blob/master/screenshots/preview.gif)

**[View Demo](https://cleanbootstrap.com)**

## Project Overview
This is the fourth project for the Udacity Full Stack Nanodegree. This project allows users to perform Create, Read, Update, and Delete operations.
Logging in is not required in order to read the categories or items uploaded. But, users need to log in to access CRUD operations such as adding, editing and removing items.
This program uses third-party auth with Facebook.

Some of the technologies used to build this application include Flask, Bootsrap, Jinja2, and SQLite.
Please see the [screenshots](https://github.com/cangir/theme-catalog#screenshots) section.

**Please note that:** 
1. *[The Demo](https://cleanbootstrap.com) doesn't have authentication features.*
2. *In order to see demo pages, you need to run the project.*


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


### Theme Add Page
![Theme Add Page](https://github.com/cangir/theme-catalog/blob/master/screenshots/theme_add.jpg)


### Theme Single Page
![Theme Single Page](https://github.com/cangir/theme-catalog/blob/master/screenshots/theme_single.jpg)


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

## Instructions
You can run the project whether installing and using vagrant which is optional or you can install requirements.txt and run the project in your local computer. In both ways **the database file and the demo content** is not shipped with the repository. Once the project runs, *the database* and the */static/uploads* folder will be created automatically.


### Install on virtual server using Vagrant
1. If you don't already have the latest version of python download it from the link in requirements.
2. Download and install Vagrant and VirtualBox.
3. Clone this repository.
4. Navigate to the `theme-catalog` folder in your bash interface.
5. Open bash terminal and launch the virtual machine with command `vagrant up`. At first time normally it takes about 10-15 minutes to build vagrant. Please be patient.
6. Once Vagrant installs necessary files use `vagrant ssh` to continue.
7. If your command prompt does not start with vagrant after typing `vagrant ssh` then please try the `winpty vagrant ssh` on your Windows system.
8. The command line will now start with vagrant. Here get into to the shared /vagrant folder by command `cd /vagrant`.
9. Rename `config.py.example` file to `config.py`.
10. Open `config.py` file. Set Facebook Api credentials and change any settings depending on your needs.
11. Run `python3 manage.py runserver`.
12. Open `localhost:5000` in your web browser.

### Manual installation on local machine (without Vagrant)
1. If you don't already have the latest version of python download it from the link in requirements.
2. Clone this repository.
3. Navigate to the `theme-catalog` folder in your bash interface.
4. Open bash terminal and install requirements with command `pip install -r requirements.txt`
5. Rename `config.py.example` file to `config.py`.
6. Open `config.py` file. Set Facebook Api credentials and change any settings depending on your needs.
7. Run `python manage.py runserver`.
8. Open `localhost:5000` in your web browser.


## Credits
First, let us take this opportunity to thank all the creative minds for their great products and hard work.

Name | License
------------ | -------------
[jQuery](https://github.com/jquery/jquery) | [LICENSE](https://github.com/jquery/jquery/blob/master/LICENSE.txt)
[Bootstrap](https://github.com/twbs/bootstrap) | [LICENSE](https://github.com/twbs/bootstrap/blob/master/LICENSE)
[Tabler UI](https://github.com/tabler/tabler) | [LICENSE](https://github.com/tabler/tabler/blob/master/LICENSE)
[Easing](https://github.com/gdsmith/jquery.easing/) | [LICENSE](https://github.com/gdsmith/jquery.easing/blob/master/LICENSE)
[EasyMDE](https://github.com/Ionaru/easy-markdown-editor) | [LICENSE](https://github.com/Ionaru/easy-markdown-editor/blob/master/LICENSE)
[Font Awesome 4.7.0](https://fontawesome.com/v4.7.0) | [LICENSE](/license/)
[Feather](https://github.com/feathericons/feather) | [LICENSE](https://github.com/feathericons/feather/blob/master/LICENSE)
[GDPR Cookie](https://github.com/thany/gdpr-cookie) | [LICENSE](https://github.com/thany/gdpr-cookie/blob/HEAD/LICENSE.md)
[Selectize](https://github.com/selectize/selectize.js) | [LICENSE](https://github.com/selectize/selectize.js/blob/master/LICENSE)
[Waypoints](https://github.com/imakewebthings/waypoints) | [LICENSE](https://github.com/imakewebthings/waypoints/blob/master/licenses.txt)

## Fonts & Images
- Google Fonts: http://www.google.com/fonts
- Startbootstrap: https://startbootstrap.com

## Release History
- 0.0.1 - Initial Release

## License
Licensed under [MIT](https://github.com/cangir/theme-catalog/blob/master/LICENSE) License.
