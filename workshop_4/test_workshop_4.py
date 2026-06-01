import requests
import pytest
import numpy as np

@pytest.fixture
def api_client():
	session = requests.Session()
	yield session
	session.close()

'''
Task 1
- Perform a GET request to https://api.zippopotam.us/us/90007
- Check that the response status code equals to 200
- Check that the value of the response header 'Content-Type' is 'application/json'
- Check that the response body element 'country' has a value equal to 'United States'
- Check that the response body element 'places' is a list and has a length of 1 (only one place corresponds to the US zip code 90007)
- Check that the first 'place name' element in the list of places has a value equal to 'Los Angeles'
'''

def test_task1(api_client):
	response = requests.get("https://api.zippopotam.us/us/90007")
	assert response.status_code == 200
	assert response.headers.get('Content-Type') == 'application/json'
	assert response.json().get('country') == 'United States'
	s =  response.json().get('places')
	assert len(s) == 1
	assert type(s) == list
	
    
	first = s[0].get("place name")
	assert first == 'Los Angeles'



	




'''
Task 2
- Perform 10 GET requests sequentially to https://jsonplaceholder.typicode.com/posts
- Check that all response status codes equal to 200
- Check that, on average, the server responds less than 300 ms.
- Check that, percentile 95, the server responds less than 400 ms.
'''
def test_task2(api_client):
	time = []
	for i in range(10):
		response = requests.get("https://jsonplaceholder.typicode.com/posts")
		assert response.status_code == 200
		time.append(response.elapsed.total_seconds())
	
	avg = sum(time) * 1000 / 10
	assert avg < 300

	p95 = np.percentile(time, 95)
	assert p95 < 400
	








'''
Task 3
- Perform a GET request to https://jsonplaceholder.typicode.com/posts/1
- Check if the response code is 200
- Check if the response follows the expected JSON schema structure. 
- The schema should match the expected_schema format
DO NOT USE ANY EXTERNAL LIBRARIES
Hint: use isinstance(variable, type) function for this
'''
def test_task3(api_client):
	expected_schema = {
        "userId": int,
        "id": int,
        "title": str,
        "body": str
    }
    #you code
	response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
	assert response.status_code == 200
	assert len(response.json()) == len(expected_schema)
	assert isinstance(response.json().get("userId"), expected_schema["userId"])
	assert isinstance(response.json().get("id"), expected_schema["id"])
	assert isinstance(response.json().get("title"), expected_schema["title"])
	assert isinstance(response.json().get("body"), expected_schema["body"])






'''
Task 4
- Perform a PATCH update to https://jsonplaceholder.typicode.com/users/1
to change the email of the user id 1 to "cs364@cs.science.cmu.ac.th"
- Check that response status code is okay (200)
- Check that the returned data shows the new email for the user.
'''
def test_task4(api_client):
	response = requests.patch("https://jsonplaceholder.typicode.com/users/1", data={"email": "cs364@cs.science.cmu.ac.th"})
	assert response.status_code == 200
	assert response.json().get("email") == "cs364@cs.science.cmu.ac.th"








'''
Task 5
- Use the username and password from https://dummyjson.com/users (any user)
- Perform a POST request to https://dummyjson.com/auth/login 
and pass the username and password object to the request
- Check that the response status code is okay
- Check that the server sends 'accessToken' back
- Perform a GET request with Authorization header with accessToken above to https://dummyjson.com/auth/me
- Check that the response code is 200
- Check that the returned user is the correct one (check if usernames are the same).
- Perform the same request but with incorrect accessToken
- Check that the response code is 401 (unauthorized) and the response's json object 'message' field says "Invalid/Expired Token!"
'''
def test_task5(api_client):
	response = requests.get("https://dummyjson.com/users/1")

	
	data = {
		"username": response.json().get("username"),
		"password": response.json().get("password"),
	}

	loged_in = requests.post("https://dummyjson.com/auth/login", data)
	assert loged_in.status_code == 200
	assert loged_in.json().get("accessToken") is not None

	headers = {
		"Content-Type": "application/json",
		"Authorization": "Bearer " + loged_in.json().get("accessToken")
	}

	res = requests.get("https://dummyjson.com/auth/me", headers=headers)
	assert res.status_code == 200
	assert res.json().get("username") == data["username"]

	res_err = requests.get("https://dummyjson.com/auth/me", headers={"Authorization": "esdgfhfdsfgfhjtrsdfgj"})
	assert res_err.status_code == 401
	assert  res_err.json().get('message') == "Invalid/Expired Token!"



