[![Build Status](https://drone.io/bitbucket.org/sam_kinard/msg-parse/status.png)](https://drone.io/bitbucket.org/sam_kinard/msg-parse/latest)

# Overview

MsgParser is a simple python package that can build json metadata about a chat message. 

### Example

    I am @sam and here is a link: https://www.simple.com have a nice day (smiley).

```json
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

Continuous Integration is hosted in [drone.io](https://drone.io/bitbucket.org/sam_kinard/msg-parse)

### Usage

It's easy to try out MsgParser in the python console:

```shell
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

See [test_msg_parser.py](https://bitbucket.org/sam_kinard/msg-parse/src/7bebe865985b5836f9a9ce269c7e93eea6feb08c/test_msg_parser.py?at=master&fileviewer=file-view-default) for more interesting examples.    