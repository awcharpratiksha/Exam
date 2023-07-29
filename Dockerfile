FROM python
RUN pip install flask
WORKDIR /src
COPY . .
CMD python server.py

