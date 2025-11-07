import sqlalchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from Crypto.Hash import SHA3_512


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "testtable"
    id: Mapped[str] = mapped_column(unique=True, nullable=False)
    pw: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return f"ID: {self.id!r}, PW: {self.pw!r}"


if __name__ == "__main__":
    hash = SHA3_512.new()
    userid = input("Enter ID: ")
    hash.update(input("Enter PW: ").encode())
    userpw = hash.hexdigest()

    userdata = User(id=userid, pw=userpw)

    engine = sqlalchemy.create_engine(
        "mysql+pymysql://root:chicken@127.0.0.1:3306/test", echo=True
    )
    with engine.connect() as conn:
        session = Session(engine)
