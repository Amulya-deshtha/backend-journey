#DAY 1: Python Basics+oops

#Python Basics:

#Write a function that checks if a number is even.
def is_even(n):
    return n%2==0


#Write a function that returns the largest of 3 numbers.
a,b,c=120,32,100
def largest_of_three(a,b,c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c
print(largest_of_three(a,b,c))

#Loop through a list and count even numbers.
l=[2,2,4,3,1,5,6]
def even_count_in_list(l):
    count = 0
    i=0
    while i<len(l):
        if l[i] % 2 == 0:
            count += 1
        i+=1
    return count
print(even_count_in_list(l))

#Testing Basics:

print(is_even(4))
print(largest_of_three(120, 32, 100))
print(even_count_in_list([2, 3, 45, 4, 5, 3, 2, 2, 8, 6]))

#Oops:

#Create a class:

#User
#attributes: name, email
#method: display_info()

class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
    def display_info(self):
        print(self.name,self.email)



#Testing:

user1 = User("Amulya", "amu@gmail.com")
user2 = User("Deshtha", "des@gmail.com")

user1.display_info()
user2.display_info()