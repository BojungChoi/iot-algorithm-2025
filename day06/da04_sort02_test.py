## 중앙값 계산(선택정렬)
def selectionSort(ary):
    n = len(ary)
    for i in range(0, n-1):
        minIdx = i
        for k in range(i+1, n) :
            if (ary[minIdx] > ary[k]):
                minIdx = k
        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp
        
        print(f'정렬중 --> {ary}')
        # ary[minIdx],ary[k] = ary[k], ary[minIdx] #-> 이부분은 다시연습해보기

    return ary
    
# 전역 변수 선언 부분

moneyAry = [7, 5, 11, 6, 9, 80000, 10, 6, 15, 12]

# 메인코드 

print(f'정렬 전 -->{moneyAry}')

moneyAry = selectionSort(moneyAry)
print(f'정렬 후 -->{moneyAry}')

print(f'중앙 값 -->{len(moneyAry)//2}')


