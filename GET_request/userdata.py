import requests
import json

base_url = "https://jsonplaceholder.typicode.com"
users = "/users"
posts = "/posts"
comments = "/comments"

# send Get request
def get_request():
    '''To validate the request is giving positive response'''

    response = requests.get(base_url+users)
    # assert response.status_code == 200, "Status code is not 200. Rather found : " + str(response.status_code)
    return response.status_code == 200

def get_user():
    '''To the get details of the user for Delphine'''

    response = requests.get(base_url + users)
    for Users in response.json():
        if Users['id'] == 9:
            return Users['username'] == "Delphine"

def get_posts():
    '''To get the posts return by the user Delphine'''

    result = requests.get(base_url+posts)
    for post in result.json():
        if post['userId'] == 9:
            return post['userId']

def get_comments():
    '''To get the cpmments from the post with any id'''

    comment_result = requests.get(base_url+comments)
    for comment in comment_result.json():
        if comment['postId'] == 81:
            return comment['postId']

def get_emailId():
    '''To validate the emailID'''

    response = requests.get(base_url+posts+'81/comments')
    data = response.json()
    emai_id = [x['email'] for x in data['name']]
    return emai_id