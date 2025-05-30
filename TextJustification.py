# words = input()
words1 = ["This", "is", "an", "example", "of", "text", "justification."]
words2 = ["What","must","be","acknowledgment","shall","be"]
words3 = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxw1 = 16
maxw2 = 16
maxw3 = 20

def justify(words, maxWidth):
    result = []
    i = 0

    while i < len(words):
        lineLength = 0
        curr = i
        while curr < len(words):
            if lineLength + len(words[curr]) + (curr - i) > maxWidth:
                break
            lineLength += len(words[curr])
            curr += 1

        noow = curr - i
        howmuchspace = maxWidth - lineLength

        line = ""

        if curr == len(words) or noow == 1:
            line = " ".join(words[i:curr])
            line += " " * (maxWidth - len(line))
        else:
            spaces = noow - 1
            minspace = howmuchspace // spaces
            extraSpace = howmuchspace % spaces

            for k in range(i, curr - 1):
                line += words[k]
                addspace = minspace + (1 if k - i < extraSpace else 0)
                line += " " * addspace
            line += words[curr - 1]
        

        result.append(line)
        i = curr

    return result

print("[")
for line in justify(words3, maxw3):
    print(line)
print("]")

'''
https://chatgpt.com/share/6839bbc7-498c-8005-82b3-c4f0d9c76464
'''