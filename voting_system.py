# Voting System.

votes = {}

while True:
    candidate = input("Enter candidate name (q to quit): ")

    if candidate.lower() == 'q':
        break

    if candidate in votes:
        votes[candidate] += 1
    else:
        votes[candidate] = 1


print("\n==== Voting Results ====")

if len(votes) == 0:
    print("No votes were cast.")
else :
    for candidate in votes:
        print(f"{candidate}: {votes[candidate]} vote(s)")