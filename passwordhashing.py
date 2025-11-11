from getpass import getpass
import sys
from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from Crypto.Hash import SHA3_512


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "testtable"
    id: Mapped[str] = mapped_column(unique=True, nullable=False, primary_key=True)
    pw: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return f"ID: {self.id!r}, PW: {self.pw!r}"


if __name__ == "__main__":
    hash = SHA3_512.new()
    engine = create_engine(
        "mysql+pymysql://root:chicken@127.0.0.1:3306/test", echo=False
    )

    inp = input("REGISTER OR LOGIN? : ")

    if inp.upper() == "REGISTER":
        userid = input("Enter ID: ")
        pw = getpass("Enter PW: ")
        if getpass("Enter PW Again: ") == pw:
            hash.update(pw.encode())
        else:
            print("Password not match")
            sys.exit(1)

        userpw = hash.hexdigest()

        # with engine.connect() as conn:
        #     session = Session(engine)
        Base.metadata.create_all(engine)

        with Session(engine) as session:
            statement = select(User).where(User.id.in_([userid]))

            if len(session.scalars(statement).all()) >= 1:
                print("ERR! USER ALREADY EXISTS!")
                exit(3)
            else:
                try:
                    userdata = User(id=userid, pw=userpw)
                    session.add(userdata)
                    session.commit()
                except Exception as e:
                    print(f"ERROR: {e}")
                    exit(-1)
                print("SUCCESS")
    elif inp.upper() == "LOGIN":
        userid = input("Enter ID: ")
        hash.update(getpass("Enter PW: ").encode())
        userpw = hash.hexdigest()

        # with engine.connect() as conn:
        #     session = Session(engine)
        Base.metadata.create_all(engine)

        with Session(engine) as session:
            statement = select(User).where(User.id.in_([userid]))

            if len(session.scalars(statement).all()) >= 1:
                if session.scalars(statement).all()[0].pw == userpw:
                    print("WELCOME")
                else:
                    print("GO AWAY")
                    exit(2)
            else:
                print("GO AWAY")
                exit(2)
