import curses
import webbrowsers

def main(win):
  while True:
    if win.getkey():
      while True:
        webbrowser.open("https://github.com/guppythegod")
        webbrowser.open("https://you-got-trolled.com")
    else:
      print "guppythegod was here"
      
curses.wrap(main)
