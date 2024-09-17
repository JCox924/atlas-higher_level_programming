# Python-Heritance

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

**Python-Heritance** is a Python package designed to simplify and enhance the usage of inheritance in object-oriented
programming. This project aims to provide utilities that facilitate common inheritance patterns and best practices.

## Installation

You can install Python-Heritance via pip:

```bash
pip install python-heritance
```

## Usage

Here's a simple example to get you started:

```python
from python_heritance import BaseClass, DerivedClass


# Define a base class
class Animal(BaseClass):
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")


# Define a derived class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


# Create an instance of the derived class
dog = Dog(name="Buddy")
print(dog.speak())
```

## Examples

Below are some more detailed examples:

### Example 1: Abstract Classes

```python
from python_heritance import AbstractBaseClass


class MyAbstractClass(AbstractBaseClass):
    def do_something(self):
        pass


class MyConcreteClass(MyAbstractClass):
    def do_something(self):
        print("Doing something!")


instance = MyConcreteClass()
instance.do_something()
```

### Example 2: Multiple Inheritance

```python
from python_heritance import BaseClass


class Base1(BaseClass):
    def talk(self):
        print("Base1 talking")


class Base2(BaseClass):
    def talk(self):
        print("Base2 talking")


class Derived(Base1, Base2):
    pass


derived_instance = Derived()
derived_instance.talk()  # Resolves to Base1's talk method
```

## Contributing

We welcome contributions from the community! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes.
4. Commit your changes: `git commit -m 'Add some feature'`
5. Push to the branch: `git push origin feature-branch`
6. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.