my_file = open('data.txt', 'r')
file_content = my_file.read()

my_file.close()

print(file_content)

user_name = input('Enter your name: ')

my_file_writing = open('data.txt', 'a')
my_file_writing.writelines(user_name)

my_file_writing.close()

print("Now enter three more names...")
users = []
for i in range(3):
    response = input("Name: ")
    users.append(response)

my_file_writing_2 = open('data.txt','a')
my_file_writing_2.writelines(users)

my_file_writing_2.close()


