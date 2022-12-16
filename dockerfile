FROM python:3

RUN apt-get update

RUN pip install --upgrade pip
RUN python -m pip install requests
RUN python -m pip install pycld2
RUN python -m pip install discord
RUN python -m pip install python-dotenv
COPY .env /.env
COPY discordbot.py /discordbot.py
CMD ["python3","discordbot.py"]