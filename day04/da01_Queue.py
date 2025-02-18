# da01_Queue.py
# 큐 자료구조 구현


# 함수 선언
def isQueueFull():
    global SIZE, Queue, front, rear # 전역변수를 함수안에서 쓰려고 할때만! global 씀
    # 1. 가장 일반적 로직 -> 데이터 삽입을 다하고난다면, 삭제 후 빈자리에 값을 다시 집어넣을 수 없다.
    # if rear == SIZE - 1:
    #     return True
    # else:
    #     return False
    # 2. 개선로직
    if rear != SIZE - 1 :
        return False
    elif rear == SIZE - 1 and front == -1:
        return True
    else: # <-- 개선된 부분
        for i in range(front +1, SIZE): # 현재 +1 부분 -> 데이터가 있는 부분
            Queue[i-1] = Queue[i] # 데이터 빈자리에 첫번째 데이터를 옮김
            Queue[i] = None # 데이터를 옮긴 후 None 처리 -> for 문으로 인해 무한반복 -> 한마디로 순차적으로 앞으로 다 땡김

        front -= 1 #다옮기고나서 끝부분을 하나 씩 빼준다.
        rear -= 1
        return False


def isQueueEmpty():
    global SIZE, Queue, front, rear
    if front == rear: # rear가 앞 데이터부터 삭제되어 front와 동일 한 경우
        return True
    else:
        return False
    
def enQueue(data):
    global SIZE, Queue, front, rear
    if isQueueFull():
        print('Queue is Full')
    else:
        rear += 1 # enQueue 는 rear 를 1 증가
        Queue[rear] = data

def deQueue():
    global SIZE, Queue, front, rear
    if isQueueEmpty():
        print('Queue is empty')
        return None
    else:
        front += 1 # deQuquq 는 front 를 1 증가
        data = Queue[front]
        Queue[front] = None
        return data
    
def peek():
    global SIZE, Queue, front, rear
    if isQueueEmpty():
        print('Queue is empty')
        return None
    else:
        return Queue[front + 1] # Front에는 값이없어 1 뒤에 데이터를 본다.(1을 더하는것이아니다.)

# 초기화
SIZE = int(input('큐크기 입력 > '))
Queue = [None for _ in range(SIZE)]
front = rear = -1


## 메인 모듈
if __name__ == '__main__' : 
    while True:
        select = input('삽입(I) / 추출(E) / 확인(V) / 종료(Q) --> ').upper()
    
        if select == 'Q':
            break
        elif select == 'I':
            data = input('데이터 입력 > ')
            enQueue(data)
            print(f'큐 상태 : {Queue}')
        elif select == 'E':
            data = deQueue()
            print(f'추출 데이터 : {data}')
            print(f'큐 상태 : {Queue}')
        elif select == 'V':
            data = peek()    
            print(f'추출 데이터 : {data}')
            print(f'큐 상태 : {Queue}')

        else:
            print('나머지 동작')
