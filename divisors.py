#asks for user to input number
#takes number and puts all numbers up to that number in list
#user number is % by number in number list
#if user % num == 0 add to new divisor list

def divisor():
    divisor_list= [1]
    user_num = int(input("Please enter a number: "))

    number_list = list(range(2, user_num + 1))

    for num in number_list:
        if user_num % num == 0:
            divisor_list.append(num)
    
    print(divisor_list)

if __name__ == '__main__':
    divisor()
