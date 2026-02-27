# try:
#     file=open("bca.txt")
#     new_dictionary= {"key":"value"}
#     print(new_dictionary["key"])
# except FileNotFoundError:
#     file=open("bca.txt","w")
#     file.write("Hello from Nepal")
# except KeyError as e_msg:
#     print(f"The key {e_msg} does not exit")
# else:
#     content=file.read()
#     print(content)
# finally:
#     raise IndexError("This is an error that I made up")

# height=float(input("Enter your height:"))
# weight=float(input("Enter you weight:"))
#
# if height > 3:
#     raise ValueError("The height should not be over 3")
#
# bmi=weight/height ** 2
# print(f"Your bmi is {bmi}")



