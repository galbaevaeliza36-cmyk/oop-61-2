class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

ROLE_COMMANDS = {
    "admin": ["start", "ban", "stop", "message"],
    "user": ["start", "message"]
}
def command_access(command_name):
    def decorator(func):
        def wrapper(self, user: User):
            if command_name not in ROLE_COMMANDS.get(user.role, []):
                print(f'Пользователь {user.username} не может выполнять команду "{command_name}"')
                return

            print(f'Пользователь {user.username} ({user.role}) выполняет команду {command_name}')
            return func(self, user)
        return wrapper
    return decorator
class CommandHandler:

    @command_access("start")
    def start(self, user):
        print("Система запущена")

    @command_access("ban")
    def ban(self, user):
        print("Пользователь заблокирован")

    @command_access("stop")
    def stop(self, user):
        print("Система остановлена")

    @command_access("message")
    def message(self, user):
        print(f" Пользователь {user.username} отправил сообщение")
if __name__ == "__main__":
    admin = User("Alice", "admin")
    user = User("Bob", "user")

    handler = CommandHandler()

    print("\n--- Действия администратора ---")
    handler.start(admin)
    handler.ban(admin)
    handler.stop(admin)

    print("\n--- Действия обычного пользователя ---")
    handler.start(user)
    handler.ban(user)
    handler.message(user)
