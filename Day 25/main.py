# # with open("weather_data.csv") as data_file:
# #     data=data_file.readlines()
# #     print(data)
#
# import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data=csv.reader(data_file)
# #     temperature=[]
# #     for row in data:
# #         if row[1] !='temp':
# #             temperature.append(int(row[1]))
# #
# #     print(temperature)
#
# import  pandas
#
# data=pandas.read_csv("weather_data.csv")
# temperature=data["temp"]
# # print(temperature)
# # print(type(data))
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list=data["temp"].to_list()
#
# # condition_list=data["condition"].to_list()
# # print(condition_list)
# #
# # average_temp=sum(temp_list)/len(data)
# # print(f"The average temperature of given data is",average_temp)
# #
# # average_temp=data["temp"].mean()
# # print(average_temp)
#
# # max_value=data["temp"].max()
# # print(max_value)
# #
# # #Get Data in Columns
# # print(data["condition"])
# # print(data.condition)
#
# #Get Data in Rows
#
# # print(data[data.day == "Tuesday"])
# #
# # #The row of data which had the highest temperature
# #
# # print(data[data.temp == data.temp.max()])
#
# # sunny=data[data.condition == "Sunny"]
# # print(sunny.day)
#
#
# #CONVERTING MONDAYS TEMP TO FAHRENHEIT
#
# # monday_temp=data[data.day == "Monday"]
# # print((monday_temp.temp*9/5) + 32)
#
# #CREATE A DATAFRAME FROM SCRATCH
#
# data_dic = {
#     "students": ["Suroj", "Aman", "Nirjal","Ankit", "Rabin","Sujan"],
#     "scores": [55 ,59,69,88,99,44],
#     "Address": ["Hetauda","Lamsure","kamane","Hetauda,"Chaukitol,"Hetauda]
#
# }
#
# Data=pandas.DataFrame(data_dic)
# Data.to_csv("new_data.csv")

import pandas

data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_color_counts=(data["Primary Fur Color"].value_counts())

create_csv=pandas.DataFrame(squirrel_color_counts)
squirrel_color_counts.to_csv("Suirrel_counts_with_color.csv")