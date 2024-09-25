class DynamicArray:
    def __init__(self, initial_capacity=2):
        self.data = [None] * initial_capacity
        self.capacity = initial_capacity
        self.size = 0
        self.prev_capacity = 1  

    def __len__(self):
        return self.size

    def __str__(self):
        return str([self.data[i] for i in range(self.size)])

    # Resize the array using Fibonacci sequence
    def resize(self):
        new_capacity = self.capacity + self.prev_capacity 
        print(f"Resizing array from {self.capacity} to {new_capacity}")
        
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        
        self.prev_capacity = self.capacity  
        self.capacity = new_capacity  
        self.data = new_data

    def append(self, value):
        if self.size == self.capacity:
            self.resize()
        self.data[self.size] = value
        self.size += 1

    # Sort the dynamic array
    def sort(self):
        self.data = sorted(self.data[:self.size])

def load_words(file_path):
    words_array = DynamicArray()
    
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip()
            words_array.append(word)
    
    return words_array

def main():
    file_path = 'words.txt'

    words_array = load_words(file_path)
    words_array.sort()

    print(f"Final array size: {len(words_array)}")
    print("First 10 words:", words_array.data[:10])

if __name__ == "__main__":
    main()
