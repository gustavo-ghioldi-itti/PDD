class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for obs in self._observers:
            obs.update(message)


class Observer:
    def update(self, message):
        pass


class EmailObserver(Observer):
    def update(self, message):
        print(f"[EMAIL] Notificación: {message}")


class SMSObserver(Observer):
    def update(self, message):
        print(f"[SMS] Notificación: {message}")


# Uso
subject = Subject()
subject.attach(EmailObserver())
subject.attach(SMSObserver())

subject.notify("Nuevo usuario registrado")
