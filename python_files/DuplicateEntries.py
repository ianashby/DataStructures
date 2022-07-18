

entries = [
    '$12 @ Bob the Builder',
    '$34 @ John Smith',
    '$56 @ Jane Doe',
    '$78 @ John Smith',
    '$90 @ Jane Doe',
    '$12 @ Bob the Builder', # Duplicate
    '$34 @ John Smith',      # Duplicate
]

def remove_duplicates(entries):
    # Your code here.
    pass


def find_duplicates(entries):
    # Your code here.
    pass


print(remove_duplicates(entries)) # Should be ['$12 @ Bob the Builder', '$34 @ John Smith', '$56 @ Jane Doe', '$78 @ John Smith', '$90 @ Jane Doe']
find_duplicates(entries) # Should be ['$12 @ Bob the Builder', '$34 @ John Smith']