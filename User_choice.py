import pandas as pd
record = pd.read_json("Bank_data.json")

class User_Choice:
    def user_account_no(self):
        self.user_account = int(input('please enter your account number'))


    def check_account_no(self):
        self.a = 0
        if self.user_account in record['Account_number'] :
            print('what do you want enter\n Press 1- To Deposite \n Press 2- To withdraw')
        else:
            print('you enter wrong account number')
            self.a = 1

    def take_user_input(self):
        self.user_input = int(input('enter your choice'))





