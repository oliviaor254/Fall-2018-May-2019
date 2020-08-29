usernames = []
passwords = []
usepass = {}
correct = False
sets = int(input("Enter the number of sets usernames/password combinations: "))
for i in range(sets):
    user = input("Enter a username: ")
    usernames.append(user)
for a in range(sets):
    passw= input("Enter a password: ")
    passwords.append(passw)
for b in range(len(usernames)):
    calc = {usernames[b]: passwords[b]}
    usepass.update(calc)
while correct == False:
    use = input("Enter what you think the username is: ")
    word = input("Enter what you think the password is: ")
    key = {use: word}
    if use in usepass:
        if word in usepass.items():
            if key[use] == usepass[use]:
                correct = True
                print('Congratulations! You are allowed into the system!')
                break
            else:
                print("That is not the correct username/password combination. Try again")
        else:
            print("That is not the correct password.")
    else:
        print("That is not the correct username")
