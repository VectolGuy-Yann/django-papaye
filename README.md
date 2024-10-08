# django-papaye

This package helps you use Transcrypt in Django.

It gives you new terminal commands and configures all you need inside any Django project, so you're all set to go.

* [Description](#package-description)
* [Usage](#usage)
* [Installation](#installation)
* [System Requirements](#system-requirements)
* [Tutorials](#tutorials)
* [Development/Contributing](#developmentcontributing)
* [History](#history)
* [Donations](#donations)
* [Licence](#licence)
* [FAQ](#faq)

## [Description](#package-description)

django-papaye 🥭 package configures your Django project in order to let you use Transcrypt into it the better way as
possible.

## [Usage](#usage)

Assuming you already created a Django project at '/path/to/your/django/project'
(if not please do so)

Before installing django-papaye you MUST first:

1) Install pyenv: https://github.com/pyenv/pyenv

2) Install a python3.9 version via pyenv:
```bash
pyenv install 3.9.19
```

3) In a new terminal tab, create a specific python virtual environment via pyenv:
```bash
cd /path/to/your/django/project  # go to you django project root folder (same folder where manage.py is)

pyenv shell 3.9.19  # switches to this specific version of python for this terminal tab until it's closed

python3 --version  # it should print out 'Python 3.9.19'

python3 -m venv venv-3.9

source venv-3.9/bin/activate  # to activate your venv-3.9
```

4) Install django-papaye 🥭:
```bash
pip install django-papaye
```

5) Then configure your Django/Transcrypt environment by executing this command:
```bash
configure
```

6) Add a "load static" statement at top of base.html, then add a "script" calling your code transpiled from Python to JavaScript just before the end of body tag:
```html
{% load static %}

<body>
    ...

    {# Transcrypted from .py to .js #}
    <script src="{% static 'js/main.js' %}"></script>
</body>
```

7) Start the Transcrypt Python2JS development server:
```bash
npm run devDesktop
```

8) Add the following code to t_logic/main.py:
```python
print('Hello from Transcrypt and django-papaye!')
```

9) Reload your browser with ctrl+shift+r, then open "inspect", then go "Console" tab and you should see the content of your print coded at previous step.

Your all good to go now!

## [Installation](#installation)

Install the package with:
```pip install django-papaye```

## [System Requirements](#system-requirements)

django-papaye 🥭 should work fine on Unix systems (Linux, MacOS).  

For Windows users, if you follow my guideline, it should be fine too.  
But if you encounter any issues, please leave me a message and I'll do my best to help you ASAP.

## [Tutorials](#Tutorials)

#### Udemy
We have a complete course on django-papaye 🥭 on [Udemy](https://www.udemy.com/course/devenir-developpeur-web-fullstack-en-100-python/?couponCode=E2827E35C7B7195FAD01):  
https://www.udemy.com/course/devenir-developpeur-web-fullstack-en-100-python/?couponCode=E2827E35C7B7195FAD01  

![](django_papaye/src/static/Formation_python.png)  

#### YouTube
Also if you want to check some videos and tutorials on django-papaye 🥭, you can watch our [YouTube playlist](https://www.youtube.com/playlist?list=PLk4FIlI8V5EJiAC9rCjsy13xoSmds0S51):  
https://www.youtube.com/playlist?list=PLk4FIlI8V5EJiAC9rCjsy13xoSmds0S51 

## [Development/Contributing](#developmentcontributing)

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request
6. Email me at guyyann.vectol@gmail.com because I do not check those messages often

## [History](#history)

    * 0.1.17 - New fix on README.md
    * 0.1.16 - Fix on README.md
    * 0.1.15 - Added Udemy and YouTube links on README.md
    * 0.1.14 - New quick fix on README.md
    * 0.1.13 - Quick fix on README.md
    * 0.1.12 - Changes on README.md
    * 0.1.11 - Added import main.js in base.html on README.md
    * 0.1.10 - New changes on README.md
    * 0.1.9 - New changes on README.md
    * 0.1.8 - Changes on README.md
    * 0.1.7 - Enabled README.md for Pypi
    * 0.1.6 - Add a donation link inside README.md
    * 0.1.5 - Another quick fix on README.md
    * 0.1.4 - Quick fix on README.md
    * 0.1.3 - Added a link to Github
    * 0.1.2 - Added README.md
    * 0.1.1 - Changes to include necessary files and folders

## [Donations](#donations)

If you want to help us, don't hesitate with any donation :)  
https://www.paypal.com/donate/?hosted_button_id=8BWT6CHREL5CE

## [Licence](#licence)

BSD License

Copyright 2024 qlapp

Contributors: Guy-Yann VECTOL

Citation: "As-tu déjà ouvert une papaye? Au premier abord ça pue. Mais ensuite tu y goutes et tu te rends compte que
c'est super bon ;)"

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following
   disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following
   disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products
   derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES,
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## [FAQ](#faq)

Q: Why this name: django-papaye ?

A1: Have you ever opened a 'papaye' 🥭? 

It smells very bad! => like using Transcrypt inside Django at first

But then you start to taste it and now you are getting in love with it. Guess what, same for Transcrypt inside
Django

P.S.: Fruits 4 life 🔆🌱🥭💪!
