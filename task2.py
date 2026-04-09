import json

# 5
users = [
    {"name": "Ali", "age": 20},
    {"name": "Vali", "age": 25},
    {"name": "Hasan", "age": 17}
]

with open("users.json", "w") as f:
    json.dump(users, f, indent=4)

with open("users.json") as f:
    data = json.load(f)

print(data)

# 6
nested = '''
{
  "user": {
    "name": "Ali",
    "address": {
      "city": "Tashkent",
      "zip": 100000
    }
  }
}
'''
obj = json.loads(nested)
print(obj["user"]["address"]["city"])

# 7
simple = '{"name": "Ali", "age": 20}'
obj = json.loads(simple)
obj["is_student"] = True

# 8
obj["age"] = 21
print(obj)

# 9
response = '''
{
  "status": "success",
  "data": [
    {"id": 1, "title": "Post 1"},
    {"id": 2, "title": "Post 2"}
  ]
}
'''

res = json.loads(response)
for post in res["data"]:
    print(post["title"])
