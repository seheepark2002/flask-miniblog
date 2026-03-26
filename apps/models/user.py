from datetime import datetime
from apps.app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

#User클래스 데이터베이스 테이블로 변환
class User(db.Model, UserMixin): 
    
    #테이블명 지정 , 사용자 정보 저장 테이블
    __tablename__ = "users" 

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
        raise AttributeError("Password is not readable.")
    #입력된 password를 hash로 변환 후 저장
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 비밀번호 체크하기
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    # 이메일 중복 체크하기
    @staticmethod
    def is_duplicate_email(email):
        return User.query.filter_by(email=email).first() is not None

# 로그인하고 있는 사용자 정보를 취득하는 함수 작성하기
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)