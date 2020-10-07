ignore = ['"', ":", ";", ",", ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"]

def remove_char(s):
    word = s
    for i in ignore:
        word = word.replace(i,'')
    return word

def word_count(s):

    words = s.lower().split()
    no_spec_chars = []
    words_count={}

    for w in words:
        no_spec_char = remove_char(w)
        no_spec_chars.append(no_spec_char)
    
    for w in no_spec_chars:
        if w not in words_count:
            words_count[w] = 0
        count = no_spec_chars.count(w)
        words_count[w] = count

    if len(no_spec_chars) > 0:
        if no_spec_chars[0] == "":
            return {}
    return words_count







# ///////////////////////////////////////////////////
    # for c in s:
    #     if c.isalpha() or c == "'":
    #         c = c.lower()
    #         word += c
    #     elif word == '':
    #         pass
    #     else:
    #         if word not in count:
    #             count[word] = 0
    #         count[word] += 1
    #         word = ''

    #     if word != '':
    #         if word not in count:
    #             count[word] = 0
    #         count[word] += 1
        
    #     return count

    # ////////////////////////////////
    # list_of_words = {}
    # excluded = '":;,.-+=/\\|[]{}()*^&'
    # if s =='':
    #     return list_of_words
    # s = s.lower()
    # s = s.replace('\r', ' ')
    # s = s.replace('\n', ' ')
    # s = s.replace('\t', ' ')
    # words = s.split(' ')


    # for word in words:
    #     for char in excluded:
    #         if char in word:
    #             word = word.replace(char, '')
    #     if word != '':
    #         if word in list_of_words:
    #             list_of_words[word] += 1
    #         else:
    #             list_of_words[word] = 1
    #     return list_of_words
    
    # ////////////////////////////////////////////////
    # lower = s.lower()
    # # print(lower)
    # words = lower.split(' ')
    # # print(words)
    # word_hash = {}

    # for word in words:
    #     if word != word_hash:
    #         word_hash[word] += 1
    # return word_hash
        

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))