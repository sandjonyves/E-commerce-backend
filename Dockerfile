FROM python:3

# RUN makdir /app

WORKDIR  /app

COPY . .
# COPY . /app/

# RUN python -m venv /env

# ENV PATH="/env/bin/${PATH}"

# COPY entrypoint.sh /app/antrypoint.sh

# RUN python -m pip install --upgrade pip

# COPY requirements.txt /app/

# COPY requirements.txt .

# RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE  8000

CMD [ "python","manage.py","runserver","0.0.0.0:8000" ]
