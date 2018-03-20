try:
   number = int(input('Enter a number: '))
   print(number)
   aFile = open ('module.py')
   print(aFile.readline())

except ValueError:
   print(' Not a number, please re-enter: ')
   number = int(input('Enter a number: '))

except IOError:
  print ('Can not open file')
print ('finish')