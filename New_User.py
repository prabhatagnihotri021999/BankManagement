import pandas as pd
record = pd.read_json("Bank_data.json")

class New_User:
    def user_information(self):
        user_name = input('enter your name')
        user_age = int(input('enter your age'))
        user_account_no = int(len(record) + 1)
        record.loc[user_account_no-1, 'Account_number'] = user_account_no
        record.loc[user_account_no - 1, 'Name'] = user_name
        record.loc[user_account_no - 1, 'Age'] = user_age
        record.loc[user_account_no - 1, 'Balance'] = 0
        record['Age'] = record['Age'].astype(int)
        record['Account_number'] = record['Account_number'].astype(int)
        record['Balance'] = record['Balance'].astype(int)
        record.to_json('Bank_data.json')


    def print_account_information(self):
        print(f"your account details are \n {record.loc[record.Account_number == len(record)]}")


