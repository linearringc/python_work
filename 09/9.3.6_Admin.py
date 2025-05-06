class User():
    def __init__(self, first_name, last_name, info):
        """初始化用户简介"""
        self.first_name = first_name
        self.last_name = last_name
        self.info = info
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, info):
        super().__init__(first_name, last_name, info)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for p in self.privileges:
            print(p)

admin1 = Privileges(['can add post', 'can delete post', 'can ban user'])
admin1.show_privileges()

admin1 = Admin('Yi', 'Chen', '985211')
admin1.show_privileges()