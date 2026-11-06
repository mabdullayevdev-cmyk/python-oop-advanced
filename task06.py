from hashlib import sha256
from uuid import uuid1, UUID


class User:
    user_count = 0

    def __init__(self, username: str, email: str, password: str, id: UUID = None):
        if not username.strip():
            raise ValueError("Username bo'sh bo'lishi mumkin emas!")
        if not self.is_valid_email(email):
            raise ValueError("Email formati noto'g'ri.")

        self.id = id or uuid1()
        self.username = username
        self.email = email
        self.__hash_password = self.hash_password(password)
        User.user_count += 1

    def get_profile(self) -> dict:
        return {
            "id": str(self.id),
            "username": self.username,
            "email": self.email
        }

    @classmethod
    def get_user_count(cls) -> int:
        return cls.user_count

    @staticmethod
    def is_valid_email(email: str) -> bool:
        return "@" in email and "." in email

    @staticmethod
    def hash_password(password: str) -> str:
        return sha256(password.encode()).hexdigest()

    @classmethod
    def create_user(cls, data: dict):
        return cls(
            username=data.get("username"),
            email=data.get("email"),
            password=data.get("password")
        )


if __name__ == "__main__":
    user_data = {
        "username": "javohir",
        "email": "javohir@gmail.com",
        "password": "securepassword123"
    }
    user = User.create_user(user_data)
    print(user.get_profile())
    print(f"Jami foydalanuvchilar: {User.get_user_count()}")