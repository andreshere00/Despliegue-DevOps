FROM python:3.7.7-slim

EXPOSE 9080

RUN apt-get update
RUN apt-get install -y git
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git

WORKDIR practica_creativa2/bookinfo/src/productpage

ENV GROUP_NUMBER=41
COPY mod_txt.py .
RUN python3 mod_txt.py ${GROUP_NUMBER}

RUN pip install -r requirements.txt && \
	pip install urllib3==1.24.1 jsonschema==2.6.0 && \
	pip install --upgrade requests

ENTRYPOINT python3 productpage_monolith.py 9080
