#Хорошая практика указывать версию
FROM python:3.9
WORKDIR /app  

#Хорошая практика использовать 1 RUN
RUN pip install \
    telebot\
    emoji

COPY tgbot.py .

#Хорошая практика использовать ENTRYPOINT
ENTRYPOINT ["python", "tgbot.py"]