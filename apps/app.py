from pathlib import Path #SQLite DB 경로 설정을 위한 Path 라이브러리
from flask import Flask
from flask_migrate import Migrate # DB migration 관리
from flask_sqlalchemy import SQLAlchemy # ORM
from flask_wtf.csrf import CSRFProtect #CSRF 보안 기능
from apps.config import config

db = SQLAlchemy() # SQLALchemy 객체 생성 #실제 Flask app과 연결은 create_app()에서 수행
csrf = CSRFProtect() #CSRF 보호 객체

#Flask Application Factory
#Flask 앱 생성 및 설정 초기화 함수
def create_app(config_key="local"):
    #Flask app 형성
    app = Flask(__name__)

    # config_key에 매치하는 환경의 config 클래스 읽어들임
    app.config.from_object(config[config_key])

    #애플리케이션 설정
#     app.config.from_mapping(
#         SECRET_KEY="83hfwkfn3SJW3", #Flask 세션 및 보안에 사용되는 시크릿코드
#         SQLALCHEMY_DATABASE_URI= f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}", # SQLite 데이터베이스 경로
#         SQLALCHEMY_TRACK_MODIFICATIONS=False, #SQLAlchemy 이벤트 시스템 비활성화(성능 개선)
#         SQLALCHEMY_ECHO=True, #SQL 쿼리를 콘솔에 출력(개발 시 디버깅용)
#         WTF_CSRF_SECRET_KEY="EAFihio39fha", #CSRF 보호용 secret key
# )   
    csrf.init_app(app) #CSRF 보호 활성화
    db.init_app(app) #SQLAlchemy Flask 앱과 연결
    Migrate(app, db) #Flask-Migrate 초기화
    
    #Blueprint import
    from apps.crud import views as crud_views
    from apps.miniblog import views as miniblog_views

    #모델 import (migration 인식용)
    from apps.models.user import User 

    # CRUD blueprint 등록
    app.register_blueprint(crud_views.crud, url_prefix="/crud")
    # miniblog blueprint 등록
    app.register_blueprint(miniblog_views.miniblog)

    return app



