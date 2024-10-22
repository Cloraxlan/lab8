From python:3.8
WORKDIR /usr/src/app
copy . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "./app.py"]
