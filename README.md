# Python-Executioner
Python framework to convert python objects to CLI applications fast.

## Getting Started
If you want to download a local copy of the project, clone it and move the ```executioner``` folder to your python project.

## Prerequisites
This project has been tested with and currently requires python 3 to run.  Instructions to install it can be found on python's [official website](https://www.python.org).

## Installing
Installing is simple by using pip:
```pip install executioner```
(**NOTE: Make sure to use the version of pip that matches the version of python you intended to use**)

To demonstrate how the project works, take for example a simple Calculator classwhich is in calculator.py:
```py
import executioner
class Calculator(object):
  
    def __init__(self):
        self.double_param = "int"

    def double(self, number):
        return 2 * number

if __name__ == '__main__':
    executioner.Execute(Calculator())
```
If you were to take this file and do the following: 
```python3 calculator.py double 20```
You will see ```40``` be the output.

You may see that we defined the property ```self.double_param``` in the above example.  In order for executioner to properly parse the CLI args, you need to specify the parameter for each function in the object's ```py __init__``` method asfunc_param = "param" where func is the name of the function for which you are defining the param for.  The types of param that are accepted are ```int, float, string, and list:type (where type can be any of the first 3 types).

## Built With
* Standard python and full advantage of the ```getattr()``` function


## Contributing
Please see CONTRIBUTING.md for contribution guidelines.

## Authors
* Tom Orth (atf1999)

## License
This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgements
* Inspired by [python-fire](https://www.github.com/google/python-fire), which I found to be rather slow when using it
