# Historia

Historia is a software born to allow communities to create portal about cities history.
The system is based on documents.

## Installation

    $ git clone git@github.com:OpenCode/historia.git
    $ cd historia
    $ virtualenv -p python3 venv
    $ source venv/bin/activate
    (venv)$ python3 -m pip install -r requirements.txt
    (venv)$ cd historia
    (venv)$ python3 manage.py createsuperuser

## Configuration

If you use the standard Historia theme, you can configure parameters in admin area. Go to <YOUR_URL>/admin/album/siteinfo/ and use the base parameters to personalize the site.

| Key | Value | HTML Content |
| --- | --- | --- |
| **about_image** | External link for image in about page |
| **about** | | About page HTML content
| **keywords** | Keywords for web page header and SEO
| **intro** | Motto on main page
| **description** | Description for web page header and SEO
| **title** | Project title
| **city** | City name

## Run

    $ python3 historia/manage.py runserver

## Development

    $ python manage.py makemigrations album
    $ python manage.py migrate
