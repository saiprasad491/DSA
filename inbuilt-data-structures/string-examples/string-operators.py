# print("sai"+10) #TypeError: can only concatenate str (not "int") to str
#   print("sai"+str(10)) #sai10

# print("ab"*3) #ababab
# print("ab"*int("3")) #ababab
# print("ab"*"3") #TypeError: can't multiply sequence by non-int of type 'str'

# print("ai" in "sai")  #True
# print("is" not in "sai")  #True

# print("abc"<"abd")  #True
# print("abc"<"abc")  #False
# print("abc">"abd")  #False
# print("abc">"abc")  #False
# print("abc"<="abd")  #True
# print("abc">="abc")  #True
# print("abc"=="abc")  #True
# print("abc"!="abc")  #False

# s = "prakash"
# print(s)          #prakash
# print(len(s))     #7
# print(max(s))     #s
# print(min(s))     #a
# print(sorted(s))  #['a', 'a', 'h', 'k', 'p', 'r', 's']
# print(sorted(s,reverse=True)) #['s', 'r', 'p', 'k', 'h', 'a', 'a']
# print(ord('a')) #97
# print(chr(97))  #a

# s = 'welcoMe to Python Programming'
# print(s)                #welcoMe to Python Programming
# print(s.upper())        #WELCOME TO PYTHON PROGRAMMING
# print(s.lower())        #welcome to python programming
# print(s.swapcase())     #WELCOmE TO pYTHON pROGRAMMING
# print(s.title())        #Welcome To Python Programming
# print(s.capitalize())   #Welcome to python programming

# s = 'sai'
# print(s.count('ai'))  #1
# print(s.replace('ai',"hubha"))  #shubha
# print(s.startswith('s'))  #True
# print(s.endswith('sh'))  #False
# print(s.index('ai'))  #1
# print(s.find('ai'))  #1
# print(s.find('aii'))  #-1
# print(s.index('aii'))  #ValueError: substring not found
# print("saiprasad sahoo".split(' ')) #['saiprasad', 'sahoo']
# print("25/10/2025".split('/')) #['25', '10', '2025']

# l = ['python','is','very','easy']
# print(" ".join(l))  #python is very easy
# print(":".join(l))  #python:is:very:easy

# s = "sai"
# print(s.isalnum())  #True
# print("123".isalnum())  #True
# print("123".isdigit())  #True
# print(s.isalpha())  #True
# print("abd".islower())  #True
# print("AD".isupper())  #True

# print("".isspace()) #False
# print("abd cd".isspace()) #False
# print(" ".isspace()) #True
# print("  ".isspace()) #True



