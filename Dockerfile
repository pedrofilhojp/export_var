FROM python
RUN apt update; apt install python3-virtualenv -y
WORKDIR /app
COPY app/ ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 11001
ENTRYPOINT [ "python3",  "app.py"]