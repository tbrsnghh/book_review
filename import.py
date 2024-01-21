import os, csv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(
    "postgresql://tbrs:1610@localhost:5432/bookrv"
)
db = scoped_session(sessionmaker(bind=engine))


def main():
    f = open("books.csv", "r")  # needs to be opened during reading csv
    reader = csv.reader(f)
    next(reader)
    for isbn, title, author, year in reader:
        db.execute(
            text(
                "INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)"
            ),
            {"isbn": isbn, "title": title, "author": author, "year": year},
        )

        db.commit()
        print(
            f"Added book with ISBN: {isbn} Title: {title}  Author: {author}  Year: {year}"
        )

    f.close()
    # 0380795272,Krondor: The Betrayal,Raymond E. Feist,1998
    # 1416949658,The Dark Is Rising,Susan Cooper,1973


if __name__ == "__main__":
    main()
