import smtplib
from email.mime.text import MIMEText 



def enviar_email(ideia, destinatario): 
    # Configurações do servidor de e-mail  
    remetente = 'felipe@ladodefora.site' 
    senha = 'Flg@1999'
    servidor_smtp = 'email-ssl.com.br' 
    porta_smtp =  587 #465 #587  
    # Cria o objeto de mensagem MIMEText   
    msg = MIMEText(ideia)
    msg['Subject'] = 'Ideia'
    msg['From'] = remetente
    msg['To'] = destinatario
    try:         
        # Inicia a conexão com o servidor SMTP 
        server = smtplib.SMTP(servidor_smtp, porta_smtp)
        server.starttls()
        server.login(remetente, senha)
        # Envia o e-mail
        server.sendmail(remetente, destinatario, msg.as_string()) 
        print('E-mail enviado com sucesso!')  
    except Exception as e:
        print('Erro ao enviar o e-mail:', str(e))  
    finally:
     # Encerra a conexão com o servidor SMTP
     server.quit() 





#enviar_email("testand direto", "felipe.gomes@messeminvestimentos.com.br")