class User:
    def __init__(self, email: str = "", password: str =""  ):
        self.nom :str 
        self.prenom: str
        self.email: str = email
        self.password: str = password

        if( email == "root@localhost.com"):
            print("Welcome, you are the super User, now you can access to the database")
            #call the function accessDB 
            # you cna call deleteUser too after selecting one of the list shown   
        else:
            print("Welcome, you are a user, you can modify your personal data ")


    def as_dict(self) -> dict:
        """
        Convert user type into python dict
        """
        return {
            "fname" : self.prenom,
            "lname" : self.nom,
            "email" : self.email,
            "password": self.password
        }


    def as_user(item:dict) -> object:
        """
        Convert python dict type into user item
        """
        user = User(
            prenom = item["fname"],
            nom = item["lname"],
            email = item["email"],
            password = item["password"]
        )
        return user


    def getall() -> list:
        """
        as a super user you can access to all the data 
        and you can delete an account 
        """
        
    def deleteUser(user):
        users.delete(user)

