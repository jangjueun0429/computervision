# 일부러 만든 정적 분석용 테스트 파일
import os

def hello_world():
    unused_variable = 42  # 사용하지 않는 변수 (Code Smell 유도)
    print("Hello World")

    if True:   # 무조건 참인 조건문 (Code Smell 유도)
        print("Test")

hello_world()
