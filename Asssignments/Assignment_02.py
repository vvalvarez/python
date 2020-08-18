# numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
# frequency
# for i in numbers:
#     if (i in numbers):
#         numbers[i]+=1
#         else:
#             numbers[i]=1
# most_used_num
# print("The most frequent number is {most_used_num} and it was {frequency} times repeated")

def most_used_num(numbers):
    frequency = 0
    for i in numbers:
        curr_frequency = numbers.count(i)
        if(curr_frequency>frequency):
            frequency = curr_frequency
            num = i
    print(f"The most frequent number is {num} and it was repeated {frequency} times")
numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
most_used_num(numbers)