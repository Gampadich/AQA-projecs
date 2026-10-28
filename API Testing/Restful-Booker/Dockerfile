FROM python:3.11-slim

WORKDIR /app

# Копіюємо залежності та встановлюємо їх
COPY requirments.txt .
RUN pip install --no-cache-dir -r requirments.txt

# Копіюємо весь код проєкту Restful-Booker
COPY . .

# Команда для запуску pytest із генерацією звітів Allure
CMD ["pytest", "-v", "--alluredir=allure-results"]