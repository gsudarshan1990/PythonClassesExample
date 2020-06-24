"""
Write a function def solution(S) that given a String S consisting of N lower case letters, returns the minimum number of letters that must be deleted
to obtain a word in which every letter occurs a unique number of times. We only care about occurences of letters that appear atleast once in result.

Given S="aaaabbbb", the function returns 1. We can delete one occurence of a or one occurence of b.Then onew letter will occur four times and the other three times

Given s="ccaaffddecee", the function should return 6. for example we can delete all occurences of e and f and one occurence of d to obtain the word ""ccaadc".Both e and f occur zero times in the new word,
but that is fine, since we only care about letters that appear atleast once

Given S="eeee", the function returns 0

Given S="example" the function returns 4

"""
def solution(S):
    if not S:
        return 0

    wordCount = {}
    for ch in S:
        wordCount[ch] =wordCount.get(ch,0)+1
    uniqueWordCount=[]
    removedCount = 0
    print(wordCount)
    for count in wordCount.values():
        while count > 0:
            if count not in uniqueWordCount:
                uniqueWordCount.append(count)
                break
            removedCount+=1
            count-=1
    print(removedCount)


solution("example")
solution("aaaabbbb")
solution("eeee")
solution("ccaaffddecee")