# da03_linear_list.pu
# 선형리스트 일반 구현
# 실제 파이썬이 이렇게 동작하는것이 아님!!!
# 배열(선형리스트)이 어떻게 동작하는지 로직을 파악하기위함임.
## 전역 변수 선언 부분
katok = [] # 빈 배열
select = -1 # -1:통과 1:추가 2:삽입 3:삭제 4:종료


## 함수 선언 부분
# 데이터 추가
def add_data(freind):
    katok.append(None)
    lenkatok = len(katok)
    katok[lenkatok -1] = freind

# 중간 데이터 삽입
def insert_data(pos, freied):        
    # 잘못된 인덱스를 넣었을때 예외처리 필요
    if pos < 0 or pos > len(katok):
        print ('실행할 범위를 벗어 났습니다.')
        return

    katok.append(None)
    lenkatok = len(katok)

    for i in range(lenkatok - 1, pos, -1): # 추가할 위치까지 데이터를 뒤로 이동
        katok[i] = katok[i - 1]
        katok[i - 1] = None

    katok[pos] = freied

# 데이터 삭제

def delete_data(pos):
    if pos <0 or pos >len(katok):
        print('데이터 삭제범위 벗어남')
        return
    lenkatok = len(katok)
    katok[pos] = None # 지정된 위치의 값을삭제

    for i in range(pos+1, lenkatok):
        katok[i - 1] = katok[i]
        katok[i] = None

    del(katok[lenkatok -1]) # 배열 맨 마지막 삭제

# 메인코드 영역
if __name__ == '__main__':

    while True:
        select = int(input('선택(1:추가, 2:삽입, 3:삭제, 4:종료)  > '))

        if select == 1:
            data = input('추가 데이터 -->')
            add_data(data)
            print(katok)
        elif select == 2:
            pos, data = input('삽입위치와, 데이터 입력 -->').split()
            pos = int(pos)
            insert_data(pos, data)
            print(katok)
        elif select == 3:
            pos = int(input('삭제 위치 -->'))
            delete_data(pos)
            print(katok)
        elif select == 4:
            break
        else:
            print('1 ~ 4 로 입력할 것')
            continue

