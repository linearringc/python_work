class User():
    def __init__(self, first_name, last_name, info):
        """初始化用户简介"""
        self.first_name = first_name
        self.last_name = last_name
        self.info = info
        self.login_attempts = 0

    def describe_user(self):
        print('your information as below: '+ self.first_name + ' ' +self.last_name + ' ' + self.info)

    def gret_user(self):
        print('Hello ' + self.first_name + self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 2
        print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)




User1 = User('Zhang', 'Bini', 'bad apple')
User2 = User('Adam', 'Scott', 'filmer')
User3 = User('Cici', '?', 'I love pizza hut')

User1.increment_login_attempts()
User1.increment_login_attempts()
User1.reset_login_attempts()
User1.increment_login_attempts()

User1.describe_user()
User2.describe_user()
User3.describe_user()

User1.gret_user()
User2.gret_user()
User3.gret_user()