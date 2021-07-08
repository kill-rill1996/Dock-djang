FROM python:3.6

RUN mkdir -p /src/usr/app/
WORKDIR /src/usr/app/

COPY .. /src/usr/app/
RUN pip install --no-cache-dir -r req.txt

EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]


