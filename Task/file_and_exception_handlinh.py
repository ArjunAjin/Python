

# 1.

def read_file():
    try:
        file = open('file_path', 'r')
       
        file.cose()
    except FileNotFoundError:
        print('ERROR: friends.txt file is not found')
   
read_file()


# 2 .

def create_file():
    try:
        file = open('C:/PGP_Data_science_and_AIML/Python/Task/friends.txt','w')
        print("friends.txt file created successfully.")
        file.close()

    except Exception as e:
        print("Error:", e)

create_file()



# 3 . 
file_path = 'C:/PGP_Data_science_and_AIML/Python/Task/friends.txt'
def add_friend():
    name = input("Enter your friend's name:")
    try:
        file = open(file_path, 'a')
        file.write(name + '\n')
        file.close()
        print("Friend's name added successfully.")  

    except FileNotFoundError:
        print("Error: friends.txt file not found.")
 
add_friend()









































