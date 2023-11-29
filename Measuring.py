class HappinessMeter:

    __slots__ = ["__All_Countries"]
    def __init__(self):
        self.__All_Countries = []
#this method is used to display all the countries that have been added to the list
    def append_countries(self,country):
        self.__All_Countries.append(country)

    def measure_happiness(self):
#this method is used to obtain the average of the listed country's metrics
        for i in self.__All_Countries:
#here it prints the value country name and their respective averages
            print(i.get_cname(),": ")
            print(round(((i.get_env() + 
                          i.get_economy() + 
                          i.get_culture() + 
                          i.get_healthcare() + 
                          i.get_education())
                          /5),2))