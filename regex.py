import re
text="Email you feedback: book@gmail.com book thank you"
result= re.findall(r"(\w+@\w+.\w+)",text)
print(result)

