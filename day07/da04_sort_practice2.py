import random
import time

def selectionSort(ary):
    n = len(ary)
    for i in range(0,n-1):
        minIdx = i
        for k in range(0,n-1):
            if (ary[minIdx] > ary[k]):
                minIdx = k
        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp

    return ary

def quicksort(ary):
    if len(ary) <= 1:
        return ary
    pivot = ary[len(ary)//2]
    equal = [a for a in ary if a == pivot]
    left = [a for a in ary if a < pivot]
    right = [a for a in ary if a > pivot]
    return quicksort(left) + equal + quicksort(right)

# countAry=[1000,10000,12000,15000]

# for count in countAry:
#     tempAry = [random.randint(10000,99999) for _ in range(count)]
#     selectAry = tempAry[:]
    
#     print('## 데이터 수 : ', count, "개")
#     start = time.time()
#     selectionSort(selectAry)
#     end = time.time()
#     print(f" 선택 정렬 --> {end-start:10.3f} 초")
#     start = time.time()
#     quickSort(selectAry)
#     end = time.time()
#     print(f'퀵 정렬 --> {end-start:10.3f} 초')
#     print()

#     count *=5


## 클래스화 해보기

class comp_performance:

    def __init__(self,func1,func2,testData = None):
        countAry = [1000,10000,12000,15000,20000]
        if testData:
            for data in testData:
                temp = [random.randint(10000,99999) for _ in range(data)]
                s = time.time()
                func1(temp)
                e = time.time()
                s2 = time.time()
                func2(temp)
                e2 = time.time()    
                print(f'{func1} 실행 결과 : \t\t{data}개 데이터 , \t{e-s:10.3f}초')
                print(f'{func2} 실행 결과 : \t{data}개 데이터 , \t{e2-s2:10.3f}초')
                
        else:
            for count in countAry:
                temp = [random.randint(10000,99999) for _ in range(count)]
                s = time.time()
                func1(temp)
                e = time.time()
                s2 = time.time()
                func2(temp)
                e2 = time.time()
                print(f'{func1} 실행 결과 : \t\t{count}개 데이터 , \t{e-s:10.3f}초')
                print(f'{func2} 실행 결과 : \t{count}개 데이터 , \t{e2-s2:10.3f}초')

testData = [1000,2000,3000,4000,5000]
comp_performance(quicksort,selectionSort)
comp_performance(quicksort,selectionSort,testData)

