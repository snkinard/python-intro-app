[![Build Status](https://drone.io/bitbucket.org/sam_kinard/msg-parse/status.png)](https://drone.io/bitbucket.org/sam_kinard/msg-parse/latest)

# Contents

# Overview

MsgParser is a simple python package that can build json metadata about a chat message. 

### Example

    I am @sam and here is a link: https://www.simple.com have a nice day (smiley).

```
{
  "raw": "I am @sam and here is a link: https://www.simple.com have a nice day (smiley).", 
  "emoticons": ["smiley"], 
  "links": [{
    "url": "https://www.simple.com", 
    "title": "Simple | Online Banking With Automatic Budgeting & Savings"
  }],     
  "mentions": ["sam"]
}
```

# Setup and Usage

This software was developed in OS X 10.11.3 with Python 2.7.10.

### OS X Development Environment Setup

This guide assumes that you have pulled the source code down onto your local machine.

Add the code directory to your python path

    $ export PYTHONPATH=$PYTHONPATH:/Users/sam/code/msg-parse

Install dependencies [pytest](http://pytest.org/latest/) and [mechanize](http://wwwsearch.sourceforge.net/mechanize/) using [easy_install](https://pythonhosted.org/setuptools/easy_install.html)

    $ easy_install -U pytest
    $ easy_install -U mechanize

### Running the tests

To run the tests locally simply run [pytest](http://pytest.org/latest/) in the code directory

    $ py.test

### Usage

It's easy to try out MsgParser in the python console:

```
$ cd /path/to/code/directory
$ python
Python 2.7.10 (default, Oct 23 2015, 18:05:06)
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from msg_parser import MsgParser
>>> parse = MsgParser()
>>> parse.parse_message("Hello, @sam!")
>>> parse.to_json_str()
'{"raw": "Hello, @sam!", "emoticons": [], "links": [], "mentions": ["sam"]}'
```
    

### TODO
Stuff I want to get done before I submit this. Probably can't get to all of it

* ~~manually test in python console~~
* ~~mechanize error handling~~
    * ~~code~~
    * ~~unit test~~
    * ~~manual verify~~
* ~~refactor~~
* ~~pep8~~
    * ~~run~~
    * ~~fix problems~~
* Readme Docs
    * Intro
    * OSX setup instructions
    * python terminal example
    * How to Run Tests
    * drone.io
    * any extra thoughts about what could be done next
* Method Docs
    * methods in MsgParser
    * any other random comments to explain weird stuff
* pylint