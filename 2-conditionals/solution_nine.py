password = str(input("Enter your password: "))
if len(password) > 10 : 
    strength = "Strong"
elif len(password) >= 8 :
    strength = "Moderate"
else :
    strength = "Weak"

print(f"Your password is {strength}")