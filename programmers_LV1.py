import re
# 1478 → "one4seveneight"
# 234567 → "23four5six7"
# 10203 → "1zerotwozero3"
# s	                result
# "one4seveneight"	1478

word = ["zero","one","two","three","four","five","six","seven","eight","nine"];
num = ['0','1','2','3','4','5','6','7','8','9'];

def solution(s):
    attachBox = '';
    tooBox = [];
    answer = '';

    for words in s:
        attachBox += words;
        for i in range(0,len(word)):
            if attachBox == word[i]:
                tooBox.append(attachBox);
                attachBox = attachBox[len(attachBox):];
            elif (attachBox >= '0' and attachBox <= '9'):
                tooBox.append(attachBox);
                attachBox = attachBox[len(attachBox):];

    for tooBoxs in range(len(tooBox)):
        for nums in zip(word,num):
            if tooBox[tooBoxs] == nums[0]:
                answer += nums[1];
            else:
                answer += tooBox[tooBoxs];

    #     print(nums[1]);
    #     if nums[0] == 
    print(answer);


solution(s="1zerotwozero3");