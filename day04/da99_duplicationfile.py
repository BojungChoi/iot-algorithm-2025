## 중복파일 이름 찾기(연습)
import os
## 함수 선언 부분 ##
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

## -------------------- 전역변수 선언 부분 -----------------##
memory = []
root = None
fnameAry = []
## -------------------- 메인 코드 부분 -----------------##
folderName = 'C:\Program Files\Common Files' # 지정한 폴더
for dirName,_, fnames in os.walk(folderName):# os.walk 함수는 지정폴더 및 그 하위폴더의 목록을 반환한다.
    for fname in fnames : # 결국 fnameAry 에는 지정한 폴더 및 하위폴더의 모든 파일 이름이 저장된다.
        fnameAry.append(fname)  # 지정한폴더의 파일 및 그 하위 폴더 목록들은 추출해서 fnameAry 배열에 저장한다
        print(len(fnameAry))

node = TreeNode() 
node.data = fnameAry[0]
root = node # 첫번째 파일 이름을 루트 노드로 지정한다
memory.append(node)

dupNameAry = [] # 중복되는 파일 이름을 저장할 배열을 준비한다.

for name in fnameAry[1:]:
    node = TreeNode()
    node.data = name

    curr = root
    while True:
        if name == curr.data:
            dupNameAry.append(name) # 중복된 파일 이름을 dupNameAry 배열에 계속 추가한다. 아직은 같은 파일 이름이 2회이상 들어갈수있다.
            break
        if name < curr.data:
            if curr.left == None:
                curr.left = node
                memory.append(node)
                break
            curr = curr.left
        else:
            if curr.right == None :
                curr.right = node
                memory.append(node)
                break
            curr = curr.right

dupNameAry = list(set(dupNameAry))

print(folderName, '및 그 하위 디렉터리의 중복된 파일 목록 -> ')
print(dupNameAry)
