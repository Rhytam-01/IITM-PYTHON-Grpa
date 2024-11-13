def longest_antakshari_subsequence(n: int, sequences: list) -> list:
    results = []
    
    # Iterate over each sequence
    for seq in sequences:
        words = seq.split(',')
        max_len = 1  # The minimum valid subsequence is a single word.
        current_len = 1  # Start with the first word
        
        # Iterate through the words and check for the antakshari property
        for i in range(1, len(words)):
            if words[i-1][-1] == words[i][0]:  # last letter of previous == first letter of current
                current_len += 1  # Extend the subsequence
            else:
                # Reset the current sequence length
                max_len = max(max_len, current_len)
                current_len = 1
        
        # Update the maximum length after the last word
        max_len = max(max_len, current_len)
        results.append(max_len)
    
    return results


# Input reading
n = int(input())  # Read the number of sequences
sequences = [input().strip() for _ in range(n)]  # Read all sequences

# Get the results
results = longest_antakshari_subsequence(n, sequences)

# Output the results
for result in results:
    print(result)
