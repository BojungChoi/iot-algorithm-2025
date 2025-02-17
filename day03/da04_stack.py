# da04_stack.py
# 스택 동작확인 구현

# 반복문에 사용되지않는 변수(i)는 _ 로 대체가능
SIZE = int(input('스택크기를 결정하시요 --> '))
stack = [None for _ in range(SIZE)]
top = -1

print(stack)

## 함수 선언
def isStackFull(): # 스택이 꽉 찼는지 확인하는 함수
    global SIZE, stack, top
    if (top == SIZE -1): # Full / 실무에서 쓰는 Stack 은 무제한
        return True
    else:
        return False
    
def isStackEmpty(): # 스택이 비었는지 확인
    global SIZE, stack, top
    if (top == -1): # Empty
        return True
    else:
        return False
def push(data): # 스택에 데이터 추가
    global SIZE, stack, top
    if isStackFull(): # isStackFull() == True 와동일
        print('Stack is Full!!')
        # return 생략
    else:
        top += 1
        stack[top] = data
def pop(): # Stack 에서 데이터 추출
    global SIZE, stack, top
    if isStackEmpty():
        print('현재 스택이 없어 더이상 POP 이 불가합니다.')
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return data
    
def peak(): # Stack의 top 위치의 데이터 확인(살짝보기)
    global SIZE, stack, top
    if isStackEmpty():
        print('현재 스택이 없습니다.')
        return None
    else:
        return stack[top]
    
## 메인 모듈 
if __name__ == '__main__':

    # while select != 'Q':
    while True:
        select = input('삽입(I) / 추출(E) / 확인(V) / 종료(Q) > ').upper()
        
        if select == 'Q':
            break
        elif select == 'I':
            data = input('입력 데이터 -> ')
            push(data)
            print(f'스택상태\n{stack}')
        elif select == 'E':
            data = pop()
            print(f'추출 데이터 -> {data}')
            print(f'스택상태 --> {stack}')
        elif select == 'V':
            data = peak()
            print(f'스택상태 --> {stack}')
        else:
            print('바보 입력오류~!')

print('스 택 종 료')