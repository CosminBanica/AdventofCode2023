# Advent of code 2023
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

### Usage
```python main.py <day> [-t|--test] [-g|--generate] [-n|--name <name>] [-h|--help]```

#### Explanation
* ```<day>``` is the day to run
* ```-t``` or ```--test``` runs the small test input instead of the big input
* ```-g``` or ```--generate``` generates files for the day, if they don't exist
* ```-n``` or ```--name``` sets the name of the problem for the day, in the newly generated files
* ```-h``` or ```--help``` shows the help message

#### Examples
* ```python main.py 1 -g -n "Trebuchet?!"```
* ```python main.py 4 -t```

## Development
### Pylint:
```pylint main.py config/ src/```

### Black formatter:
```black main.py config/ src/```

### Possible improvements
* A lot of problems have a map as input; I should write a map/grid class to make it easier to work with