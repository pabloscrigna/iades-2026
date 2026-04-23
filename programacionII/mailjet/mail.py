import os
from mailjet_rest import Client
from dotenv import load_dotenv

load_dotenv()


class MailSender:
    def __init__(self):
        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")
        self.client_mail = Client(auth=(api_key, api_secret), version="v3.1")

    def envia_mail(self, data_email: dict):
        data = {
            "Messages": [
                {
                    "From": {
                        "Email": data_email["from_email"],
                        "Name": data_email["from_name"],
                    },
                    "To": [{"Email": data_email["destino_email"]}],
                    "Subject": data_email["subject"],
                    "HTMLPart": data_email["html_body"],
                }
            ]
        }

        result = self.client_mail.send.create(data=data)
        return result.json(), result.status_code


client_email = MailSender()


if __name__ == "__main__":
    email_data = {
        "destino_email": "pscrigna@gmail.com",
        "subject": "Mail de prueba",
        "from_email": "pscrigna@gmail.com",
        "from_name": "Pablo",
        "html_body": "<h1>mail de prueba enviado desde mailjet</h1>",
    }
    response = client_email.envia_mail(email_data)
    print(response)
