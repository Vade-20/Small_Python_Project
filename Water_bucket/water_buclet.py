import curses
from curses import wrapper


GOAL = 4  # The exact amount of water to have in a bucket to win.
steps = 0  # Keep track of how many steps the player made to solve this.

class Bucket:
    def __init__(self,size:int,amount = 0):
        self.size = size
        self.amount = amount
        if self.amount>self.size:
            self.fill_the_bucket()
        
    def fill_the_bucket(self):
        self.amount = self.size
    
    def empty_the_bucket(self):
        self.amount = 0
    
    def pour_into_from_another_bucket(self,bucket):
        while bucket.amount != 0:
            if self.amount < self.size:
                self.amount += 1
                bucket.amount -= 1
            else:
                break
    
    def printing_bucket(self):
        amount = self.amount
        bucket = {0:' +----------+'}
        for i in range(1,self.size+1):
            level = str(i)+'|'
            if amount != 0:
                level += 'W'*10+'|'
                amount -= 1
            else:
                level += ' '*10+'|'
            bucket[i] = level
        return bucket   
            
        
    
def printing_material(stdsrc,buckets):
    stdsrc.clear()
    stdsrc.refresh()
    max_size = max([i.size for i in buckets])
    screen = ''
    stdsrc.addstr(f'Water Bucket Puzzle\nTry to get {GOAL}L of water into one of these buckets\nSTEPS: {steps}')
    for i in range(max_size,-1,-1):
        for bucket in buckets:
            bucket = bucket.printing_bucket()
            screen += bucket.get(i,' '*13)
            screen += ' '*3
        screen += '\n'
    stdsrc.addstr(5,0,screen)
    stdsrc.addstr('''
You can:
  (F)ill the bucket
  (E)mpty the bucket
  (P)our one bucket into another
  (Q)uit\n>''')
    stdsrc.refresh()

def win_condition(buckets):
    for i in buckets:
        if i.amount == GOAL:
            return True
    return False

@wrapper
def main(stdsrc):
    global steps
    
    curses.echo()
    b8 = Bucket(8)
    b5 = Bucket(5)
    b3 = Bucket(3)
    buckets = [b8, b5, b3]
    while True:
        printing_material(stdsrc,buckets)
        if win_condition(buckets):
            stdsrc.addstr(f'Good job! You solved it in {steps} steps!\n Press any key to exit')
            stdsrc.getch()
            quit()
        else:
            steps += 1
            
        ans = stdsrc.getstr().decode(encoding='utf-8').upper()[0]
        if ans not in ['F','E','P','Q']:
            continue
        elif ans == 'Q':
            print('Thank you for playing')
            quit()
        
        stdsrc.addstr(f"Select a bucket {','.join([str(i.size) for i in buckets])} or QUIT\n>")
        bucket_1 = stdsrc.getstr().decode(encoding='utf-8').upper()
        if bucket_1[0] == 'Q':
            print('Thank you for playing')
            quit()
            
        for i in buckets:
            if i.size==int(bucket_1):
                    bucket_1 = i 
                    break
        else:
            continue
        
        if ans == 'F':
            bucket_1.fill_the_bucket()
        elif ans == 'E':
            bucket_1.empty_the_bucket()
        elif ans == 'P':
            stdsrc.addstr(f"Select a bucket to pour into {','.join([str(i.size) for i in buckets])}\n>")
            bucket_2 = stdsrc.getstr().decode(encoding='utf-8')
            for i in buckets:
                if i.size==int(bucket_2):
                    i.pour_into_from_another_bucket(bucket_1)