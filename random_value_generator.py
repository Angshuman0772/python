import random

for i in range(5):
    print(random.randint(10, 20))
    
    
members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)