from review import Review  # Import the Review class

class Restaurant():
    # intialises restaurant with name
    def __init__(self,name):
         if isinstance(name, str):
            self._name = name
         else:
            print("Name must be a string")
            
    # returns restaurant's name    
    def name(self):
        return self._name    
    # returns a list of restaurant reviews
    def reviews(self):
        return [review for review in Review.all() if review.restaurant()== self._name]

           
    
    # returns a list of customers
    def customers(self):
        return set([review.customer() for review in  self.reviews()] )
    
    # calculate average star rating
    def average_star_rating(self):
        if not self.reviews():
            return 0  # No reviews, so average is 0
        total_ratings = sum(review.rating() for review in self.reviews())
        average = total_ratings / len(self.reviews())
        return average

sfc=Restaurant('SFC')
print(sfc.average_star_rating())