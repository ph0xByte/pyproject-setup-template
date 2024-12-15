import contextlib
import urllib


with contextlib.closing(urllib.urlopen("https://www.python.org/")) as front_page:
    for line in front_page:
        print(line)
