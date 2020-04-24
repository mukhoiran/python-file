# FILE I/O

""" Read file txt """

# file = open('data.txt','r')
# text = file.read()
# print(text)

""" Write file txt """

file = open('data.txt','a+')
file.write("Hello my Bro")

file.seek(0)
text = file.read()
print(text)
