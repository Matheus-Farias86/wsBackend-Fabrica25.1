FROM python:3.12.1-slim

WORKDIR /app_accounts

COPY . /app_accounts/
COPY ./requirements.txt /app_accounts/requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
