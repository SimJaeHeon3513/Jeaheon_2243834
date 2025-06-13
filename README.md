# 만든 목적
원래 게임을 좋아하고 코딩을 시작하게 된 계기가 게임을 만들고 싶었기 때문에 기말고사 프로젝트 기회를 통해 간단한 게임을 만들어 보기 위함

# 실행 방법
1. cmd창을 열어 'pip install pygame' 명령어로 pygame 라이브러리를 설치
2. vscode를 열고 game.py의 코드를 복사하여 실행

# 게임 설명 및 조작법  
                          ===피하기 게임===  
화면 위에서 떨어지는 빨간색 장애물을 피해 오랫동안 살아남는 것이 목표인 게임

특징: 빨간색 장애물은 시간이 지날수록 속도가 빨라짐  
조작법: 좌우 방향키

코드 설명
1. #라이브러리 import  ![image](https://github.com/user-attachments/assets/7f322e06-a148-46b8-b989-7b9af82941b4)
2. #초기 설정: 모듈 초기화, 게임 창 크기 설정, 게임 화면을 지정한 크기로 생성, 윈도우 상단에 보일 게임 제목 설정, clock 객체 생성  ![image](https://github.com/user-attachments/assets/b3186a21-3f43-4998-8e84-be2bfb52ae11)

3. #색상: 색상 정의  ![image](https://github.com/user-attachments/assets/deaf63f5-cddb-4323-b660-a6b402e6621c)

4. #플레이어: 25X25 사이즈의 사각형 객체 생성, 플레이어 속도 설정  ![image](https://github.com/user-attachments/assets/68f34184-37a6-4261-9c3a-6249a67afd61)

5. #장애물: 화면상단에서 장애물 생성 위치는 랜덤하게 지정, 장애물 속도  ![image](https://github.com/user-attachments/assets/101a01c9-94de-49e2-9318-524280ec1a2a)

6. #점수: 점수 및 폰드 설정  ![image](https://github.com/user-attachments/assets/7e597bab-05cd-49d2-b301-926e1c33a9c1)

7. #게임루프: 메인 게임 루프시작  ![image](https://github.com/user-attachments/assets/6d04a348-6c44-4f4f-91e2-d4ef61540aac)

8. #키 입력: 왼/오른쪽 방향키를 눌러 플레이어를 이동, 화면 밖으로 나가지 않도록 경계 조건  ![image](https://github.com/user-attachments/assets/7505b804-3ca0-4532-9879-9460dec8b915)

9. #장애물 이동: 화면을 벗어나면 랜덤한 X의 위치에서 재생성, 점수와 속도 증가  ![image](https://github.com/user-attachments/assets/99c513bb-01be-49b0-b58a-300aef5ee372)

10. #충돌체크: colliderect로 플레이어와의 충돌체크, 충돌할시 Game Over와 점수를 출력하고 2초뒤 게임 종료  ![image](https://github.com/user-attachments/assets/d9d42af0-2b2c-4893-88bd-6c49b4cb3c45)

11. #그리기: 플레이어, 장애물, 점수를 화면 그리고 flip로 화면에 그린 내용을 반영  ![image](https://github.com/user-attachments/assets/5fddd4aa-7bf1-4ddc-bd05-874c907566e0)

12. #게임 종료  ![image](https://github.com/user-attachments/assets/90765ec8-cc99-44db-b879-590af4f6d3ec)

