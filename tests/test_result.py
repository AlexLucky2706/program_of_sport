import pytest
from sqlalchemy import insert, select
from conftest import async_session_maker
from httpx import AsyncClient
from result.models import Result

async def test_add_result(ac: AsyncClient):
    response = await ac.post("/result/", json={
            'id': 2,
            'bench_press': 'one',
            'raising_hands': 'one',
            'holding_hands': 'one',
            'bench_of_Scott': 'one',
            'hammer': 'one',
            'pull_ups': 'one',
            'bar_pull_below': 'one',
            'bar_pull_overhead': 'one',
            'block_pull_below': 'one',
            'curring_dumbbells_head': 'one'
    })
    assert response.status_code == 200

