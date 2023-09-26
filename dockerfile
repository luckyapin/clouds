# #Плохая практика использовать latest
# FROM python:latest

# WORKDIR /app  

# #Плохая практика использование множества RUN 
# RUN pip install telebot
# RUN pip install emoji        

# COPY tgbot.py .

# #Плохая практика использовать CMD
# CMD ["python", "tgbot.py"]

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