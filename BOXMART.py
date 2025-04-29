connon = 'Yes'

while connon == 'Yes':
    name = input("Enter your name: ")
    hrsworked = int(input("Enter the number of work hrs: "))
    occupation = input("Enter the Employee occupation: ")
    
    if occupation == "cashier":
        payrate = 17.25
    elif occupation == "clerk":
        payrate = 18
    elif occupation == "manager":
        payrate = 25.25
    else: 
        print("**Invalid Occupation Code ** Program stopped*** Check your data****")
        exit()

    normal_hrsworked = 0
    overtime_hrsworked = 0


    if hrsworked > 40:
        normal_hrsworked = hrsworked
        overtime_hrsworked = hrsworked - 40
    else:
        normal_hrsworked = hrsworked
        overtime_hrsworked = 0

    if occupation == 'manager':
        normal_hrsworked = 40
        overtime_hrsworked = 0


# Logic changes for Capstone is here


    print(f"Hello, {name}! You are a {occupation}.")
    print(f"Your work hours are, {normal_hrsworked}! You have {overtime_hrsworked} overtime hrs.")
    print(f"Your payrate is, {payrate}.")
   
    connon = input("Do you wish to continue? ")
    if connon == 'No':
        break
