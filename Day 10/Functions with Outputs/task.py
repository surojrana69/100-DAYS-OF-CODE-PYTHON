# def mul_fucntion():
#     result = 10/2
#     return result
# output=mul_fucntion()
# print(output)

def format_name(f_name,l_name):
    # print(f_name.title())
    # print(l_name.title())
    formatted_f_name=f_name.title()
    formatted_l_name=l_name.title()
    # print(f"{formatted_f_name},{formatted_l_name}")
#     return f"{formatted_f_name} {formatted_l_name}"
#
# # format_name("SUrOj","RaNA")
# formatted_string=format_name("SuRoJ","RANA")
# print(formatted_string)
#
# print(format_name("SURoj", "RANA"))

#USING ONES FUCTION OUTPUT AS INPUT IN ANOHTER FUNCTION

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

print(add(2,sub(4,mul(2,2))))