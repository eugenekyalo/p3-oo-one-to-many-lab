class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # List of pets owned

    def pets(self):
        """Returns all related pets."""
        return self._pets

    def add_pet(self, pet):
        """Adds a pet to the owner if it's a valid Pet instance."""
        if isinstance(pet, Pet):
            self._pets.append(pet)
        else:
            raise TypeError("Expected a Pet instance")

    def get_sorted_pets(self):
        """Returns pets sorted by name."""
        return sorted(self._pets, key=lambda pet: pet.name)
