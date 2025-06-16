di = {}

di["name"] = "John"
di["age"] = 30
di["city"] = "New York"

print(di["name"])
print(di["age"])
print(di["city"])

for key in di:
    print(key, di[key])

for key, value in di.items():
    print(key, value)

print(di.get("name"))
print(di.get("address"))

di.pop("city")
print(di)

di.popitem()
print(di)

di.clear()
print(di)   

print(len(di))

di1 = {"name": "John", "age": 30, "city": "New York"}
di2 = {"code": "1234", "city": "London"}

print(di1 == di2)
print({**di1, **di2})