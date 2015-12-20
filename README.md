![Python Thursday Logo](docs/images/python-thursday-logo.png)
# python-thursday-adventure-2
The sequel to the 2015 favorite, Python Thursday Adventure

![Travis-CI](https://travis-ci.org/jamalhansen/python-thursday-adventure-2.svg?branch=master)

## Dependencies
Dependencies are managed for this project with pip.  Basic proceedures for installing and saving dependencies is below, additional information can be found in the [pip documentation](https://pip.readthedocs.org/en/1.1/requirements.html#).

### Installing

The dependencies for this project are stored in the file requirements.txt.  To install these dependencies into your environment use the command below.

```pip install -r requirements.txt```

### Saving

If you have added new dependencies to the project, please add them to the requirements.txt file. You can do this with ```pip freeze > requirements.txt``` which will save your current requirements to the requirements.txt file.

## Testing

### Test setup

Before running tests you will need to use pip to install the Python Adventure in editable mode.  You can do this by typing the following from the root directory of the project ```pip install -e .```

### Running unit tests

Running unit tests can be achieved by running pytest from the command line and passing it the location of the tests to run.  This can be done with the following command run from the root folder of the project ```python -m pytest test/```

Running your tests should looks something similar to this:

![Pytest example](docs/images/pytest-example.jpg)
