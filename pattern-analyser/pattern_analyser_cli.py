from collections import Counter
 
 
def count_bit_blocks(file_path, block_size):
    """
    Counts bit patterns of 'block_size' bits without overlapping.
    Optimized reading with bit register.
    """
 
    counter = Counter()
 
    register = 0
    bit_count = 0
 
    with open(file_path, "rb") as f:
 
        while True:
 
            chunk = f.read(4096)
 
            if not chunk:
                break
 
            for byte in chunk:
 
                # Add the 8 bits of the byte to the register
                register = (register << 8) | byte
                bit_count += 8
 
                # Extract complete blocks
                while bit_count >= block_size:
 
                    shift = bit_count - block_size
 
                    pattern = register >> shift
 
                    counter[pattern] += 1
 
                    bit_count -= block_size
 
                    mask = (1 << bit_count) - 1
                    register &= mask
 
    return counter
 
 
def main():
    # Get file path from user
    file_path = input("Enter the path to the binary file: ")
 
    # Get block size from user
    while True:
        try:
            block_size = int(input("Enter block size (2, 3, or 4): "))
            if block_size in [2, 3, 4]:
                break
            else:
                print("Please enter 2, 3, or 4")
        except ValueError:
            print("Please enter a valid number")
 
    # Analyze the file
    print("\nAnalyzing file...")
    counter = count_bit_blocks(file_path, block_size)
 
    total = sum(counter.values())
 
    # Display results
    print(f"\nFile: {file_path}")
    print(f"Block size: {block_size} bits\n")
 
    print(f"{'Pattern':<8}{'Occurrences':>12}{'Frequency':>15}")
    print("-" * 38)
 
    for i in range(2 ** block_size):
 
        pattern = format(i, f"0{block_size}b")
 
        count = counter[i]
 
        frequency = count / total if total else 0
 
        print(f"{pattern:<8}{count:>12}{frequency:>15.6f}")
 
    print("\n")
    print(f"Total number of blocks: {total}")
 
 
if __name__ == "__main__":
    main()
 
