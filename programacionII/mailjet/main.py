import os

from dotenv import load_dotenv

from mail import MailSender


load_dotenv()


def main(api_key, api_secret):
    print("Programa para envio de correo")
    email_data = {}
    email_data["destino_email"] = "pscrigna@gmail.com"
    email_data["subject"] = "Mail de prueba"
    email_data["from_email"] = "pscrigna@gmail.com"
    email_data["from_name"] = "Pablo"
    envia_data["html_body"] = "<h1>Este es un mail de prueba enviado desde mailjet</h1>"
    envia_mail(api_key, api_secret, email_data)


if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")
    main(api_key, api_secret)
