# Take the input from standard input using input()
# and print the output according to the problem .

# Write your code here
def run_length_encode(number: str) -> str:
    # Start with the first character and initialize the count
    result = []
    count = 1
    for i in range(1, len(number)):
        if number[i] == number[i - 1]:
            count += 1
        else:
            result.append(f"{count} {number[i - 1]}")
            count = 1
    # Append the last sequence
    result.append(f"{count} {number[-1]}")
    
    return " ".join(result)

# Reading input and processing each line
n = int(input().strip())
for _ in range(n):
    number = input().strip()
    print(run_length_encode(number))
