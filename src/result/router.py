from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from result.models import Result
from result.schemas import ResultCreate, ResultUpdate
from fastapi_cache.decorator import cache

router = APIRouter(
    prefix="/result",
    tags=["Result"]
)

@router.get("/all")
@cache(expire=3600)
async def get_all_programs(session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Result)
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.mappings().all(),
            "details": None
        }
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
    })

@router.get("/{id_person}")
async def get_all_programs(id_person: int, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Result).where(Result.id == id_person)
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.mappings().all(),
            "details": None
        }
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
    })

@router.post("/")
async def add_result(new_result: ResultCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Result).values(**new_result.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router.patch("/{id_person}")
async def put_result(id_person: int, update_result: ResultUpdate, session: AsyncSession = Depends(get_async_session)):
    update_result = update_result.dict(exclude_unset=True)
    stmt = update(Result).where(Result.id == id_person).values(**update_result)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}