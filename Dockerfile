FROM python:3.9.12

WORKDIR /app

ADD vectorizer.pkl model.pkl app.py ./



RUN pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]