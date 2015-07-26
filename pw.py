__author__ = 'tle'
# pw.py - An insecure password locker. Enter your Username, and it will copy the password to your clipboard.

import sys
import os.path
import pyperclip
import pickle

filepath = "pword.p"

if os.path.exists(filepath) is False:
    passwords = {}
    with open(filepath, 'wb') as f:
        pickle.dump(passwords, f)

passwords = pickle.load(open(filepath, "rb"))


def save():  # saves to file
    pickle.dump(passwords, open(filepath, "wb"))


def add_new():
    print("Enter new username:")
    username = input()
    if username in passwords:
        print("Username '" + str(username) + "' already exists!\n")
    else:
        print("Enter password:")
        password = input()
        passwords[str(username)] = str(password)
        print("Account '" + username + "' successfully added.\n")


def remove_account():
    print("Enter username to delete:")
    delete_username = input()
    print("Are you sure you want to delete '" + str(delete_username) + "'? YES / NO.")
    agree = str(input()).upper()

    if agree == "YES":
        del passwords[delete_username]
        print("'" + str(delete_username) + "' successfully removed.\n")
    elif agree == "NO":
        print("'" + str(delete_username) + "' was not removed.\n")
    else:
        print("Invalid command.")
        sys.exit()


def copy_pw():
    print("Enter desired username: ")
    account = input()

    if account in passwords:
        pyperclip.copy(passwords[account])
        print('Password for ' + account + ' copied to clipboard.\n')
    else:
        print('There is no account named ' + account + "\n")


def __main__():
    print("Select a number:\n1. Retrieve Password\n2. Add Account\n3. Remove Account\n4. Exit\n")
    selection = int(input())

    if selection is 1:
        copy_pw()
    elif selection is 2:
        add_new()
    elif selection is 3:
        remove_account()
    else:
        sys.exit()
    save()
    __main__()  # allows for continuation

__main__()
