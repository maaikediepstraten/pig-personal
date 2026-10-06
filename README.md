# Pig Latin Demo

## Goal

This is a Pig Latin converter that demonstrates the basic structure of a Python package.

## Installation

### For regular users

If you just want to use this project, simply install it with:

```shell
python -m pip install git+https://github.com/LFKoning/pig-latin
```

This will install the package and all of its dependencies into your current Python
environment.

### For developers

If you want to help develop this project, clone the repository from GitHub:

```shell
git clone https://github.com/LFKoning/pig-latin
```

Then install the package and its development dependencies:

```shell
python -m pip install -e .[dev]
```

## Usage

To use this package from the command line type:

```shell
pig-latin "Hello World!"
```

Or import it into your own Python project like so:

```python
>>> from pig_latin.latin import pig_latin
>>> pig_latin("Hello World!")
```
