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
    
# Load existing labels and faces data
with open('data/names.pkl', 'rb') as f:
    labels = pickle.load(f)
with open('data/faces_data.pkl', 'rb') as f:
    faces_data = pickle.load(f)

# Function to delete user from dataset
def delete_user(user_name):
    global labels, faces_data
    indices_to_delete = [i for i, name in enumerate(labels) if name == user_name]

    if indices_to_delete:
        # Remove entries corresponding to the user from labels and faces data
        labels = [label for i, label in enumerate(labels) if i not in indices_to_delete]
        faces_data = np.delete(faces_data, indices_to_delete, axis=0)

        # Save updated data
        with open('data/names.pkl', 'wb') as f:
            pickle.dump(labels, f)
        with open('data/faces_data.pkl', 'wb') as f:
            pickle.dump(faces_data, f)

        print(f"User '{user_name}' deleted successfully.")
    else:
        print(f"User '{user_name}' not found in the dataset.")

# Get user input for name to delete
name_to_delete = input("Enter the name you want to delete from the dataset: ")

# Delete the user from the dataset
delete_user(name_to_delete)
