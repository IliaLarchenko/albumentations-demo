FROM python:3.9.16-buster
EXPOSE 8501
WORKDIR /code
COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip setuptools wheel                                                                                                                                                                                                
RUN python3 -m pip install -r requirements.txt  
COPY . .
RUN bash setup_docker.sh
CMD ["streamlit", "run", "src/app.py"]
