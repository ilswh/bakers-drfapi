# [BAKERS drf api](https://bakers-drfapi-cfb949bb8921.herokuapp.com/)

More extensive [README](https://github.com/ilswh/bakers/blob/main/README.md) can be found in the bakers repository.
<hr>

## Agile Development Process

[Follow the agile development process here.](https://github.com/ilswh/bakers/blob/main/README.md#agile-development-process)


## Database Design

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models.
Understanding the relationships between different tables can save time later in the project.
So I tried to generate one with DBeaver using my Elephant SQL details, but unforunatley without success.


## User Stories

[Here you can see the admins user stories.](https://github.com/ilswh/bakers/blob/main/README.md#site-admin)
<br>
More extensive [User Stories](https://github.com/ilswh/bakers/blob/main/README.md#user-stories) can be found in the bakers repository.


## User Stories Testing

[Here you can see the user stories testing](https://github.com/ilswh/bakers/blob/main/README.md#user-stories)


## Python Testing 

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.
[See results from python validation, here.](https://github.com/ilswh/bakers/blob/main/TESTING.md#python)
<br>
<br>
More extensive [TESTING](https://github.com/ilswh/bakers/blob/main/TESTING.md) can be found in the bakers repository.


## Python Packages

asgiref==3.7.2
<br>
cloudinary==1.39.0
<br>
dj-database-url==0.5.0
<br>
dj-rest-auth==2.1.9
<br>
Django==3.2.25
<br>
django-allauth==0.44.0
<br>
django-cloudinary-storage==0.3.0
<br>
django-cors-headers==4.3.1
<br>
django-filter==23.5
<br>
djangorestframework==3.14.0
<br>
djangorestframework-simplejwt==5.3.1
<br>
gunicorn==21.2.0
<br>
oauthlib==3.2.2
<br>
pillow==10.2.0
<br>
psycopg2==2.9.9
<br>
PyJWT==2.8.0
<br>
python3-openid==3.2.0
<br>
pytz==2024.1
<br>
requests-oauthlib==1.3.1
<br>
sqlparse==0.4.4
<br>
<hr>

## Deployment

Code Institute has provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser.
This is to improve the accessibility of the project to others.

The live deployed application can be found deployed on [Heroku](https://play-in-python-5451a263c67c.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- Further down, to support dependencies, select **Add Buildpack**.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: node index.js > Procfile`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The frontend terminal should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/ilswh/play-in-python) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/ilswh/play-in-python.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/ilswh/play-in-python)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/ilswh/play-in-python)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

Use this space to discuss any differences between the local version you've developed, and the live deployment site on Heroku.


## Bugs

[Backend bugs are documented here.](https://github.com/ilswh/bakers/blob/main/TESTING.md#backend)


## Tools & Technologies Used

- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [GitHub Pages](https://pages.github.com) used for hosting the deployed front-end site.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [ElephantSQL](https://www.elephantsql.com) used as the Postgres database.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [Cloudinary](https://cloudinary.com) used for online static file storage.


## Credits

When building bakers drf api I followed the walkalong Django REST Frameworks from Code Institute.
When building the contact feature I took inspiration from my mentors project and when building the bookmark feature I took inspiration from one of my mentors students. They are linked below, under content.

### Content

[Backend credits can be seen here.](https://github.com/ilswh/bakers/blob/main/README.md#content)

### Acknowledgements

- I would like to thank my Code Institute mentor, [Gareth McGirr](https://github.com/Gareth-McGirr) for his support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) tutor team for their tremendous assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and imposter syndrome.
- I would like to thank my family, for believing in me, and allowing me to make this transition into software development.
<br>