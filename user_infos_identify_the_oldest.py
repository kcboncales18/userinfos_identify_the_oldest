#array
user_infos = []

def user_name (): #define the variables
    name = input("Kindly, insert your name: ")
    name.isalpha
    return name
def user_age (): 
    age = int(input("Kindly, insert your age: "))
    return age 

while True: 
    name = user_name()
    age = user_age ()

    user_infos.append({"user_name":name, "user_age":age}) #format

    print("User's informations")
    print(user_infos) #the program continues to ask without stopping. 

#asking the user to continue inserting another infos or not
    retry = input("Do you want to insert another infos? Yes or no.")
    if retry =="no":
        break
