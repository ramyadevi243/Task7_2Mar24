# Requests module allows us to send HTTP requests and to interact with APIs.
import requests

# Creating a class called Brewery
class Brewery:
    # Constructor takes one parameter states
    def __init__(self, states):
        # Assigns the value of states parameter to states attribute of the instance.
        self.states = states
        # Assigns url for base_url attribute of the instance.
        self.base_url = "https://api.openbrewerydb.org/v1/breweries"
        # This line calls fetch_data method and assigns the returned value to 'info' attribute of the instance.
        self.info = self.fetch_data()
    
    # This method fetches data from specified URL.
    def fetch_data(self):
        # Creating an empty list
        list_of_breweries = []
        # Iterating over states attribute
        for i in self.states:
            #This line sends a GET request to the URL specified in the base url attribute of the instance using the requests.get function.
            # It returns a Response object representing the HTTP response.
            # Also this part of url is a query string that includes parameters to filter the breweries by state
            response = requests.get(f"{self.base_url}?by_state={i}&per_page=10")
            # This line checks if the status code of the response is 200, which indicates that the request was successful
            if response.status_code == 200:
                # If the request was successful, this line returns the JSON content of the response using the .json() method
                breweries = response.json()
                # It extends the list with elements from breweries list
                list_of_breweries.extend(breweries)
            else:
                print("Failed to fetch breweries data")
        return list_of_breweries
    
    # Method to fetch the brewery names
    def get_breweries_list(self):
        brewery_names = [i['name'] for i in self.info]
        return brewery_names

    # Method to fetch count of breweries in each state    
    def count_breweries_state(self):
        state_count = {}
        for i in self.states:
            state_count[i] = sum(1 for j in self.info if j['state'] == i)
        return state_count
    
    # Method to fetch the number of types of breweries present in each city
    # of specified state
    def types_brewery_cites(self):
        brewery_type_city = {}
        for i in self.states:
            states = [j for j in self.info if j['state'] == i]
            cities = set(k['city'] for k in states)
            for city in cities:
                brewery_type_city.setdefault(i, {}).setdefault(city, set())
                for brewery in states:
                    if brewery['city'] == city:
                        brewery_type_city[i][city].add(brewery['brewery_type'])
        return brewery_type_city

    # Method to fetch the count of breweries that have websites in the specified states
    def brewery_website(self):
        breweries_website = {}
        for i in self.states:
            brewery_state = [j for j in self.info if j['state'] == i]
            website_count = sum(1 for i in brewery_state if 'website_url' in i and i['website_url'])
            breweries_website[i] = website_count
        return breweries_website


# Assigning a list of value to the variable called states
states = ['Alaska', 'Maine', 'New York']
# Creating an object for class Brewery
brewery = Brewery(states)

# Task_1 - Calling the method to find the names of all breweries of each state
brewery_names = brewery.get_breweries_list()
print("\nNames of All Breweries in Alaska, Maine and New York:")
for name in brewery_names:
    print(name)

# Task_2 - Calling the method to find the count of breweries in each state
brewery_count = brewery.count_breweries_state()
print("\nCount of Breweries in Each State: ")
for state, count in brewery_count.items():
    print(f"{state}: {count}")

# Task_3 - Calling method to find the breweries that have websites in each state
brewery_with_websites = brewery.brewery_website()
print("\nBreweries that have Websites in Each State:")
for state, website_count in brewery_with_websites.items():
    print(f"{state}: {website_count}")

# Task_4 - Calling method to find number of types of breweries present in individual cities of each state
brewery_type_count_city = brewery.types_brewery_cites()
print("\n\n\nNumber of Types of Breweries Present in Individual Cities of Each State:")
for state, cities in brewery_type_count_city.items():
    print(f"\nState: {state}")
    for city, data in cities.items():
        print(f"\n\tCity: {city}")
        for brewery in data:
            print(f"\t\tBrewery Type: {brewery}")