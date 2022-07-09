class RSVP:
    def __init__(self):
        self.set = set()

    def RSVP_to_party(self, person):
        self.set.add(person)

    def remove_car(self, person):
        return self.set.remove(person)

    def size(self):
        return len(self.set)

    def __str__(self):
        return str(self.set)

RSVP_set = RSVP()
RSVP_set.RSVP_to_party("John")
RSVP_set.RSVP_to_party("Jane")
RSVP_set.RSVP_to_party("Jack")
RSVP_set.RSVP_to_party("Jill")
RSVP_set.RSVP_to_party("Joe")
print(RSVP_set) # {'John', 'Jane', 'Jack', 'Jill', 'Joe'}

RSVP_set.remove_car("Jack") # Jack is no longer attending the party.
print(RSVP_set) # {'John', 'Jane', 'Jill', 'Joe'}

