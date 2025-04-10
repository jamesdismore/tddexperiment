#A function called make_snippet that takes a string as an argument 
# and returns the first five words and then a '...' if there are more 
# than that.


def make_snippet(string):
    if len([x for x in string if x == ' ']) > 4:
        inc = 0
        pos = 0
        while inc <5:
            x = string.find(' ',pos)
            pos = x+1
            inc = inc+1
        firstpart = (string[0:pos-1])
        return firstpart + '...'
    else:
        return string

print(make_snippet('There are six words here actually'))

