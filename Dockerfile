FROM python:3.9.12

WORKDIR /app

ADD model.pkl app.py ./

RUN pip install streamlit tensorflow tensorflow_hub tensorflow_text

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]