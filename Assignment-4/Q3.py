import numpy as np

# Sample genomic data (DNA sequence): A NumPy array of DNA base pairs (A, T, C, G)
dna_sequence = np.array(['A', 'T', 'G', 'C', 'A', 'G', 'T', 'A', 'C', 'G', 'T', 'A', 'A', 'G', 'C', 'T', 'G', 'G', 'G'])

# 1. Counting the frequency of each base (A, T, C, G)
unique, counts = np.unique(dna_sequence, return_counts=True)
base_frequencies = dict(zip(unique, counts))

print("Base Frequencies:")
for base, count in base_frequencies.items():
    print(f"{base}: {count}")

# 2. Finding the most common base
most_common_base = unique[np.argmax(counts)]
print(f"\nMost Common Base: {most_common_base}")

# 3. Finding base pair sequences longer than a specified threshold
def find_long_sequences(sequence, base, threshold):
    """Find sequences of consecutive base pairs longer than the threshold."""
    long_sequences = []
    current_sequence = []
    
    for bp in sequence:
        if bp == base:
            current_sequence.append(bp)
        else:
            if len(current_sequence) > threshold:
                long_sequences.append(current_sequence.copy())
            current_sequence = []
    
    # Check at the end of the sequence
    if len(current_sequence) > threshold:
        long_sequences.append(current_sequence.copy())
    
    return long_sequences

threshold = 2  # Define threshold for sequence length
long_sequences = {base: find_long_sequences(dna_sequence, base, threshold) for base in unique}

print("\nLong Base Pair Sequences (longer than threshold):")
for base, sequences in long_sequences.items():
    if sequences:
        print(f"{base}: {[''.join(seq) for seq in sequences]}")

# 4. Reversing the entire DNA sequence
reversed_sequence = np.flip(dna_sequence)
print("\nReversed DNA Sequence:")
print(''.join(reversed_sequence))