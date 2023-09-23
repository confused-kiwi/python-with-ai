fibonacci_seq = []
for n in range(0,50):
    if n == 0 :
        f = 0
    elif n == 1:
        f = 1
    else:
        f = fibonacci_seq[n-1] + fibonacci_seq[n-2]
    fibonacci_seq.append(f)

print(fibonacci_seq)


for j in range(2,len(fibonacci_seq),1):
    y = fibonacci_seq[j]/fibonacci_seq[j-1]
    print(f"{j} - {y}")