def print_numbers(n):
    """
    Function for print Three for multiples of three, Five for multiples of five
    and ThreeFive for multiples of three and five.

    Args: 

        n - number

    Returns:

        None
    """
    if n % 3 == 0 and n % 5 == 0:

        print("ThreeFive") 

    elif n % 3 == 0:
        
        print("Three") 
    
    elif n % 5 == 0:
        
        print("Five") 
    
    else: 

        print(n)
    

if __name__ == "__main__":

    for n in range(1,100):

        print_numbers(n)

