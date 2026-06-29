nums=[1,2,3,1,2]
# Initialize the result variable to 0 outside the loop
single_num = 0

# Loop through every number in your list
for num in nums:
    # XOR the current number with the running total
    single_num = single_num ^ num

# Print the final result after the loop finishes
print(single_num)

#in an array , in that array some elements would repeat twice or more but one among them only occurs once
 