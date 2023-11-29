from Countries import *
from Measuring import *



def main():
#takes user input of the number of countries the user wishes to add
    number_of_countries = int(input("Enter the number of countries you want to measure: "))
#new  HappinessMeter object created 
    HP = HappinessMeter()
    
    for _ in range(number_of_countries):
#new country object
        country = Country()
#setting the values for each country using setter
        country.set_cname(input("Enter the name of the country: "))
        country.set_env(float(input("Enter environment factor (0-100): ")))
        country.set_economy(float(input("Enter economy factor (0-100): ")))
        country.set_culture(float(input("Enter culture factor (0-100): ")))
        country.set_healthcare(float(input("Enter healthcare factor (0-100): ")))
        country.set_education(float(input("Enter education factor (0-100): ")))
# adding country to the list present in the HP alson known as HappinessMeter class
        HP.append_countries(country)
    
    print("Happiness Measurement")
    HP.measure_happiness()
    print("\nThanks for using our happiness measurement system")
    input("\n'Click ENTER to exit'")
if __name__=="__main__":
    main()