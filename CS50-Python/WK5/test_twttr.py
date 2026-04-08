from twttr import shorten

def main():
    test_shorten()


def test_shorten():
    assert shorten("tatto") == "ttt"
    assert shorten("APPLE") == "PPL"
    assert shorten("123!") == "123!"
