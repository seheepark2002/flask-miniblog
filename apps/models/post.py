# 데이터타임 넣기
from datetime import datetime
# db 데이터테이블 연결하기
from apps.app import db

# post 데이터베이스 테이블 생성
class Post(db.Model):

# 테이블명 지정
    __tablename__ = "posts"

# 컬럼 정의
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.now)

