FROM python:3

# Создаем рабочую директорию
WORKDIR /usr/src/app

# Копируем Python файл
COPY main.py /usr/src/app
RUN mkdir data
COPY data/brands.csv /usr/src/app/data
COPY data/products.csv /usr/src/app/data
COPY data/shop_names.csv /usr/src/app/data
COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# Команда по умолчанию
CMD ["python","./main.py"]



# docker build -t generator .
# docker run -it -v /Users/alicee/Desktop:/usr/src/app/output generator 
