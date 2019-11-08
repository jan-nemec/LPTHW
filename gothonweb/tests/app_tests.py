from nose.tools import *
from app import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    
    rv = web.get('/hello', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"Fill Out This Form", rv.data)

    # 404 Not Found response - the page actually doesn't exists
    rv = web.get('/about', follow_redirects=True)
    assert_equal(rv.status_code, 404)    

    # The flask framework has a very simple API for processing requests, which
    # looks like this:
    data = {'name': 'Zed', 'greet': 'Hola'}
    rv = web.post('/hello', follow_redirects=True, data=data)
    # You can send a POST request using the post() method, and then give it the
    # form data as a dict.

    assert_in(b"Zed", rv.data)
    assert_in(b"Hola", rv.data)
