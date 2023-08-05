def diamond_outline(diamond_size):
    for i in range(diamond_size,-1,-1):
        print(' '*i+'/',end='')
        print(' '*(diamond_size-i)*2+'\\')

    for i in range(0,diamond_size+1):
        print(' '*i+'\\',end='')
        print(' '*(diamond_size-i)*2+'/')
    
def diamond_inside(diamond_size):
    num = 1 
    for i in range(diamond_size,-1,-1):
        print(' '*i+'/'*num,end='')
        print('\\'*num)
        num+=1
    num-=1 
    for i in range(0,diamond_size+1):
        print(' '*i+'\\'*num,end='')
        print('/'*num)
        num-=1
        
if __name__=='__main__':
    n:int = 39 # number of diamond you want to generate
    for i in range(n):
        diamond_outline(i)
        print('\n')
        diamond_inside(i)
        print('\n')