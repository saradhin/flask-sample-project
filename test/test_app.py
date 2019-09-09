from app import app 
import pytest

def test_get_store():
    assert app.get_store('mystore')['name'] == "mystore"
