emails = ['me@gmail.com','you@hotmail.com','they@gmail.com']
print("Without Forloop")
print(emails[0])
print(emails[1])
print(emails[2])

print("\nWith forloops")
for email in emails:
    #print(email)
    if "gmail" in email:
        print email