import time
def searcher():
    book = "this is nitesh kumar and i am coding now"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print('Your text is in the book')
        else:
            print('Your text is not in the book')

search = searcher()
print('search started')
next(search)
print('search done')
search.send('nitesh')
input = ('press any key')
search.send('coding')
input = ('press any key')
search.send('we')
input = ('press any key')
search.send('how')
input = ('press any key')
search.send('i')