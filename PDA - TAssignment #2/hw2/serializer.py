# AndrewID: judahemu

# Import the class and other packages needed
import json
import os
from attendance import Attendance
from employee import Employee
from manager import Manager
from intern import Intern
# from hrmis import HrMaster

class Serializer:
    
    """
    The Serializer class is responsible for converting to JSON format while deserializing is converting from JSON format.
    The function check the type of account before execution.
    """


    def __init__(self, filename="employee.json"):
        self.filename = filename

    def serialize_to_json(self, employee_object):

        # Check the type of the account object as part of classifying data
        if not isinstance(employee_object, (BankAccount, SavingsAccount, CheckingAccount, CreditCardAccount)):
            raise ValueError("Unsupported account type")

        # Create a dictionary for common values from each account.
        account_data = {
            'AccountType': employee_object.__class__.__name__,
            'Owner': employee_object.get_account_name(),
            'Balance': employee_object.get_account_balance(),
            'AccountNumber': employee_object.get_account_number()
        }

        # Adding the extra values to each account_data based on its type
        if isinstance(employee_object, SavingsAccount):
            account_data['InterestRate'] = employee_object.interest_rate
        
        elif isinstance(employee_object, CheckingAccount):
            account_data['OverdraftLimit'] = employee_object.overdraft_limit
        
        elif isinstance(employee_object, CreditCardAccount):
            account_data['CreditLimit'] = employee_object.credit_limit

        # Saving data
        existing_data = self.load_data()
        self.update_data(existing_data, account_data)
        self.save_data(existing_data)


    def deserialize_from_json(self):
        
        # Using os package imported earlier to find if the file exist and import the file
        existing_data = self.load_data()
        # accounts = []

        # Using FOR LOOP to retrieve constitutes information of the dictionary
        for data in existing_data:
            account_type = data['AccountType']
            owner = data['Owner']
            balance = data['Balance']
            account_number = data['AccountNumber']

            # Checking if account type before retrieving the data
            if account_type == 'BankAccount':
                # account = BankAccount(owner, account_number, balance)
                print (f'Account = BankAccount("{owner}", "{account_number}", {balance})')
            
            # Checking if account type before retrieving the data
            elif account_type == 'SavingsAccount':
                interest_rate = data['InterestRate']
                # account = SavingsAccount(owner, account_number, balance, interest_rate)
                print (f'Account = SavingsAccount("{owner}", "{account_number}", {balance}, {interest_rate})')

            # Checking if account type before retrieving the data
            elif account_type == 'CheckingAccount':
                overdraft_limit = data['OverdraftLimit']
                # account = CheckingAccount(owner, account_number, balance, overdraft_limit)
                print (f'Account = CheckingAccount("{owner}", "{account_number}", {balance}, {overdraft_limit})')

            # Checking if account type before retrieving the data
            elif account_type == 'CreditCardAccount':
                credit_limit = data['CreditLimit']
                # account = CreditCardAccount(owner, account_number, balance, credit_limit)
                print (f'Account = CreditCardAccount("{owner}", "{account_number}", {balance}, {credit_limit})')

             # When data added are not matching any format
            else:
                raise ValueError("Unsupported account type")

            # accounts.append(account)

        # return existing_data

    
    # Reading the values of a JSON file
    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as json_file:
                return json.load(json_file)
        return []

    # The dictionary update as you change any value in the list below. 
    # However, when you change Owner's name, it appends to the existing list.
    def update_data(self, existing_data, new_data):
        owner_name = new_data['Owner']
        updated_existing = False

        for entry in existing_data:
            if entry['Owner'] == owner_name:
                entry.update(new_data)
                updated_existing = True
                break

        if not updated_existing:
            existing_data.append(new_data)

    # Saving the files in the pathway as this file
    def save_data(self, data):
        with open(self.filename, "w") as updated_file:
            json.dump(data, updated_file, indent=4)

# # Example usage
# bank_account = BankAccount("Jules Uahemuka", "787641301", 2000.0)
# savings_account = SavingsAccount("Emmy Iraturinze", "1234567890", 5000.0, 20)
# checking_account = CheckingAccount("Sergio Mutabazi", "9876543210", 2500.0, 500.0)
# credit_card_account = CreditCardAccount("Jacky Kalinda", "5678901234", 200.0, 2000.0)


# # Serialize and save each account type to JSON file.
# serializer = Serializer()
# serializer.serialize_to_json(bank_account)
# serializer.serialize_to_json(savings_account)
# serializer.serialize_to_json(checking_account)
# serializer.serialize_to_json(credit_card_account)

# # Deserialize and print the values from our JSON file.
# serializer.deserialize_from_json()
