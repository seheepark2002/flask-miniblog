from pathlib import Path

basedir = Path(__file__).parent.parent

# BaseConfig 클래스 작성하기
class BaseConfig:
    SECRET_KEY = "SWudebj23"
    WTF_CSRF_SECRET_KEY = "AJifne7fg"

# BaseConfig 클래스 상속하여 LocalConfig 클래스 작성
class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

# BaseConfog 클래스 상속하여 TestingConfig 클래스 작성
class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'testing.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False

# config 사전에 매핑
config = {
    "testing": TestingConfig,
    "local": LocalConfig,
}
 




