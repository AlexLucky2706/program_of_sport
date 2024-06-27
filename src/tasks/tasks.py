import smtplib
from email.message import EmailMessage
from celery import Celery
from config import SMTP_PASSWORD, SMTP_USER, REDIS_HOST, REDIS_PORT

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

celery = Celery('tasks', broker=f'redis://{REDIS_HOST}:{REDIS_PORT}')

def get_email_template_dashboard(username: str, email: str):
    email = EmailMessage()
    email['Subject'] = 'Сегодня тренировка'
    email['From'] = SMTP_USER
    email['To'] = SMTP_USER

    email.set_content(
        '<div>'
        f'<h1 style="color: red;">Здравствуйте, {username}, напоминаю, что сегодня у вас самая важная тренировка в вашей жизни. Не пропускайте 😊</h1>'
        '</div>',
        subtype='html'
    )
    return email


@celery.task
def send_reminder_to_email(username: str, email: str):
    email = get_email_template_dashboard(username, email)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)
