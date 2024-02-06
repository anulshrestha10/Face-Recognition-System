import os
import pickle

import numpy as np

# Load registered users from the dataset
with open('data/names.pkl', 'rb') as f:
    registered_users = pickle.load(f)

# Print all registered users
print("Registered Users:")
for user in registered_users:
    print(user)