person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)


# the name of the second child
print(person.get("children")[1])
print(person["children"])

# the name of the cat
print(type(person))


# use a for loop to list each child
for i in person["children"]:


# print out the pets in this format;
# 'type of pet: dog name of pet: Fido'

for 