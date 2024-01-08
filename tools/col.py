def myzip(it1, it2):
    """
    Custom implementation of the zip function for two collections.
    """
    # Initialize iterators for the two collections
    iter1 = iter(it1)
    iter2 = iter(it2)
    
    # Continue iterating until either of the iterators is exhausted
    while True:
        try:
            # Get the next elements from both iterators
            element1 = next(iter1)
            element2 = next(iter2)
            
            # Yield a tuple containing the elements from both collections
            yield (element1, element2)
        except StopIteration:
            # If either iterator is exhausted, stop the iteration
            break

# Example usage
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

result = list(myzip(list1, list2))
print(result)
