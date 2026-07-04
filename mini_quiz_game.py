# Mini quiz game.

score = 0

print("====== Mini Python Quiz ======")

while True:
    capital_city = input("What's the capital city of Pakistan? ")
    if capital_city.lower() == 'islamabad':
        score += 1
    
    days_in_week = input("How many days are there in a week? ")
    if days_in_week == '7':
        score += 1
    
    provinces_in_Pakistan = input("How many provinces are there in Pakistan? ")
    if provinces_in_Pakistan == '5':
        score += 1
        
    if score == 3: 
        print(f"You answered all questions right, score is {score}")
        break
    else:
        score = 0
        print("Sorry, 1 answer is incorrect. To win, keep trying.") 

