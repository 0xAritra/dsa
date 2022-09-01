# Let us say your expense for every month are listed below,
#     January - 2200
#     February - 2350
#     March - 2600
#     April - 2130
#     May - 2190

# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

expense = [2200, 2350, 2600, 2130, 2190]

# 1
print(expense[1] - expense[0])

# 2
print(expense[0] + expense[1] + expense[2])

# quarter = 1
# q_expense = 0
# for i in range((quarter - 1) * 3, quarter * 3):
#   q_expense += expense[i]
# print(q_expense)

# 3
print(2000 in expense) 

# target = 2000
# for i in range(len(expense)):
#   if expense[i] == target:
#     print(i)


# 4
expense.append(1980)

# 5
expense[3] = expense[3] - 200

# 
# print(expense)