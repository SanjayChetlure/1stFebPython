studentData=[20,50,25,60,10,65]

for data in studentData:
    if data==60:
        continue
    print(data)


print("---------------")
studentsPEM=[500,400,600,100,250,800]
for PEM in studentsPEM:
    if PEM<300:
        continue
    print("Selected for Mains Exam: ",PEM)