# coding: utf8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

toaddr = 'nick19942091@yandex.ru'
me = 'From: Nick Korolkov'
you = 'To: ' + toaddr

server = 'smtp.gmail.com' # Сервер
port = 465 # Порты
user_name = 'nick1994209@gmail.com' # Отправитель
user_passwd = 'nick89163558230' # Пароль отправителя

# server = 'smtp.yandex.ru' # Сервер
# port = 465 # Порты (исходящая)  #993 входящая
# user_name = 'nick1994209@yandex.ru' # Отправитель
# user_passwd = '785665' # Пароль отправителя

# Формируем заголовок письма
msg = MIMEMultipart('mixed')
msg['Subject'] = 'Заголовок письма'
msg['From'] = me
msg['To'] = toaddr

# Формируем письмо
part = MIMEText('Содержимое письма', 'Plain email')
msg.attach(part)

# Подключение
s = smtplib.SMTP_SSL(server, port)
s.ehlo()
s.starttls()
s.ehlo()
# Авторизация
s.login(user_name, user_passwd)
# Отправка письма
s.sendmail(me, toaddr, msg.as_string())
s.quit()