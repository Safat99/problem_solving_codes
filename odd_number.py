#Create a list of all odd numbers between 1 and a max number.
#  Max number is something you need to take from a user using input() function

def odd_number(n):
        odd_numbers = list(range(1,n+1))
        for i in odd_numbers:
            if i % 2 == 0:
                odd_numbers.remove(i)
        return odd_numbers

if __name__== '__main__':
    n = int(input())
    odd_numbers = odd_number(n)
    print(odd_numbers) 