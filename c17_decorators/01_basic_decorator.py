"""

Solution to coding exercise #1

"""

# ---- Do not change the code below ----
# User identity dictionary
user = {
    'id': 1,
    'name': 'jose',
    'role': 'admin'
}


# delete_database() function, DO NOT CHANGE
def delete_database():
    # perform deletion
    print('Database deleted!')


# ---- Do not change the code above ----


# You code starts here:
# Define a check_permission() decorator:
def check_permission(func):
    def secure_func():
        if user.get('role') == 'admin':
            return func()
        raise PermissionError("You are not an admin")

    return secure_func


# Use the check_permission() decorator and delete_database() function to
# create a secure_delete_database() function:

@check_permission
def secure_delete_database():
    delete_database()




