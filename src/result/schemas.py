from pydantic import BaseModel
from typing import Optional

class ResultCreate(BaseModel):
    bench_press: str
    raising_hands: str
    holding_hands: str
    bench_of_Scott: str
    hammer: str
    pull_ups: str
    bar_pull_below: str
    bar_pull_overhead: str
    block_pull_below: str
    curring_dumbbells_head: str

class ResultUpdate(BaseModel):
    bench_press: str | None = None
    raising_hands: str | None = None
    holding_hands: str | None = None
    bench_of_Scott: str | None = None
    hammer: str | None = None
    pull_ups: str | None = None
    bar_pull_below: str | None = None
    bar_pull_overhead: str | None = None
    block_pull_below: str | None = None
    curring_dumbbells_head: str | None = None

