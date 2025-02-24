# 순차검색과 이진검색의 성능 비교

import random

## 전역변수 선언 부분
dataAry , sortedAry = [],[]
findData = 7878
count = 0

## 클래스, 함수 선언부분
def seqSearch(ary, fdata):
    global count
    pos = -1
    for i in range(len(ary)):
        count += 1
        if ary[i] == fdata:
            pos = i
            break
    return pos

def binSearch(ary, fdata):
    global count
    start = 0
    end = len(ary) - 1

    while (start <= end):
        count +=1
        mid = (start + end) // 2
        
        if fdata == ary[mid]:
            return mid
        elif fdata > ary[mid]:
            start = mid + 1
        else: end = mid -1 

    return - 1

## 메인코드

dataAry = [random.randint(0, 999999) for _ in range(1000000)]
dataAry.insert(random.randint(0,1000000), findData)
sortedAry = sorted(dataAry)

print('#비정렬 배열(100만개) --> ', dataAry[0:5], '~~~', dataAry[-5:len(dataAry)])
print('#정렬 배열(100만개) --> ', dataAry[0:5], '~~~', sortedAry[-5:len(sortedAry)])

count = 0
pos = seqSearch(dataAry,findData)
if pos != -1:
    print(f'순차 검색(비정렬 데이터) -->{count} 회 입니다')

count = 0
pos = binSearch(dataAry,findData)
if pos != - 1:
    print(f'순차 검색(정렬 데이터) -->{count} 회 입니다')

