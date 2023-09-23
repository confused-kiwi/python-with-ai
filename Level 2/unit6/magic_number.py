#   Magic Number 2.0
#  Luciana


def binarysearch(arr, low, high):
    global counter
    counter += 1
   
    if high > low:

        mid = (high + low) // 2
        
        display = f"""
            My guess is {arr[mid]}.
            I have {max_guesses - counter} guesses left.
            Is my guess too low (type L) or too high (type H)? If I got it, type (R).
            Then, press [ENTER]
           
            """
        response = input(display)
        if response == "R":
            print(f"I got it! My final guess was {arr[mid]}! I got it in {counter} attempt(s).")
            return high
       
        elif response == "L":
            binarysearch(arr, mid + 1, high)
       
        elif response == "H":
            binarysearch(arr, low, mid - 1)
   
    else:
        return f"I got it! My final guess is {arr[high]}, and I got it in {counter} tries."


counter = 0
min = 1 #  index 0
max = 100 #  index 99
max_guesses = 7


arr = list(range(min, (max + 1), 1))
#  print(arr)


text = f"""
    Please think of a integer from {min} to {max}.
    It is best to write it down.
    I, the program, will attempt to guess your integer within {max_guesses} guesses.
    In a bit, you will start.
    Have fun!
"""


print(text)


ready = input("     When ready, press [ENTER].")




print(binarysearch(arr, 0, len(arr) - 1))


