from re import S
from bbquote.api import quote

def test_quote():
    result = quote()
    assert type(result) == str
    assert len(result) > 0
