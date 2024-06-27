from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from auth.base_config import current_user
from sqlalchemy import select, insert, update
from auth.models import Person
from program.models import Program
from .tasks import send_reminder_to_email

router = APIRouter(prefix="/reminder")


@router.get("/")
async def send_reminder(session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Person, Program).join(Program)
        result = await session.execute(query)
        data = result.all()
        for person, program in data:
            if program.day1 == 'Friday':
                send_reminder_to_email.delay(person.name, person.email)
        return {
            "status": "success",
            "data": None,
            "details": None
    }
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
    })