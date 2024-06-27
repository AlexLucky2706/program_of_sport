from sqlalchemy import Column, Integer, String
from database import Base

class Result(Base):
    __tablename__ = 'result'

    id = Column(Integer, primary_key=True)
    bench_press = Column(String)
    raising_hands = Column(String)
    holding_hands = Column(String)
    bench_of_Scott = Column(String)
    hammer = Column(String)
    pull_ups = Column(String)
    bar_pull_below = Column(String)
    bar_pull_overhead = Column(String)
    block_pull_below = Column(String)
    curring_dumbbells_head = Column(String)