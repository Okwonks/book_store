def logError(error):
  print(f'ERROR: {error}')
  
def logInfo(info):
  print(f'INFO:  {info}')

def main():
  
  try:
    # initialize books list
    bookList = []
    storedBooks = open('books.txt', 'r')
    line = storedBooks.readline()
    while line:
      bookList.append(line.strip('\n').split(','))
      line = storedBooks.readline()
    storedBooks.close()
  except FileNotFoundError:
    logError('<books.txt> file not found')
    logInfo('starting new <books.txt> file')
  
  choice = 0
  
  while choice != 4:
    print('*** Books Manager ***')
    print('1. Add a book')
    print('2. Look up a book')
    print('3. Display books')
    print('4. Quit')
    choice = int(input())
    
    if choice == 1:
      print('Adding a book...')
      nBook = input('Enter the name of the book >>> ')
      nAuthor = input('Enter the name of the author >>> ')
      nPages = input('Enter the number of pages >>> ')
      bookList.append([nBook, nAuthor, nPages])
    elif choice == 2:
      print('Looking up for a book...')
      keyword = input('Enter search term: ')
      for book in bookList:
        if keyword in book:
          print(book)
    elif choice == 3:
      print('Displaying all books...')
      for i in range(len(bookList)):
        print(bookList[i])
    elif choice == 4:
      print('Quitting...')
  print('Goodbye!')
  
  # save to external file
  outfille = open('books.txt', 'w')
  for book in bookList:
    outfille.write(','.join(book) + '\n')
  outfille.close()
  
if __name__ == '__main__':
  main()