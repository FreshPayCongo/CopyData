FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install pydantic==1.10.11
#RUN pip install -r ./requirements.txt
RUN pip install fastapi
RUN pip install sqlalchemy
RUN pip install pymysql
RUN pip install fastapi-scheduler
RUN pip install uvicorn
RUN pip install mysqlclient
RUN pip install sqlmodel
RUN pip install asyncmy
RUN pip install python-dotenv

EXPOSE 8001

CMD ["uvicorn", "main:app","--host","0.0.0.0", "--port", "8001"]