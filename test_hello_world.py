def hello_world():
    return "Hello, World!"

def test_hello_world():
    assert "Hello, World!", hello_world()

def test_fail():
    assert False
