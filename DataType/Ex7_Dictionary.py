student = {
    "name":"Rahul",
    "age":20,
    "courses": ["Java","Selenium","Python"],
    "is_graduated":True
}

print("-------Accessing data------")
print(student["name"])              #Rahul
print(student.get("age"))          #20

print(student)

print("-----Adding new k-v pair-------")
student["grade"]="A"
print(student)

print("----updating existing data-----")
student["age"]=25
print(student)

print("-------Removing k-v pair-------")
student.pop("grade")
print(student)
student.popitem()           #remove last k-v pair from dict

print("-------------")
print("age" in student)
print(student.__contains__("age"))

print("------Access k-v-----")
print(student.keys())
print(student.values())
print(student.items())

print("------prin k-v through loop-----")
for key,value in student.items():
    print(key, value)