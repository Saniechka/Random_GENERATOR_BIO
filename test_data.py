import random
import string
import hashlib
import time
import matplotlib.pyplot as plt

# Funkcja generująca losowy ciąg znaków o zadanej długości
def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

# Tablica stringów
strings1 = ["Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit"]

def generate_hash(strings):
    random_string_32 = generate_random_string(32)
    strings.append(random_string_32)
    random.shuffle(strings)
    concatenated_string = ''.join(strings)
    sha256_hash = hashlib.sha256(concatenated_string.encode()).hexdigest()
    return sha256_hash

def  generate_tocken():
    hash =generate_hash(strings1)
    random_hex = hash[-5:]
    if random_hex < '0x186A0': #zabiezpieczenie  przed mniejszymi liczbami ale co jak byb na początku było 0? to string i wklejac
        random_hex = hash[-6:]
        
    decimal_number = int(random_hex, 16)%1000000  
    return str(decimal_number).zfill(6)

def save_data(filename, data):
    with open(filename, 'a') as file:
        for item in data:
            file.write(str(item) + '\n')

def load_data(filename):
    with open(filename, 'r') as file:
        data = [int(line.strip()) for line in file]
    return data

# Plik, do którego będą zapisywane dane
filename = 'generated_numbers2.txt'
counter = 0
start_time = time.time()

# Wygenerowanie danych i zapisanie ich do pliku
for i in range(100000):
    random_int = generate_tocken()
    save_data(filename, [random_int])
    if len(random_int)!=6:
        counter= counter+1

excecute_time = time.time()- start_time

print(counter)
print(excecute_time)

# Wczytanie danych z pliku
data = load_data(filename)

# Wygenerowanie histogramu
plt.hist(data, bins=50, color='blue', edgecolor='black')
plt.title('Histogram wygenerowanych liczb')
plt.xlabel('Wygenerowana liczba')
plt.ylabel('Częstość')
plt.show()
