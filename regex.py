import re
text="Email you feedback: book@gmail.com book thank you"
result= re.findall(r"(\w+@\w+\.\w+)",text)
print(result)


text="Email you feedback: book@gmail.com book thank you"
result1= re.findall(r"(\w+@\w+[.]\w+)",text)
print(result1)


