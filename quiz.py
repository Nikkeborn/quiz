def quiz(start_range=1, stop_range=100, attempts=8, print_num=False):
   
    """
    Enter start_range=int to sign beginning of the range.
    Enter stop_range=int to sign end of the range.      
    Enter attempts=int to sign the number of attempts.
    Enter print_num=bool 'True' to cheat.   
    
    """
    from random import randrange        
    stop_r=stop_range+1
    n=randrange(start_range, stop_r)
    if print_num==True:
        print(n)        
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
###############################console_launch##########################################
###############################console_launch##########################################
###############################console_launch##########################################
if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Quiz')
    parser.add_argument('-start',action='store',dest='start_range',type=int,default=1,nargs='?',required=False,help='Input beginning number of the range')
    parser.add_argument('-stop',action='store',dest='stop_range',type=int,default=100,nargs='?',required=False,help='Input end number of the range')
    parser.add_argument('-a','--attempt',action='store',dest='attempts',type=int,default=8,nargs='?',help='Input number of attempts')
    parser.add_argument('-ch','--cheat',action='store_true',dest='print_num', required=False,help='Input to cheat')
#################################################################
    args = parser.parse_args()
##################################################################
    quiz(args.start_range,args.stop_range,args.attempts,args.print_num)