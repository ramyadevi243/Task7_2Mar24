# Requests module allows us to send HTTP requests and to interact with APIs.
import requests

# Creating a class called Country
class Country:
    # Constructor takes one parameter url
    def __init__(self, url):
        # Assigns the value of url parameter to url attribute of the instance.
        self.url = url
        # This line calls fetch_data method and assigns the returned value to 'info' attribute of the instance.
        self.info = self.fetch_data()
        
    # This method fetches data from specified URL.
    def fetch_data(self):
        #This line sends a GET request to the URL specified in the url attribute of the instance using the requests.get function.
        # It returns a Response object representing the HTTP response.
        response = requests.get(self.url)
        # This line checks if the status code of the response is 200, which indicates that the request was successful
        if response.status_code == 200:
            # If the request was successful, this line returns the JSON content of the response using the .json() method
            return response.json()
        else:
            print("Failed to fetch data")
            # This line returns an empty list if data fetching is failed.
            return []

    # Creates a method to display name of country, currencies and currency symbol.
    def country_details(self):
        # Iterates through the info object where data is fetched from the url.
        for i in self.info:
            # It returns the value from the key name and common and stores in the object
            country_name = i.get('name').get('common')
            # Prints names of all countries from the list
            print("Country Name: ", country_name)
            
            # This retrieves the currencies of the corresponding country
            currencies = i.get('currencies', {})
            # Iterates over the currencies which is a list
            for j in currencies:
                # Returns the corresponding values of currency and symbol
                currency_name = currencies[j].get('name')
                currency_symbol = currencies[j].get('symbol', 'N/A')
            print("Currency Name: ", currency_name)
            print("Currency Symbol: ", currency_symbol)
            print()
            
    # Creates a method to display the countries which have Dollar as its currency.
    def dollar_currency(self):
        print("Countries which have DOLLAR as its currency:")
        for i in self.info:
            currencies = i.get('currencies', {})
            for j in currencies:
                #country_name = i.get('name').get('common')
                if currencies[j].get('name') == 'United States dollar':
                    print(i.get('name').get('common'))
                    break
    
    # Creates a method to display the countries which have Euro as its currency.
    def euro_currency(self):
        print("Countries that have EURO as its currency:")
        for i in self.info:
            currencies = i.get('currencies', {})
            for j in currencies:
                if currencies[j].get('name') == 'Euro':
                    print(i.get('name').get('common'))
                    break

# Assigning the specified URL as value for url
url = "https://restcountries.com/v3.1/all"

# Created an object for the class Country
country = Country(url)

# Calling the method for displaying the country name, currency and symbol
country.country_details()
print()

# Calling the method for displaying the country names that have Dollar as their currency
country.dollar_currency()
print()

# Calling the method for displaying the country names that have Euro as their currency
country.euro_currency()