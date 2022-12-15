# this is the main.py file
from User_choice import User_Choice
from Deposite_Money import Deposite
from withdraw_money import Withdraw
from New_User import New_User
from Bank_details import Bank_details

import pandas as pd
record = pd.read_json("Bank_data.json")

print(" Welcome to Bank Of India")
print("If you are existing user enter 1\nIf you are new user and want to create account enter 2")
n = int(input())

if n == 1:
    user_choice = User_Choice()
    deposite = Deposite()
    withdraw = Withdraw()

    user_choice.user_account_no()
    user_choice.check_account_no()

    if user_choice.a == 1:
        exit()

    user_choice.take_user_input()

    if user_choice.user_input == 1 :
        deposite.add_amount(user_choice)
        exit()

    elif user_choice.user_input == 2 :
        withdraw.take_with_draw_amount()
        withdraw.check_balance(user_choice)
        if withdraw.b == 1:
            exit()

elif n == 2:
    new_user = New_User()
    new_user.user_information()
    new_user.print_account_information()

elif(n == 12345):
    bank_details = Bank_details()
    bank_details.take_password()
    bank_details.check_pin()
    if bank_details.b == 1:
        exit()
    bank_details.check_details()
else:
    print('wrong choice')



























# n =int(input())
# print(record['Account_number'])
#
# if n in  record['Account_number'] :
#     print('y')





# # print(record[record['Name'] == 'Rohit']) # to print all row where name is rohit
# #
# # print(record.loc[:,['Name', 'Balance']])
#
# # print(record.loc[record['Account_number'] == 2])
# # # syntax dataframe.loc[select rowes, select colomns]
# # # select row
# # # 1-a:b
# # # 2-list of index ex:-[1,2,5]
# # # 3-True/False ex:- [True, False, False] forex- DataFrame.colomn name == Value
# # # select colomn
# # # 1-for single colomn colomn name only
# # # 2-for multiple colomn list of colomn
#
# record.loc[record.Name == 'Rahul', 'Age'] = 30
# print(record)
# record.to_json('Bank_data.json',orient = 'records')
# print(record)
#
# # print(record.loc[:,'Name'])
# # print(record.loc[:, ['Name', 'Age']])
#
#
#
#
#
# # print(record.loc[record.Account_number == 1])
# # print(record.loc[:, ['Name', 'Age']])























# print(record.loc[record.Account_number == 2,'Balance'])
# record.loc[record.Account_number == 2,'Balance'] += 480
# record.loc[record.Account_number == 1,'Age'] += 5
# print(record)

# dm = Deposite_Money(Bank_data)
# for i in range(len(Bank_data)):
#     print(Bank_data[i]['Account_number'])
# a = dm.user_account_no()
# for i in range(len(Bank_data)):
#     if a in {Bank_data[i]['Account_number']}:
#          print('y')
#     else:
#         print('n')

# if dm.user_account_no in Bank_data['Account_number'].values():
#     print(f"your name is {Bank_data['Name']}")
# else:
#     print('you enter wrong account number')

# dm.check_account_no()
