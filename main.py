from dados import meu_email, password
import smtplib
import random
from email.message import EmailMessage

MEU_EMAIL = meu_email
PASSWORD = password
try:
    with open('mensagem.txt', 'r', encoding='utf-8') as mensagens:
        mensagens = mensagens.readlines()
        mensagem = random.choice(mensagens)
except FileNotFoundError:
    print("Arquivo de mensagens não encontrado.")


msg = EmailMessage()
msg['Subject'] = '\u2728 Miracle Messages! \u2728'
msg['From'] = MEU_EMAIL
msg['To'] = 'email_destinatario'
msg.set_content(f'\u2B50 Mensagem do dia \u2B50\n\n{mensagem}\n - Um Curso em Milagres')

try:
    with smtplib.SMTP('smtp.gmail.com', 587) as conexao:
        conexao.starttls()
        conexao.login(user=MEU_EMAIL, password=PASSWORD)
        conexao.send_message(msg)
except Exception as erro:
    print(f'Erro ao enviar o e-mail: {erro}')