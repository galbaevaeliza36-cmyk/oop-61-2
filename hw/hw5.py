class User:
    def __init__(self, username: str, role: str):
        self.username = username
        self.role = role

    def __str__(self):
        return f"{self.username} ({self.role})"


ALLOWED_COMMANDS = {
    "admin": ["start", "ban", "stop", "message"],
    "user": ["start", "message"]
}

def check_permission(command_name: str):
    def decorator(func):
        def wrapper(self, user: User, *args, **kwargs):

            # проверка: существует ли команда
            if command_name not in self.get_all_commands():
                print(f" Команда '{command_name}' не существует")
                return

            # проверка прав доступа
            allowed = ALLOWED_COMMANDS.get(user.role, [])
            if command_name not in allowed:
                print(f" Пользователь {user.username} не может выполнять команду \"{command_name}\"")
                return

            # если всё ок
            print(f"Пользователь {user.username} ({user.role}) выполняет команду {command_name}")
            return func(self, user, *args, **kwargs)

        return wrapper
    return decorator



class CommandHandler:

    def __init__(self):
        self.commands_executed = 0
    @classmethod
    def get_all_commands(cls):

        return ["start", "ban", "stop", "message"]

    @staticmethod
    def print_separator():
        print("-" * 40)


    @check_permission("start")
    def start(self, user: User):
        self._count()
        print(" Система запущена")

    @check_permission("ban")
    def ban(self, user: User):
        self._count()
        print("Пользователь заблокирован")

    @check_permission("stop")
    def stop(self, user: User):
        self._count()
        print("Система остановлена")

    @check_permission("message")
    def message(self, user: User):
        self._count()
        print(f" Пользователь {user.username} отправил сообщение")

    # обычный instance method
    def _count(self):
        self.commands_executed += 1


if __name__ == "__main__":


    admin = User("Alice", "admin")
    user = User("Bob", "user")

    handler = CommandHandler()

    # ADMIN
    CommandHandler.print_separator()
    handler.start(admin)
    handler.ban(admin)
    handler.stop(admin)


    CommandHandler.print_separator()
    handler.start(user)
    handler.ban(user)        # запрещено
    handler.message(user)

    CommandHandler.print_separator()
    print(f"Всего выполнено команд: {handler.commands_executed}")