class DynamicArray:
    def __init__(self, initial_capacity=2, increment=10):
        self.data = [None] * initial_capacity
        self.capacity = initial_capacity
        self.size = 0
        self.increment = increment

    def __len__(self):
        return self.size

    def __str__(self):
        return str([self.data[i] for i in range(self.size)])

    def resize(self):
        print(f"Resizing array from {self.capacity} to {self.capacity + self.increment}")
        new_data = [None] * (self.capacity + self.increment)
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity += self.increment

    def append(self, value):
        if self.size == self.capacity:
            self.resize()
        self.data[self.size] = value
        self.size += 1

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
