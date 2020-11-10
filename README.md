## Diving into the nook and cranny of an awesome language - PYTHON

### EPAi Session 14

### Understanding Iterables and Iterators

### We looked over :

- List Comprehensions
- Iterating Collections
- Iterators
- Iterators and Iterables
- Consuming Iterators Manually
- Cyclic Iterations
- Lazy Iterables
- In-Built Iterables
- Sorting Iterables
- The iter() function
- Iterating Callables
- Delegating Iterators
- Reversed Iteration
- Using Iterators as function arguments

Iterator is an object which is used to iterate over an iterable object using **next**() method.

Iterable is an object that implements __iter__ method and method returns an iterator that can be used to iterate over the object using **next**()

Lazy Execution is when variables used in the generator expression are evaluated lazily in a separate scope when the next() method is called. i.e only be loaded at the time of retrieval.

---

### Assignment

```
Goal 1

Refactor the Polygon class so that all the calculated properties are lazy properties, i.e. they should still be calculated properties, but they should not have to get recalculated more than once (since we made our Polygon class "immutable").

Goal 2

Refactor the Polygons (sequence) type, into an iterable. Make sure also that the elements in the iterator are computed lazily - i.e. you can no longer use a list as an underlying storage mechanism for your polygons.

You'll need to implement both an iterable, and an iterator.

```

### Modules 

- polygon : polygon class with basic gt and eq functionality
- polygon sequence/iterable : class which implements a custom sequence for polygons

Notebook attached tests the functionality of the modules and showing lazy excecution.