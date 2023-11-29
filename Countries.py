#inializing the country class
class Country:
#placing only the neccessary variables to "__slots__" and converting it into private
    __slots__=["__Name_of_country","__environment_type","__Economy","__Culture", "__Health_care", "__Education"]

    def __init__(self):
        self.__Name_of_country = "Country Name"
        self.__environment_type = 0
        self.__Economy = 0
        self.__Culture = 0
        self.__Health_care = 0
        self.__Education = 0

#setter and getter used for country name function
    def set_cname(self, cname):
#The above mentioned function is  used to assign a value to the set_cname which is an attribute
        if cname!="":
            self.__Name_of_country = cname
        else:
            raise ValueError("Please enter a valid Country Name")
    
    def get_cname(self):
        return self.__Name_of_country
    
#setter and getter for the given environment 
    
    def set_env(self, env):
#The above mentioned function is  used to assign a value to the set_env  which is an attribute
        if env <= 100 and env >= 0:
            self.__environment_type = env
        else:
            raise ValueError("Please Enter a Value between 0 and 100")
        
    def get_env(self):
        return self.__environment_type
    
#setter and getter for the given economy 

    def set_economy(self, economy):
#The above mentioned function is  used to assign a value to the set_economy which is an attribute
        if economy <= 100 and economy >= 0:
            self.__Economy = economy
        else:
            raise ValueError("Please Enter a Value between 0 and 100")

    def get_economy(self):
        return self.__Economy
    
#setter and getter for the given culuture 

    def set_culture(self, CULT):
    #The above mentioned function is  used to assign a value to the set_culture which is an attribute
        if CULT <= 100 and CULT >= 0:
            self.__Culture = CULT
        else:
            raise ValueError("Please Enter a Value between 0 and 100")
        
    def get_culture(self):
        return self.__Culture

#setter and getter for the given healtcare 

    def set_healthcare(self, Hcare):
#The above mentioned function is  used to assign a value to the set_healthcare which is an attribute
        if Hcare <= 100 and Hcare >= 0:
            self.__Health_care = Hcare
        else:
            raise ValueError("Please Enter a Value between 0 and 100")
    
    def get_healthcare(self):
        return self.__Health_care
   
#setter and getter for the given education 

    def set_education(self, edu):
#The above mentioned function is  used to assign a value to the set_educationh  which is an attribute
        if edu <= 100 and edu >= 0:
            self.__Education = edu
        else:
            raise ValueError("Please Enter a Value between 0 and 100")

    def get_education(self):
        return self.__Education
    
#This function is used to obrain the content for the education attribute
