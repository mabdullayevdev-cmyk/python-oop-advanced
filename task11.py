from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


class EmailNotification(Notification):
    def send(self, message: str):
        print(f"Sending Email notification: {message}")


class SMSNotification(Notification):
    def send(self, message: str):
        print(f"Sending SMS notification: {message}")


class PushNotification(Notification):
    def send(self, message: str):
        print(f"Sending Push notification: {message}")


if __name__ == "__main__":
    notifications = [
        EmailNotification(),
        SMSNotification(),
        PushNotification()
    ]

    for notif in notifications:
        notif.send("Sizning buyurtmangiz qabul qilindi!")