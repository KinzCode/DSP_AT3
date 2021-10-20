FROM python:3.8.2
WORKDIR /project
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app . /project
COPY . /src . /project
CMD ["streamlit", "run", "streamlit_app.py"]