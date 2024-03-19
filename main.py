import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl  # Encriptar correo
import smtplib  # envio de correo
from extract_names import info_colegios 

load_dotenv()

datos_colegios = info_colegios()

for i in range(len(datos_colegios["colegios"])):
    if datos_colegios["correos"][i] == "-":
        continue
    else:
        email_sender = "alejandrotordecilla12@gmail.com"
        password = os.getenv("PASSWORD")
        email_receiver = datos_colegios["correos"][i]

        subject = "Información Concurso de Escritura e Ilustración Nexcolar 2024"
        body = f'''<html>
                    <body>
                        <p>Buenos días. Esperamos se encuentren muy bien,</p>
                        <p>Somos el Periódico Estudiantil Nexos, de la Universidad EAFIT (Medellín), y les hacemos envío del presente mensaje con el propósito de invitar a <u>{datos_colegios["colegios"][i]}</u> a participar en el Concurso de Escritura e Ilustración Nexcolar 2024.</p>

                        <p>A grandes rasgos, podríamos describir esta iniciativa, que ya marcha por su cuarta edición, como una oportunidad para visibilizar la importancia de las competencias y habilidades características de áreas del saber vinculadas con las artes y las humanidades; reconociendo, en el proceso, la valía de los intereses de aquellos estudiantes que sienten afinidad por dichas disciplinas.</p>

                        <p>El concurso está dirigido a los estudiantes que estén cursando el décimo u onceavo grado, en alguna de las instituciones educativas del Área Metropolitana del Valle de Aburrá. La temática del concurso es <b style="color:red;">Cuando despierta el corazón</b>, y estaremos recibiendo textos o ilustraciones, tanto análogas como digitales, a partir del 24 de mayo hasta el 28 de julio.</p>

                        <p>Habrá tres finalistas por cada categoría, ilustración y texto. Además, quienes ocupen el primer lugar podrán ver sus obras en una de las ediciones impresas de nuestro periódico, y serán merecedores de unas cuantas sorpresas más.</p>

                        <p>En ese sentido, le solicitamos amablemente que nos confirme si le parece bien que los estudiantes de esta institución sean tomados en cuenta para futuras comunicaciones sobre el concurso. De ser así, le agradeceríamos que nos enviara, junto a la respuesta de este correo, el contacto de los directores de grupo de los grados décimo y onceavo; o, en caso de no contar con ellos, de quienes imparten lengua castellana, artística o semejantes en aquellos grados formativos. Asimismo, nos sería de gran utilidad que nos contara si la institución educativa puede regalarnos un espacio para hacer la convocatoria de manera presencial, al igual que los días y horas en que podríamos hacerlo, y las fechas entre las que los estudiantes estarán en el periodo de vacaciones de mitad de año.</p>

                        <p>Por último, adjuntamos el siguiente link donde los estudiantes pueden ingresar sus datos de contacto para hacerles llegar la totalidad de la información, en caso de estar interesados en participar. Les solicitamos que, por favor, lo compartan con ellos:</p>

                        <p><a href="https://forms.office.com/r/0XvgYCQDxb?origin=lprLink">https://forms.office.com/r/0XvgYCQDxb?origin=lprLink</a></p>
                        <p>Gracias por el tiempo dedicado a la lectura de este correo y por su consecuente colaboración.</p>
                        <p>Estaremos atentos a su respuesta y a las dudas que surjan en el proceso.</p>
                        <p>Cordialmente,</p>
                        <p>Periódico Estudiantil Nexos.</p>
                    </body>
                </html>'''

        em = EmailMessage()
        em["from"] = email_sender
        em["to"] = email_receiver
        em["subject"] = subject
        em.add_alternative(body, subtype="html")  # Set the body as HTML

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, password)
            smtp.send_message(em)

        print("Enviado")
