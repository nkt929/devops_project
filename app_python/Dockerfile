FROM python:3.9-alpine
WORKDIR /code
RUN adduser -D myuser && chown -R myuser .
USER myuser
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip install Flask pytz
EXPOSE 5000
COPY main.py .
CMD ["python", "-m", "flask", "run"]