import json

# 1
data = '{"name": "Ali", "age": 20, "city": "Tashkent"}'
obj = json.loads(data)
print(obj["name"], obj["city"])

# 2
user = {
    "username": "coder123",
    "email": "coder@mail.com",
    "is_active": True
}
print(json.dumps(user, indent=4))

# 3
data = '''
[
    {"name": "Ali", "age": 20},
    {"name": "Vali", "age": 25},
    {"name": "Hasan", "age": 17}
]
'''
users = json.loads(data)

for u in users:
    if u["age"] > 18:
        print(u["name"])

# 4
for u in users:
    if u["name"] == "Vali":
        print(u)
