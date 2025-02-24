# contact book

users = [
    {
        'name':'anushka',
        'phone_no':11002,
        'email':'anu19@gmail.com'
    },
    {
        'name':'aashika',
        'phone_no':11099,
        'email':'aashika19@gmail.com'  
    },
    {
        'name':'nansika',
        'phone_no':11077,
        'email':'nanshika19@gmail.com' 
    },
    {
        'name':'anita',
        'phone_no':11011,
        'email':'anita19@gmail.com' 
    },
]
def add_contact(name,phone_no,email):
    new_conct = {'name':name, 'phone':phone_no,'email':email}
    users.append(new_conct)
    print('successfully added')
add = add_contact('saugat',12011,'saugat19@gmail.com')
print(add)
print(users)

def search_conct(name):
    result = [user for user in users if user['name'].lower()==name.lower()]
    if result:
        return result
    else:
        return f"not found {name}"

a = search_conct('anushka')
print(a)

def display_conct():
    if users: 
        print("All Contacts:")
        for user in users:
            print(f"Name: {user['name']}, Phone: {user['phone_no']}, Email: {user['email']}")
    else:
        print("No contacts found")

# Example Usage
users = [
    {'name': 'anushka', 'phone_no': 11002, 'email': 'anu19@gmail.com'},
    {'name': 'aashika', 'phone_no': 11099, 'email': 'aashika19@gmail.com'},
]

display_conct()  

grocery = ['fruits','drinks','cauliflower','potato','corrinder','tomato']

# adding items in grocery
def add_grocery(items):
    grocery.extend(items)
    print('successfully added')
newitem = add_grocery(['zuchini','chilly'])
print(newitem)

def display_groc():
    if grocery:
        print('All grocery')
        for item in grocery:
            print(item[0:6])
    else:
        return 'not found'

display_groc()

# basic banking system


accounts = {
    1001: {'name':'Anushka','balance':10000},
    1002: {'name':'Aashika','balance':1000},
    1003: {'name':'Anita','balance':500000},
    
}
# dictonary to store transaction histroy for each account
transactions = {
    1001: [],
    1002: [],
    1003: [],
}
# deposite
def deposite(account_no,amount):
    if account_no in accounts:
        accounts[account_no]['balance'] += amount
        transactions[account_no].append(('deposite',amount))
        print(f"the balance is deposite to {account_no} is {amount} and new balance is {accounts[account_no]['balance']}")
    else:
        print('account not found')
    
deposite(1001,9000)

# withdraw
def withdraw(account_no,amount):
    if account_no in accounts:
        if accounts[account_no]['balance'] >= amount:
            accounts[account_no]['balance'] -= amount
            transactions[account_no].append(('withdraw',amount))
            print(f"₹{amount} withdrawn from Account {account_no}. New balance: ₹{accounts[account_no]['balance']}")
        else:
            print('insufficient balance')
    else:
        print('Account not found')

withdraw(1002,200)

# checking balance

def check_balance(account_no):
    if account_no in accounts:
        print(f"Account: {account_no} Balance:{accounts[account_no]['balance']}")
    else:
        print('Account not found')

check_balance(1002)

def display_transaction(account_no):
    if account_no in accounts:
        print(f"Transaction histroy of account {accounts}")
        for transaction in transactions[account_no]:
            print(f" {transaction[0]}: {transaction[1]}")
    else:
        print('Account not found')

display_transaction(1001)


students = {
    1001: {'name':'Anushka','major':'computer_science','marks':{
        'NM':90,
        'DSA':95,
        'Statistics':89
    }},
    1002: {'name':'jenisha','major':'computer_science','marks':{
        'NM':91,
        'DSA':85,
        'Statistics':79
    }},
    1003: {'name':'Anjeela','major':'computer_science','marks':{
        'NM':70,
        'DSA':75,
        'Statistics':89

    }}
}
# to store the students results
result = {
    1001:[],
    1002:[],
    1003:[],
}
def grade(student_id, total):
    if student_id in students:
        # Update the student's NM mark
        students[student_id]['marks'] = total
        
        # Determine the grade based on the updated mark
        if total == 100:
            grade = 'A'
        elif total >= 90:
            grade = 'A-'
        elif total >= 80:
            grade = 'B+'
        elif total >= 70:
            grade = 'B-'
        else:
            grade = 'F'

        # Store the result
        result[student_id].append({'subject': 'NM', 'grade': grade, 'total': total})

        # Print the grade
        print(f"Your grade in NM is {grade} with a total of {total}")
    else:
        print('Student not found. Try next year.')

# Example usage
grade(1002, 70)

# You can print the `result` dictionary to verify
print(result)


student_result = {'name':'Anushka', 'sem':'third', 'subjects':{
    'NM': 90,
    'DSA':95,
    'STAT':98,
    'CG':88,
    'CA':92
},
}

def total(subjects):
    return sum(subjects.values())

total_marks = total(student_result['subjects'])
print(total_marks)

def percentage(total_marks):
    return (total_marks*100)/500
student_percentage = percentage(total_marks)
print(student_percentage)

def grade(subjects):

        for marks in subjects.values():
             
         if marks in range(89,101) :
            print('your grade is A')
         elif marks in range(79,91) :
            print('Your grade is Aminus')
         elif marks in range(69,81):
            print('Your garde is Bplus')
         else:
             print('try next time')
        return 'Complete'
     
total_grade = grade(student_result['subjects'])
print(total_grade)

def total_gpa(subject_marks):  # Only one parameter for the subject marks
   
    total_grade = sum(subject_marks.values()) / len(subject_marks)
    
    # Determine the GPA based on average marks
    if 90 <= total_grade <= 100:  
        print('Your grade point is 4.0')
    elif 80 <= total_grade < 90:  
        print('Your grade point is 3.7')
    elif 70 <= total_grade < 80:  
        print('Your grade point is 3.3')
    else:  
        print("You have less grading point!")
    return 'complete'
    

student_total = total_gpa(student_result['subjects'])
print(student_total)

   
