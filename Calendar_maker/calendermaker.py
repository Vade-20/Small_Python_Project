import datetime
import calendar

weeks = {1:'Monday',
         2.:"Tuesday",
         3:'Wednesday',
         4:'Thursday',
         5:'Friday',
         6:'Saturday',
         7:'Sunday'}

month_names = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}


def list_of_days(year,month):
    a = datetime.date(year,month,1)
    day = a.isoweekday()
    num_of_days = []
    for i in range(1,day):
        num_of_days.append('')
    for i in range(1,calendar.monthrange(a.year,a.month)[1]+1):
        num_of_days.append(str(i))
    while len(num_of_days)%7!=0:
        num_of_days.append('')
    return num_of_days 
        
def printing(year,month):
    print(f'{month_names.get(month)} of {year}'.center(105))
    print('\n')
    num_od_days = list_of_days(year,month)
    if len(num_od_days)>35:
        num_of_row = 6
    elif len(num_od_days)<28:
        num_of_row = 4
    else:
        num_of_row = 5
        
    var = 0
    for i in weeks.values():
        print(f'{i}'.center(16),end='')
    print()
    
    for ___ in range(num_of_row):
        print(('+'+'-'.ljust(15,'-'))*7,end='')
        print('+')
        for k in range(5):
            if k!=2:
                for _ in range(7):
                    print('|'.ljust(16),end='')
                print('|')
            else:
                for _ in range(7):
                    print('|',end='')
                    print(num_od_days[var].center(15),end='')
                    var += 1
                print('|')        
    print(('+'+'-'.ljust(15,'-'))*7,end='')
    print('+')

if __name__=='__main__':
    while True:
        year = input('Please enter the year : ')
        if not year.isdigit():
            continue
        elif int(year)<0:
            continue
        year = int(year)
        break
    
    while True:
        month = input('Please enter the month : ')
        if not month.isdigit():
            continue
        elif int(month) not in range(1,13):
            continue
        month = int(month)
        break
    printing(year,month)
    
    
    
    