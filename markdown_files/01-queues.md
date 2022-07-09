# **Data Structure 01: Queues**
*Ian Ashby*
*07/02/2022*

---

## **Introduction**
#### Purpose

Queues are often referred to as a "First in, first out" (FIFO) data structure and can be implemented in Python using lists. Being a FIFO data structure means that the first element that is added to the queue will be the first one to removed. 

We can see this illustrated in **Figure 1** where the first element is enqueued, or added to the queue. As more elements are enqueued, the first and the following elements are shifted. When an element is dequeued, or removed from the queue, it is removed from the beginning of the queue.

<!-- Queue GIF -->
<figure>
<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--LTu3kVda--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://1.bp.blogspot.com/-N-v_FiIdQXM/XlkFCQQYtPI/AAAAAAAAHR0/zxkuX6WfQS8Y8Mkoj1nHZDWtMOD3MjsUwCLcBGAsYHQ/s1600/0_E33E-AjyAUTFjVmM.gif">
<figcaption align = "center">Figure 1: Basic queue operations. <a href="https://dev.to/adavidoaiei/fundamental-data-structures-and-algorithms-in-c-4ocf">Image Source</a></figcaption>
</figure>

#### Operations & Big O

Queues have multiple operations that allow us to add and remove values from a queue. There are also processes to help us determine a queues size and whether it is empty. We will go over each of these operations and discuss their Big O performance below:

###### Enqueue O(1)

If we want to add a value to a queue, we will *enqueue* a value to the queue. This operation yields a Big O performance of O(1) since we are only adding to the end of a dynamic array. We can dequeue values in Python like this:

```python
def enqueue(value, queue):
    return queue.append(value)
```

###### Dequeue O(n)

If we want to remove a value from a queue, we will *dequeue* the first value from the queue. This operation yields a Big O performance of O(n) since we are removing from the start of the dynamic array. We can enqueue values in Python like this:

<!-- LINKED LIST IS 0(1), explain that o(n) is for dynamic array and is easier -->

```python
# Example 01
def dequeue(queue):
    value = queue[0]
    del queue[0]
    return value

# Example 02
def dequeue(queue):
    return queue.pop(0)
```

###### Size O(1)

We can also find the length or size of a queue. This operation yields a Big O performance of O(1) since we are simply counting each element in the dynamic array. We can find the size of a queue in Python like this:

```python
def length(queue):
    return len(queue)
```

###### Empty O(1)

We can also determine whether a queue is empty. This operation yields a Big O performance of O(1) since we are simply counting each element in the dynamic array. We can find this in Python like this:

```python
def is_empty(queue):
    return len(queue) == 0
```

### Common errors

***Add work here.*** What are some common errors with queues?

<!-- Implemented a queue with a dynamic array -->
<!-- Correct order -->

## Real world example

Now that we have a basic understanding of what a queue is as well as various operations a queue can perform, lets take a look at a real-world example of a queue.

I like to think of a queue like a car wash. Order matters at a car wash. The first car in line is the first car to be washed and to exit the car wash. It would be hard to rearrange the order of the cars and we would not expect to do so. There is a determined order that promotes efficiency and organization. 

## Coding example

Following the idea of a queue being similar to a car wash, lets create a simple program that adds a car to a queue and then removes them once they have gone through the car wash.

```python
class CarWash:
    def __init__(self):
        self.queue = []

    def add_car(self, car):
        self.queue.append(car)

    def remove_car(self):
        return self.queue.pop(0)

    def length(self):
        return len(self.queue)
     f __str__(self):
        return str(self.queue)

car_wash = CarWash()
car_wash.add_car('BMW')
car_wash.add_car('Audi')
car_wash.add_car('Mercedes')
car_wash.add_car('Ferrari')
# print(car_wash) ['BMW', 'Audi', 'Mercedes', 'Ferrari']
car_wash.remove_car()
# print(car_wash) ['Audi', 'Mercedes', 'Ferrari']
```

## Problem set

Now it's your turn! The car wash informs you that no more than 10 cars can be in line at a time. Can you add functionality to implement this?

<!-- Add in downloadable file -->
<!-- What is this ds good at? used for commonly? -->