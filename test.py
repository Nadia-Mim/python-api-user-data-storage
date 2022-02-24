import requests

BASE = "http://127.0.0.1:5000/"

print("parent test")
# inserts user data to parent database
data = [{"firstName": "Nadia", "lastName": "Tasnim", "street": "Senpara Parbata",
         "city": "Dhaka", "state": "Bangladesh", "zipCode": 1216},
        {"firstName": "Sadia", "lastName": "Anjum", "street": "Mirpur 10",
         "city": "Dhaka", "state": "Bangladesh", "zipCode": 1216},
        {"firstName": "Salma", "lastName": "Alam", "street": "Mohakhali",
         "city": "Dhaka", "state": "Bangladesh", "zipCode": 1206}]

print("parent user data input test")
for i in range(len(data)):
    response = requests.post(BASE + "parent/" + str(i+1), data[i])
    print(response.json())

input()

print("parent user data delete test")

# deletes user data of the given id
response = requests.delete(BASE + "parent/1")
print(response)

input()
# deletes user data of the given id error check
response = requests.delete(BASE + "parent/1")
print(response)

input()
print("parent user data update test")

# updates user data of the given id
response = requests.patch(
    BASE + "parent/2", {"city": "Chittagong", "zipCode": 4225})
print(response.json())

input()
# updates user data of the given id error check
response = requests.patch(
    BASE + "parent/1", {"city": "Chittagong", "zipCode": 4225})
print(response.json())

input()
print("parent user data read test")

# gets the user data of the given id
response = requests.get(BASE + "parent/3")
print(response.json())

input()
# gets the user data of the given id error check
response = requests.get(BASE + "parent/3")
print(response.json())

print("child test")
# inserts user data to child database
input()
data1 = [{"firstName": "Nadia", "lastName": "Tasnim", "parentId": 3},
         {"firstName": "Sadia", "lastName": "Anjum", "parentId": 1},
         {"firstName": "Salma", "lastName": "Alam", "parentId": 2}]

print("child user data input test")
for i in range(len(data1)):
    response = requests.post(BASE + "child/" + str(i+1) +
                             str(data1[i]["parentId"]), data1[i])
    print(response.json())

input()
print("child user data delete test")

# deletes user data of the given id
response = requests.delete(BASE + "child/13")
print(response)

input()
# deletes user data of the given id error check
response = requests.delete(BASE + "child/13")
print(response)

input()
print("child user data update test")

# updates user data of the given id
response = requests.patch(
    BASE + "child/32", {"parentId": 3})
print(response.json())

input()
# updates user data of the given id error check
response = requests.patch(
    BASE + "child/32", {"parentId": 3})
print(response.json())

input()
print("child user data read test")

# gets the user data of the given id
response = requests.get(BASE + "child/33")
print(response.json())

input()
# gets the user data of the given id error check
response = requests.get(BASE + "child/31")
print(response.json())

input()
print("parent and child user data delete test if parent id is deleted")

# this deletes the user from the parent and deletes child user data to if the parent has a child
response = requests.delete(BASE + "parent/3")
print(response)
