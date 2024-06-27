from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from program.models import Program, Exercise
from program.schemas import ProgramCreate, ExerciseCreate

router = APIRouter(
    prefix="/program",
    tags=["Program"]
)

@router.get("/all")
async def get_all_programs(session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Program)
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

@router.get("/{program_number}")
async def get_all_programs(program_number: int, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Program).where(Program.id == program_number)
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

@router.post("")
async def add_program(new_operation: ProgramCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Program).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router.post("/exercise")
async def add_exercise(new_exercise: ExerciseCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Exercise).values(**new_exercise.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}