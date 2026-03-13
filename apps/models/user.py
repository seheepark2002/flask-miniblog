from datetime import datetime
from apps.app import db
from werkzeug.security import generate_password_hash

class User(db.Model): #db.Model을 상속한 User클래스 작성
    __tablename__ = "users" #테이블명 지정

    #컬럼 정의
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String, index=True)
    email = db.Column(db.String, unique=True, index=True)
    password_hash = db.Column(db.String) #보안 강화를 위해  hash를 저장
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    @property
    def password(self):
        raise AttributeError("읽어 들일 수 없음")
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

