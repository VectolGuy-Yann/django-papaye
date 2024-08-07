# django-papaye

This package installs helps help you use Transcrypt in Django.

It gives you new terminal commands and configures all you need inside any Django project, so you're all set to go.

* [Description](#package-description)
* [Usage](#usage)
* [Installation](#installation)
* [System Requirements](#system-requirements)
* [Testing](#testing)
* [Development/Contributing](#developmentcontributing)
* [History](#history)
* [Donations](#donations)
* [Licence](#licence)
* [Todo and Possible Future Improvements](#todopossible-future-improvements)
* [FAQ](#faq)

## Package Description
* [Description](#package-description)

django-papaye package configures your Django project in order to let you use Transcrypt into it the better way as
possible.

### Usage
* [Usage](#usage)

#### In a Script - purely for development

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

4) Install django-papaye

```bash
pip install django-papaye
```

5) Then configure your django transcrypt environment by executing this command:

```bash
configure
```

Your all good to go now!

### Installation
* [Installation](#installation)

Install the package with:
```pip install django-papaye```

### System Requirements
* [System Requirements](#system-requirements)

Must have linux. You can prob change easily to support other OSes, but not currently supported

## Testing
* [Testing](#testing)

Run tests on install by doing:
```pip3 install lib_off_campus_housing_parser --force --install-option test```
This will install the package, force the command line arguments to be installed, and run the tests
NOTE: You might need sudo to install command line arguments when doing this

You can test the package if in development by moving/cd into the directory where setup.py is located and running:
```python3 setup.py test```

To test a specific submodule, cd into that submodule and run:
```pytest```

Note: I currently have not written any tests, since I have tried the program and checked it's output by hand so I know
that it works. I know that this is not sufficient, but no one is going to use this thing but me so whatevs.

## Development/Contributing
* [Development/Contributing](#developmentcontributing)

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request
6. Email me at guyyann.vectol@gmail.com because I do not check those messages often

## History
* [History](#history)

    * 0.1.9 - New changes on README.md
    * 0.1.8 - Changes on README.md
    * 0.1.7 - Enabled README.md for Pypi
    * 0.1.6 - Add a donation link inside README.md
    * 0.1.5 - Another quick fix on README.md
    * 0.1.4 - Quick fix on README.md
    * 0.1.3 - Added a link to Github
    * 0.1.2 - Added README.md
    * 0.1.1 - Changes to include necessary files and folders

## Donations
* [Donations](#donations)

https://www.paypal.com/donate/?hosted_button_id=8BWT6CHREL5CE

## License
* [Licence](#licence)

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

## TODO/Possible Future Improvements
* [Todo and Possible Future Improvements](#todopossible-future-improvements)

    * Actual testing
    * Cross platform compatibility

## FAQ
* [FAQ](#faq)

Q: Why this name: django-papaye ?

A1: Have you ever opened a 'papaye' 🥭? 

It smells very bad! => like using Transcrypt inside Django at first

But then you start to taste it and now you are getting in love with it. Guess what, same for Transcrypt inside
Django

P.S.: Fruits 4 life 🔆🌱🥭💪!
