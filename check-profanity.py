import urllib.request

def read_text():
    quotes = open("movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()

def check_profanity():
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q=shit")
    output = connection.read()
    print("oi: " + str(output))

check_profanity()