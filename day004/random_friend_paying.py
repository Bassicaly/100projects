import random


friends = ["Alice", "Bob", "Charlie", "David", "Eve"]

# 1ste option
print(random.choice(friends))

# 2de option
random_index = random.randint(0, len(friends) - 1)
print(friends[random_index])