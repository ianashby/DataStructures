# **Data Structure 02: Sets**

* [Welcome](/markdown_files/00-welcome.md)
* [Queues](/markdown_files/01-queues.md)
* [Sets](/markdown_files/02-sets.md)
* [Trees](/markdown_files/03-trees.md)

---

## **Introduction**

Location and order are not as vitally important in some data structures in the way that they are for lists, stacks, and queues. The set data structure does not rely on location or order to efficiently perform operations. 

At first, one may think this would cause disorder and disorganization; however, it is important to understand how a set works. The first thing to understand about a set is that duplicate entries are not allowed. Since order and duplicates are not allowed, a set utilizes hashing to perform all of its common operations in O(1) performance. 

Hashing is the processing of turning an element into a unique number. The number is used to index into a our set data structure. The hashed number is then used to determine if an element is in the set as well as being able to quickly find its location.

This also means that each unique element in the set will have a unique hash value. This is important because it allows us to quickly find the location of an element in the set. 

What happens when we try to add an element to the set that is already in the set? We can utilize the open addressing method to resolve this issue which tells us to check the next location in the set. This can result in more conflicts, however. A second option for conflict resolution is to use a method called chaining. This involves creating a list of values that occupy the same hash index. This would mitigate any conflicts that may arise. If we have too many conflicts, our performance may suffer, so it is important to be mindful of this.

---

## **Operations & Big O**

Sets have multiple operations that allow us to add and remove values from a set. There are also processes to help us determine a set's size and whether it is empty. We will go over each of these operations and discuss their Big O performance below:

###### Add O(1)

Adding to a set yields a Big O performance of O(1) since we are relying on the hashing to give us good performance. We can add values to a set in Python like this:

```python
def add_value(set, value):
    return set.add(value)
```

###### Remove O(1)

Removing from a set also yields a Big O performance of O(1) since we are, again, relying on the hashing to give us good performance. We can remove values from a set in Python like this:

```python
def remove_value(set, value):
    return set.remove(value)
```

###### Membership O(1)

Checking if a value is in a set yields a Big O performance of O(1) since we are, again, relying on the hashing to give us good performance. The result will be a Boolean expression. We can check set membership in Python like this:

```python
def is_member(set, value):
    return value in set
```

###### Size O(1)

We can also find the length or size of a set. This operation yields a Big O performance of O(1) since we are simply counting each element in the set. We can find the size of a set in Python like this:

```python
def set_size(set):
    return len(set)
```

---

## Real world example

Now that we have a basic understanding of what a set is as well as various operations a set can perform, lets take a look at a real-world example utilizing a set.

One way that I like to think of a set is like an RSVP list to a party. Obviously, you cannot have people RSVP more than once, so they should only show up on the set once. Additionally, in most cases, order does not matter. 

Once a person RSVPs to a party, they are added to the set. If they can't come anymore, they are removed. If someone can't remember if they have already RSVP'd and they try to again, nothing will change.

---

## Coding example

Following the idea of a set being similar to a RSVP list, lets create a simple program that adds a person to a set if they RSVP and then removes them if they can longer come.

```python
class RSVP:
    def __init__(self):
        self.set = set()

    def RSVP_to_party(self, person):
        self.set.add(person)

    def cancel_RSVP(self, person):
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
RSVP_set.cancel_RSVP("Jack") # Jack is no longer attending the party.
print(RSVP_set) # {'John', 'Jane', 'Jill', 'Joe'}
```

---

## Problem set

Now it's your turn! Suppose your boss gives you a list of transactions that he wants you to go through. He typed the list up himself and is sure there are duplicate entries. Can you find what entries may be a duplicate by adding them to a set? Can you also give him a clean list of unique entries?

You can find the [work file here](../python_files/DuplicateEntries.py) and the [sample solution here](../python_files/solutions/DuplicateEntriesSolution.py). 