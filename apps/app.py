from pathlib import Path #SQLite DB 경로 설정을 위한 Path 라이브러리
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate # DB migration 관리
from flask_sqlalchemy import SQLAlchemy # ORM
from flask_wtf.csrf import CSRFProtect #CSRF 보안 기능
from apps.config import config

# SQLALchemy 객체 생성
db = SQLAlchemy()  
#CSRF 보호 객체 생성
csrf = CSRFProtect() 

# LoginManager 인스턴스화
login_manager = LoginManager()

# login_view 속성에 미로그인 시 리다이렉트하는 엔드포인트 지정
login_manager.login_view = "auth.login"

# login_message 속성에 로그인 후에 표시할 메세지 지정
login_manager.login_message = ""


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
    #CSRF 보호 활성화
    csrf.init_app(app) 
    
    #Flask 앱과 DB 연결
    db.init_app(app) 

    #Flask앱이랑 DB를 migration 시스템에 연결
    Migrate(app, db) 
    
    # login_manager를 애플리케이션과 연계하기
    login_manager.init_app(app)

    #Blueprint import
    from apps.crud import views as crud_views
    from apps.miniblog import views as miniblog_views
    # auth 패키지로부터 views를 import 
    from apps.auth import views as auth_views
    # posts 모듈의 route를 flask 앱에서 사용하기 위해  모듈 import "posts_views"
    from apps.posts import views as posts_views
    #모델 import (migration 인식용)
    from apps.models.user import User 
    from apps.models.post import Post 


    # CRUD blueprint 등록
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    # miniblog blueprint 등록
    app.register_blueprint(miniblog_views.miniblog)

    # register_blueprint를 사용해 views의 auth를 앱에 등록
    app.register_blueprint(auth_views.auth, url_prefix="/auth")

    # blueprint 앱에 등록하기, 공통 루트 "/posts"
    app.register_blueprint(posts_views.posts, url_prefix="/posts")

    return app



