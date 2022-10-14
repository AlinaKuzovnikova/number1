from datetime import datetime, timedelta

try:
    print('Введите дату рождения в формате дд/мм/гггг')
    user_birthday = datetime.strptime(input(), "%d/%m/%Y")
except:
    print('Неверно введена дата')
    exit()

print('10000 дней исполнится ', user_birthday+timedelta(days=10000))
print('1000000 минут исполнится ', user_birthday+timedelta(minutes=1000000))
print('1000000000 секунд исполнится ', user_birthday+timedelta(seconds=1000000000))
