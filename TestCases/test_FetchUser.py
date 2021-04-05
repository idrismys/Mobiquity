import re

from GET_request import userdata


def test_status():
    '''To fetch the user Delphine details and validate if Delphine is the user'''

    assert userdata.get_request()


def test_user():
    '''To get the user details'''

    assert userdata.get_user()


def test_posts():
    '''To get the posts return by the user'''

    assert userdata.get_posts()


def test_comments():
    '''To get the comments from the post'''

    assert userdata.get_comments()


def test_validate_emailid():
    regex = '^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$'
    if (re.search(regex, userdata.get_emailId())):
        return True
    else:
        return False
