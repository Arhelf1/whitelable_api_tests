import smtplib
import os
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from notify.email_config import PASSWORD, MY_ADDRESS, SERVER, PORT
from notify.spam_protect import Spam

# globals
tmp_api = []
success = 'Сервис восстановился после сбоя.'


def erase_file(file):
    open(get_file_path(file), mode='w', encoding='utf-8').close()


def get_file_path(path):
    current_dir = os.path.dirname(__file__)
    path_to_file = os.path.join(current_dir, path)
    return path_to_file


def logger(response_data, target_url):
    global tmp_api
    tmp_api.append('API метод : {0} вернул статус код {1} \n'.format(target_url, str(response_data.status_code)))
    return 'API метод : {0} вернул статус код {1} \n'.format(target_url, str(response_data.status_code))


def get_contacts(filename):
    emails = []

    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            emails.append(a_contact.split(',')[0])
    return emails


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def make_email_message(**kwargs):
    message_template = read_template(get_file_path(kwargs['template']))
    msg = MIMEMultipart()
    message = message_template.substitute(API_FAIL=kwargs['message'])
    msg['From'] = 'wl-api-finam@yandex.ru'
    msg['To'] = ', '.join(kwargs['emails'])
    msg['Subject'] = 'ФИНАМ: WL API'
    msg.attach(MIMEText(message, 'plain'))
    return msg


def send_alarm_message():
    api_fail = ''

    emails = get_contacts(get_file_path('contacts.txt'))
    s = smtplib.SMTP_SSL(SERVER, PORT)
    s.login(MY_ADDRESS, PASSWORD)

    for i in list(set(tmp_api)):
        api_fail += '\n{0}'.format(i)

    if api_fail != '':
        if Spam.comparator(Spam.from_file(get_file_path('data.txt')), api_fail) is False:
            s.send_message(make_email_message(template='message.txt', message=api_fail, emails=emails))
            Spam.to_file(get_file_path('data.txt'), api_fail)
            erase_file('flag.txt')
    else:
        if os.path.getsize(get_file_path('flag.txt')) == 0:
            s.send_message(make_email_message(template='success.txt', message=success, emails=emails))
            Spam.to_file(get_file_path('flag.txt'), 'error_true')
            erase_file('data.txt')
        else:
            return

    s.quit()
