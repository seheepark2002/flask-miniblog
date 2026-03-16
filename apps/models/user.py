from datetime import datetime
from apps.app import db
from werkzeug.security import generate_password_hash

class User(db.Model): #db.Model을 상속한 User클래스 작성
    __tablename__ = "users" #테이블명 지정 , 사용자 정보 저장 테이블

    #컬럼 정의
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String, index=True) 
    email = db.Column(db.String, unique=True, index=True) # 
    username = db.Column(db.String, unique=True, index=True)
    password_hash = db.Column(db.String) #보안 강화를 위해  hash 저장
    created_at = db.Column(db.DateTime, default=datetime.now)# 생성시간
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)#수정 시간

    #password property는 읽기 불가
    @property
    def password(self):
        raise AttributeError("읽어 들일 수 없음")
    #입력된 password를 hash로 변환 후 저장
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)