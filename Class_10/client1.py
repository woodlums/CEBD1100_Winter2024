import requests

# https://dummyjson.com/todos

response = requests.get("https://dummyjson.com/todos")

#print(response)
#print(response.json())


my_todos = response.json()["todos"]

for todo in my_todos:
    print(todo)