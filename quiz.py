def quiz(start_range=1, stop_range=100, attempts=8, print_num='no'):
   
    """
    Enter start_range=int to sign beginning of the range.
    Enter stop_range=int to sign end of the range.      
    Enter attempts=int to sign the number of attempts.
    Enter print_num=str 'yes' to cheat.   
    
    """
    from random import randrange        
    stop_r=stop_range+1
    n=randrange(start_range, stop_r)
    #return n
    if print_num=='no':
        pass
    elif print_num=='yes':
        print(n)
    else:
        pass
    while True:
        m=input('Enter\'stop\' to STOP'+f'\nYou have {attempts} attempts.'+f'\nGuess the number from {start_range} to {stop_range}: ')
        if m=="stop":
            break
        elif False==m.isdigit():
            print(f'"{m}" is not a number')
            attempts-=1
        else:
            if n==int(m):
                print('Congratulations you are win!!!)))')
                break
            elif n<int(m):
                print(f'Your numbel {m} is too big (')
                attempts-=1
            else:
                print(f'Your number {m} is too small (')
                attempts-=1
        if attempts==0:
            print (f'You have no more attempts. You lost (((\nNumber was {n}')
            break
if __name__=='__main__':
    quiz(1,100,8,'yes')
        