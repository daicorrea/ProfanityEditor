import urllib

def read_text():
    quotes = open("movie_quotes.txt")
    contents_of_file = quotes.read()
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(txt_to_check):
    url = "http://www.wdylike.appspot.com/?q=" + (txt_to_check)
    connection = urllib.urlopen(url)
    output = connection.read()
    print(str(output))


read_text()