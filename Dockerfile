FROM python:3

# Создаем рабочую директорию
WORKDIR /usr/src/app

# Копируем Python файл
COPY main.py /usr/src/app
COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt
# Команда по умолчанию
CMD ["python","./main.py"]

# docker build -t generator .
# docker run -v /Users/alicee/Desktop:/usr/src/app/output generator 
