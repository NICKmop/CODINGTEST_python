from ntpath import join
from pymysql import NULL

def checkWithNumber(word):
    
    attachWord = '';
    wordBox = '';
    NumberBox = 0;

    for i in word:
        attachWord += i;
        if attachWord == "zero":
            wordBox += attachWord;
            attachWord = "";

        elif attachWord == "one":
            wordBox += attachWord;
            attachWord = "";
        elif attachWord == "two":
            wordBox += attachWord;
            attachWord = "";
        elif attachWord == "three":
            wordBox += attachWord;
            attachWord = "";
        elif attachWord == "four":
            wordBox += attachWord;
            attachWord = "";
        elif attachWord == "five":
            wordBox += attachWord;
            attachWord = "";
        elif attachWord == "six":
            wordBox += attachWord;
            attachWord = "";
        elif attachWord == "seven":
            wordBox += attachWord;
            attachWord = "";
        elif attachWord == "eight":
            wordBox += attachWord;
            attachWord = "";
        elif attachWord == "nine":
            wordBox += attachWord;
            attachWord = "";
        elif attachWord == "4":
            wordBox += attachWord;
            attachWord = "";
            # attachWord = "";

    return wordBox;


def solution(s):
    checkWithNumber(s);
    answer = 0
    return answer

# "one4seveneight"	1478
# "23four5six7"	234567
# "2three45sixseven"	234567
# "123"	123

solution("one4seveneight");