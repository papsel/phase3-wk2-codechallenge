from review import Review  # Import the Review class

class Customer:
    # keeps track of all instances.
    customers = []
    
    # initialises given name and last name such that they can be updated
    def __init__(self, given_name=None, family_name=None):
        self._given_name = given_name
        self._family_name = family_name
        self._full_name = f"{given_name} {family_name}"
        Customer.customers.append(self)# adds an instance to the instance list
        
    # gets the recently updated name
    def given_name(self):
        return self._given_name
 
    # updates name only when its a string   
    def set_given_name(self, first_name):
        if isinstance(first_name, str):
            print(f"Setting given name to: {first_name}")
            self._given_name = first_name
            self._full_name = f"{first_name} {self._family_name}"
        else:
            print('Given name must be a string.')
    
    given_name = property(given_name, set_given_name)
    
    # gets the recently updated name
    def family_name(self):
        return self._family_name
    # updates name only when its a string     
    def set_family_name(self, last_name):
        if isinstance(last_name, str):
            print(f"Setting family name to: {last_name}")
            self._family_name = last_name
            self._full_name = f"{self._given_name} {last_name}"
        else:
            print('Family name must be a string.')

    family_name = property(family_name, set_family_name)
    
    # returns cutomers full name
    def full_name(self):
        return self._full_name
    
    # returns all customers
    @classmethod
    def all(cls):
        return cls.customers
    # returns a list of all restaurants customer has reviewed
    def restaurants(self):  
        return set([review.restaurant() for review in Review.all() if review.customer() in self.full_name()])
    
    # enable customer to add a new review
    def add_review(self, restaurant, rating):
        Review(Customer.full_name(self), restaurant, rating)
        
    # returns number of reviews
    def num_reviews(self):
        reviews=[review for review in Review.all() if review.customer() in self.full_name()]
        return len(reviews)
    
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.customers:
            if customer.full_name() == name:
                return customer
            else:
                print("customer not found")
                
    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in Customer.all() if customer.given_name == name]
        
    
    def __repr__(self):
        return f"{self._given_name} {self._family_name} "
    


elijah=Customer("Elijah","Njora") 
milly=Customer("Milly","Mburu") 
julius=Customer("Julius","Kahangi")
mary=Customer("Mary","Nduta")
minne=Customer("Minne","Warigia") 


elijah.add_review("Kfc",7)
print(Customer.find_by_name("Elijah Njora"))

print(Customer.find_all_by_given_name("Elijah"))   



    