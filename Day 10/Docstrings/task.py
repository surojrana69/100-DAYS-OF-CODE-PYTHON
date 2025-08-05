'''This function take the first and last name and using .title() make the it title case meaning i will capitalize the first letter of every word or any words after spaces. '''
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("Suroj", "Rana")

length = len(formatted_name)



