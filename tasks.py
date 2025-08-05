from sqlalchemy import Column, DateTime, func
from enum import Enum

from functools import cache
from typing import Annotated

#from fastapi import Depends
from sqlmodel import Session, SQLModel, Field, Relationship, create_engine, select

engine = create_engine("sqlite:///tasks.db", echo=False)
client = engine  # compatibility -- remove later


def _init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

class TaskPriority(str, Enum):
    whimsy = "whimsy" # less than optional; suggestions to make the day more fun
    bonus = "bonus" # stretch goals: what do you want your life to be?
    zero = "zero" # if it never gets done, thats fine
    low = "low"
    medium = "medium"
    high = "high"
    immediate = "immediate" # MUST DO!

class TaskSource(str, Enum):
    work = "work"
    life = "life"
    chore = "chore"
    relationship = "relationship"
    automation = "automation"
    sideproject = "sideproject"
    blockchain = "blockchain"
    homelab = "homelab"


class Tasks(SQLModel, table=True):
    id: int = Field(primary_key=True)
    task: str
    priority: TaskPriority
    source: TaskSource

def import_csv(filename: str = "tasks.csv"):
    with open(filename, newline="") as f:
        reader = csv.reader(f)
        with Session(engine) as session:
            for row in reader:
                task_name, priority_str, source_str = row
                task = Tasks(
                    task=task_name,
                    priority=TaskPriority(priority_str),
                    source=TaskSource(source_str)
                )
                session.add(task)
            session.commit()


def query_tasks():
    with Session(engine) as session:
        tasks = session.exec(select(Tasks).order_by(Tasks.priority)).all()
        for task in tasks:
            print(task)


if __name__=="__main__":
    SQLModel.metadata.create_all(engine)
