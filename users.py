class User:
    usercount = 0

    def __init__(self,name,country,occupation,hobbies):
        self.name = name
        self.country = country
        self.occupation = occupation
        self.hobbies = hobbies
        User.usercount += 1

    def getUserCount(self):
        return User.usercount
    
    def getUserProfile(self):
        print("'{0}' is from '{1}' working as '{2}'. Hobbies are '{3}'".format(self.name, self.country, self.occupation, self.hobbies))
