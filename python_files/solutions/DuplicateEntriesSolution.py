

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
    return list(set(entries))


def find_duplicates(entries):
    unique_vals = set()
    duplicates = set()

    for entry in entries:
        if entry in unique_vals:
            duplicates.add(entry)
        else:
            unique_vals.add(entry)

    print(duplicates)


print(entries)
print(remove_duplicates(entries)) # Should be ['$12 @ Bob the Builder', '$34 @ John Smith', '$56 @ Jane Doe', '$78 @ John Smith', '$90 @ Jane Doe']


find_duplicates(entries) # Should be ['$12 @ Bob the Builder', '$34 @ John Smith']