# Your code here

def hist(file):
    ignore = ['"', ":", ";", ",", ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"]
    cache = {}
    with open(file) as f:
        s = f.read()

    if s =='':
        return cache
    s = s.lower()
    s = s.replace('\r', ' ')
    s = s.replace('\n', ' ')
    s = s.replace('\t', ' ')
    words = s.split('   ')

    for w in words:
        for c in ignore:
            if c in w:
                w = w.replace(c, '')
        if w != '':
            if w in cache:
                cache[w] += 1
            else: 
                cache[w] = 1
    cache = {k: v for k, v in sorted(
    cache.items(), key=lambda item: item[0])}
    cache = {k: v for k, v in sorted(
    cache.items(), key=lambda item: item[1], reverse=True)}
    for key in cache:
        l = len(key)
        space = (20 - l)*' '
        print(key, space, cache[key]*'#')

hist('./robin.txt')