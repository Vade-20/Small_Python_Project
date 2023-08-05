while True:
    print('Do you want to know how to keep a gullible person busy for hours? Y/N')
    ans = input('>')
    if ans.lower().startswith('y'):
        continue
    elif ans.lower().startswith('n'):
        break
    else:
        print(f'{ans} is not a valid command.\nPlease enter Y for yes and N for no')
        
print('Thank you. Have a nice day!')