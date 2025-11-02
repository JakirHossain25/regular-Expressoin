import re
# text="Email yoi feedback here : book@subeen.com py.book@@subeen.com book_py@subeen.com thank you"
# result= re.findall(r"(\w+@\w+[.]\w+)",text)
# print(result)


# tx="Email yoi feedback here : book@subeen.com py.book@@subeen.com book_py@subeen.com thank you"
# result= re.findall(r"[.\w]+@\w+[.]\w+",tx)
# print(result)



tx="book At subeen.com, book At subeen.com,book (at) subben dot com,book [at] subeen [dot] com"
result= re.sub(r"\s+[\[]*\s*at\s*[\)\]]*\s+",'@',tx,flags=re.I)
print(result)

