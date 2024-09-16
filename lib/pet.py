import psycopg2
from psycopg2 import sql

class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']

    def __init__(self, name, pet_type):
        if pet_type not in Pet.PET_TYPES:
            raise ValueError(f"Invalid pet type: {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self.owner_id = None  # Initially, pet does not have an owner

    def set_owner(self, owner):
        """Sets the owner of the pet."""
        if isinstance(owner, Owner):
            self.owner_id = owner.id  # Assuming Owner has an id attribute
        else:
            raise TypeError("Expected an Owner instance")
