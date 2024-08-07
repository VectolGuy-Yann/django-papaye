# django\-papaye

This package runs a set of commands to help you use Transcrypt in Django.

It configures all you need inside you Django project, so you're all set to go.


* [django-papaye](#django\-papaye)
* [Description](#package-description)
* [Usage](#usage)
* [Possible Future Improvements](#possible-future-improvements)
* [Installation](#installation)
* [Testing](#testing)
* [Development/Contributing](#developmentcontributing)
* [History](#history)
* [Credits](#credits)
* [Licence](#licence)
* [Todo and Possible Future Improvements](#todopossible-future-improvements)
* [FAQ](#faq)


## Package Description
* [django\-papaye](#django\-papaye)

This package is configure your Django project in order to let you use Transcrypt the better way possible.

### Usage
* [django\-papaye](#django\-papaye)

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
#### From the Command Line

NOTE: Even better, configure a custom keyboard shortcut! I use control alt l.

run in a terminal: ```login```

If you need to reconfigure (run in a terminal) ```configure```

### Installation
* [lib\_work\_login](#lib\_work\_login)

Install the package with:
```pip3 install lib_work_login```

To install from source and develop:
```
git clone https://github.com/jfuruness/lib_work_login.git
cd lib_work_login
pip3 install wheel --upgrade
pip3 install -r requirements.txt --upgrade
python3 setup.py sdist bdist_wheel
python3 setup.py develop
```

### System Requirements
* [django\-papaye](#django\-papaye)

Must have linux. You can prob change easily to support other OSes, but not currently supported

## Testing
* [django\-papaye](#django\-papaye)

Run tests on install by doing:
```pip3 install lib_off_campus_housing_parser --force --install-option test```
This will install the package, force the command line arguments to be installed, and run the tests
NOTE: You might need sudo to install command line arguments when doing this

You can test the package if in development by moving/cd into the directory where setup.py is located and running:
```python3 setup.py test```

To test a specific submodule, cd into that submodule and run:
```pytest```

Note: I currently have not written any tests, since I have tried the program and checked it's output by hand so I know that it works. I know that this is not sufficient, but no one is going to use this thing but me so whatevs.

## Development/Contributing
* [django\-papaye](#django\-papaye)

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request
6. Email me at jfuruness@gmail.com because I do not check those messages often

## History
* [django\-papaye](#django\-papaye)
   * 0.1.3 - Added a link to Github 
   * 0.1.2 - Added README.md 
   * 0.1.1 - Changes to include necessary files and folders

## Credits
* [django\-papaye](#django\-papaye)

https://stackoverflow.com/a/38493278/8903959

## License
* [django\-papaye](#django\-papaye)

BSD License

## TODO/Possible Future Improvements
* [django\-papaye](#django\-papaye)
    * Actual testing
    * Cross platform compatibility

## FAQ
* [django\-papaye](#django\-papaye)

Q: Have you ever opened a 'papaye' 🥭

A1: Yes and it smells very bad! => like using Transcrypt inside Django at first

A2: But then you start to taste it and now you are getting in love with it. Guess what, same for Transcrypt inside Django

P.S.: Fruits 4 life 🔆🌱🥭💪!