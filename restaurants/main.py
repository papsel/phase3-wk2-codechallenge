from review import Review
from restaurant import Restaurant
from  customer import Customer

print("RESTAURANTS")
sfc=Restaurant('SFC')
print(sfc.name())

kfc=Restaurant('KFC')
print(kfc.name())
print(kfc.customers())

bigsquare=Restaurant('BIGSQUARE')
print(bigsquare.name())


print("CUSTOMERS")
elijah=Customer("Elijah","Njora")
print(elijah.full_name())
mary=Customer("Mary","Nduta")
print(mary.full_name())

print("REVIEWS")
good=Review("Elijah Njora","Kfc",9)
bad=Review("Mary Nduta","sfc",5)
better=Review("Elijah Njora","bigsquare",7)
print(bad.customer())
nice=Review("Mary Nduta","sfc",9)