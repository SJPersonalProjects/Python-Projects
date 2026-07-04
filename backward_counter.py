# Counts backwards using for range() in negative steps.

counter_starts = int(input("Start the backward counting from: "))

for i in range(counter_starts, 0, -1):
    print(i)

