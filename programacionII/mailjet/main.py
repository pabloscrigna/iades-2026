from mail import client_email


def main():

    mail_to = "ivangmclp@gmail.com"
    mail_from = "pscrigna@gmail.com"
    mail_from_name = "Pablo"
    nombre_destino = "Ivan"

    email_data = {
        "destino_email": mail_to,
        "subject": "Mail de prueba",
        "from_email": mail_from,
        "from_name": mail_from_name,
        "html_body": f"<h1> Hola {nombre_destino}, este es un mail de prueba</h1>",
    }
    response = client_email.envia_mail(email_data)
    status_code, res_json = response
    print("status code:", status_code)
    print("response: ", response)


if __name__ == "__main__":
    main()
