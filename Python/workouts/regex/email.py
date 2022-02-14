import re

email='drp_thakur@yahoo.co.in'
def validate_email(email):
        valid = re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",email)
        if valid:
            print()
            print(email)
            print()
        print('XXXXXXXXXXX== NOT_VALID ==XXXXXXXXXXXXXX')


def looping():
    with open('D:\\App_Folders\\vscode\\Python\\vumaasha-s-py\\workouts\\regex\\data.txt') as f:
        for line in f:
            # For Python3, use print(line)
            validate_email(line)
            if 'str' in line:
                break
looping()