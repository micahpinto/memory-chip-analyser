file_name = input("Enter the name of the .bin file: ")
 
with open(file_name, 'rb') as file:
    data = file.read()
 
# Convert bytes to hexadecimal, then to integer, then to binary string
binary_data = bin(int(data.hex(), 16))[2:]
 
# Count the number of 0s and 1s in the binary representation
count_0 = binary_data.count('0')
count_1 = binary_data.count('1')
 
# Calculate the percentage of 1s
total_bits = count_0 + count_1
percentage_1 = (count_1 / total_bits) * 100
 
print(f"Percentage of Erasure: {percentage_1:.2f}%")
