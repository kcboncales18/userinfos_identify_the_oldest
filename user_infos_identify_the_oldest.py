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
    retry = input("Do you want to insert another infos? Yes or no.") #the program will continue if yes, and stop if no. 
    if retry =="no":
        break
#identifying the oldest
def oldest(user_infos): #new variable
    oldest_user = user_infos[0]
    for another_user in user_infos: 
        if another_user["user_age"] > oldest_user["user_age"]:
            oldest_user = another_user
    return oldest_user
oldest_user = oldest(user_infos)
print(f"the oldest user is {oldest_user['user_name']} with the age of {oldest_user['user_age']} years old.") 