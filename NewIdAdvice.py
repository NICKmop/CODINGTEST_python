# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

import re

def wordCheck(strWord):
    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if strWord == "":
        strWord = 'a';
    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    elif len(strWord) <= 16:
        strWord = strWord[:15];
    return strWord;

def reCheck(str):
    strWord = wordCheck(str);
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    chword = strWord.lower();
    attach = '';
    cp = re.findall(r'[a-z0-9-_.]+', chword);
    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    for i in cp:
        attach += i;
    chwords = attach;
    chword = re.sub('(([.])\\2{1,})', '.', chwords);
    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    for i in range(len(chword) + 1):
        if chword[0] == '.':
            chword = chword[1:];
        elif i == len(chword):
            if chword[i-1] == '.':
                chword = chword[:i-1];
                return chword;
            
def changeWord(word):
    chword = reCheck(word);
    return chword;

def solution(new_id):
    chWord = changeWord(new_id);
    print(chWord)
    answer = ''
    return answer

data = "...!@BaT#*..y.abcdefghijklm.";
# data2 = "z-+.^.";
# data3 = "123_.def";
# data4 = '';
# data5 = '1234567890123456';
solution(data)