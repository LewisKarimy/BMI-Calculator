weight = 60 
height = 1.79832 # in cm

BMI = weight / height ** 2

print (BMI)

if BMI < 18.5:
    print('You are underweight')
elif  18.5 <=  BMI <= 25:
    print("You are healthy :)")
elif 25 <=  BMI  <= 30:
    print("You are Overweight")
else:
    print("You are Obese")
    
       