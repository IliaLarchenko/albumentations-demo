FROM python:3.7-buster
EXPOSE 8501
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
RUN bash setup_docker.sh
CMD ["streamlit", "run", "src/app.py"]
