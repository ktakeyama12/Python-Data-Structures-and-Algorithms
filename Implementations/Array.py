# Main Reference https://www.geeksforgeeks.org/implementation-of-dynamic-array-in-python/
# Python uses a dynamic array

import ctypes
# ctypes is a foreign function library for Python. It provides C compatible data types, and allows calling functions
# in DLLs or shared libraries. It can be used to wrap these libraries in pure Python


class DynamicArray(object):

    def __init__(self):
        self.n = 0  # Count actual elements (Default is 0)
        self.capacity = 1  # Default Capacity
        self.A = self.make_array(self.capacity)

    def __len__(self):
        """
        Return number of elements sorted in array
        """
        return self.n

    def __getitem__(self, k):
        """
        Return element at index k
        """
        if not 0 <= k < self.n:
            # Check it k index is in bounds of array
            return IndexError('K is out of bounds !')

        return self.A[k]  # Retrieve from the array at index k

    def append(self, ele):
        """
        Add element to end of the array
        """
        if self.n == self.capacity:
            # Double capacity if not enough room
            self._resize(2 * self.capacity)

        self.A[self.n] = ele  # Set self.n index to element
        self.n += 1

    def _resize(self, new_cap):
        """
        Resize internal array to capacity new_cap
        """

        B = self.make_array(new_cap)  # New bigger array

        for k in range(self.n):  # Reference all existing values
            B[k] = self.A[k]

        self.A = B  # Call A the new bigger array (important)
        self.capacity = new_cap  # Reset the capacity

    def make_array(self, new_cap):
        """
        Returns a new array with new_cap capacity
        py_object - All object types are extensions of this type. This is a
        type which contains the information Python needs to treat a pointer to an object as an object.
        """
        return (new_cap * ctypes.py_object)()


if __name__ == '__main__':
    arr = DynamicArray()
    arr.append(1)
    len(arr)
