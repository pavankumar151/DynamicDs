import time
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
        print(f"Time taken for binary search: {end_time - start_time} seconds")

        
        self.data.insert(position, value)

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

def main():
    file_path = 'words.txt'  

  
    word_limit = 20  # Adjust this limit as needed

    print(f"\n--- Using Python List with a limit of {word_limit} words ---")
    words_list = load_words(file_path, limit=word_limit)
    
    print(f"Final list size: {len(words_list)}")
    print("First 10 words:", words_list.data[:10])

if __name__ == "__main__":
    main()
