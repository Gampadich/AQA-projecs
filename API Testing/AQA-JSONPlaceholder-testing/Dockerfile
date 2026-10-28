FROM python:3.11-slim

WORKDIR /app

COPY requirments.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ['pytest', '-v', '--alluredir=allure-results']