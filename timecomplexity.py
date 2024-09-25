import time
import sys
import bisect

class DynamicList:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)

    
    def binary_search_insert(self, value):
        start_time = time.time()


        position = bisect.bisect_left(self.data, value)

        
        end_time = time.time()
        print(f"Time taken for binary search: {end_time - start_time:.6f} seconds")

        
        self.data.insert(position, value)

        
        self.print_elements_at_increase()

    def print_elements_at_increase(self):
        n = len(self.data)
        if n > 0:
            first = self.data[0] if n > 0 else None
            quarter = self.data[n // 4] if n >= 4 else None
            half = self.data[n // 2] if n >= 2 else None
            three_quarters = self.data[3 * n // 4] if n >= 4 else None
            last = self.data[n - 1] if n > 0 else None
            
            print(f"Current size: {n}, Elements: {first} -> {quarter} -> {half} -> {three_quarters} -> {last}")

def load_words(file_path, limit=None):
    words_list = DynamicList()
    
    with open(file_path, 'r') as file:
        count = 0
        for line in file:
            if limit is not None and count >= limit:
                break
            word = line.strip()
            words_list.binary_search_insert(word)
            count += 1
            
    return words_list

def measure_performance(file_path, limit=None):
    start_time = time.time()
    words_list = load_words(file_path, limit)
    end_time = time.time()

    elapsed_time = end_time - start_time
    memory_usage = sys.getsizeof(words_list.data)  
    
    print(f"\nElapsed Time: {elapsed_time:.6f} seconds")
    print(f"Memory Usage: {memory_usage} bytes")
    
    return elapsed_time, memory_usage

def main():
    file_path = 'words.txt'  
    word_limit = 100  

    print(f"\n--- Measuring Performance for {word_limit} words ---")
    measure_performance(file_path, limit=word_limit)

if __name__ == "__main__":
    main()
