
###################### Question 1 #####################################
# For a list of integers, return any set of two integers that sum to zero.
# Do not return any duplicate numbers (i.e. [1,-1], [-1,1])

# Input = [-1,3,4,5,1,-5, 3,0]
# Output =  [-1,1], [5,-5]

def two_sum_to_zero(lst):

    # go through the list and see if the negative of the number is in the rest of the list
    for i in range(len(lst) - 1):
        if -lst[i] in lst[i+1:]:
            print [lst[i], -lst[i]]

two_sum_to_zero([-1,3,4,5,1,-5, 3,0])


# Extra question

# For a list of integers, return any set of three integers that sum to zero.
# Do not return any duplicate numbers (i.e. [1,-1,0], [-1,0,1])

# Input = [-1,3,-2,4,1,-5,3,0]
# Output =  [-1,3,-2], [-1,-2, 3], [-1,1,0], [4,1,-5]

def three_sum_to_zero(lst):

    # go through list and see if the negative of the sum of two consecutive numbers is in the rest of thei list
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1)[i+1:]:
            two_sum = lst[i] + lst[j]
            if -two_sum in lst[j+1:]:
                print [lst[i], lst[j], -two_sum]


three_sum_to_zero([-1,3,-2,4,1,-5,3,0])


###################### Question 2 #####################################
# For a list of integers, return the max sum for a subsequence of numbers.

# Input = [-2,3,4,5,-1,-5, 3]
# Output = 12

def get_max_sum(lst):
    max_sum = 0
    total_sum = 0

    # go through the list and add each number to the total sum
    for num in lst:
        total_sum += num
        # if total sum is less than zero, set total sum to zero
        if total_sum < 0:
            total_sum = 0
        # if total sum is greater than the max_sum, make update the new max sum
        if total_sum > max_sum:
            max_sum = total_sum

    return max_sum

print get_max_sum([-2,3,4,5,-1,-5, 3])


# Runtime: O(n)
