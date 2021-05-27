from plyer import  notification
import schedule
import time


def notificacion():

    print('Espseramos 2 segundos para enviar la primera nota')
    time.sleep(2)

    nota1 = 'Primera notificacion'
    notification.notify(title = 'Notificación Python',message = nota1 ,timeout = 2,)

    print('Espseramos 5 segundos para enviar la segunda nota')
    time.sleep(5)

    nota2 = 'Segunda notificacion'
    notification.notify(title = 'Notificación Python',message = nota2 ,timeout = 2,)


def programar_notificacion():

    schedule.every(2).seconds.do(notificacion)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    #Llamamos a la funcionn que programa la ejecucion de las notificiones
    programar_notificacion()

