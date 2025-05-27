# def format_name(f_name, l_name):
#     if f_name =="" or l_name=="":
#         return "You did not provide any inputs."
#
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
#
# print(format_name(input("Enter your first name:"),input("Enter your last name:")))

def is_leap_year(year):
    if year%4!=0:
        return False
    elif  year%100!=0:
        return True
    elif year%400 ==0:
        return True
    else:
        return False

print(is_leap_year(2002))