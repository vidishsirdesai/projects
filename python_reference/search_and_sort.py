# wip

class Search:

    def __init__(self, array, target):
        self.array = array
        self.target = target

    def linear_search(self):
        
        for i in range(len(self.array)):
            if self.array[i] == self.target:
                return f"Element found at index = {i}"
        
        return -1

    def binary_search(self):

        self.array.sort()

        print(self.array)
        
        start_index = 0
        end_index = len(self.array) - 1
        
        while start_index <= end_index:
            
            mid_index = (start_index + end_index)// 2

            if self.array[mid_index] == self.target:
                return f"Element found at index = {mid_index}"
            elif self.array[mid_index] < end_index:
                start_index = mid_index + 1
            else:
                end_index = mid_index - 1

        return -1
    

class Sort:

    def __init__(self, array):
        self.array = array

    def bubble_sort_ascending(self):

        for i in range(len(self.array) - 1):
            for j in range(len(self.array) - i - 1):
                if self.array[j + 1] < self.array[j]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
        
        return self.array


    def selection_sort(self):

        n = len(self.array)

        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.array[j] < self.array[min_index]:
                    min_index = j

            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
        
        return self.array

    def insertion_sort(self):

        for i in range(1, len(self.array)):
            key = self.array[i]

            j = i - 1
            while j >= 0 and key <= self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
            
            self.array[j + 1] = key
        
        return self.array

    def merge_sort(self, array):

        if len(array) <= 1:
            return array
        
        n = len(self.array)
        left_half = Sort.merge_sort(self.array[:n//2])
        right_half = Sort.merge_sort(self.array[:n//2])

        i, j = 0, 0
        result = []
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                result.append(left_half[i])
                i += 1
            else:
                result.append(right_half[i])
                j += 1
        
        if i < len(left_half):
            result += left_half[i:]
        else:
            result += right_half[j:]
        
        return result
    
import random
array = []

for i in range(20):
    i = random.randint(0, 20)
    array.append(i)

# # test search
# print(array)
# search_object = search_and_sort.Search(array, 4)
# search_result = search_object.binary_search()
# print(search_result)

# test sort
print(array)
sort_object = Sort(array)
sorted_array = sort_object.merge_sort(array)
print(sorted_array)
