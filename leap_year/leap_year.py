def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    
    if year % 4 == 0:
        print("primeiro if")
        print(year % 100)
        if year % 100 != 0:
            print("segundo if")
            return True
        elif year % 400 == 0:
            print("terceiro if")
            return True   
    
    return False

print(is_leap_year(2000))
print(is_leap_year(2100))