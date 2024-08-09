from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __repr__(self):
        return self.nickname

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        return self.nickname == other.nickname

    def __hash__(self):
        return hash(self.password)


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title


class UrTube:
    def __init__(self):
        self.users = {}  # Словарь База пользователей 'nickname:password'.
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        self.current_user = None
        login = {nickname: hash(password)}  # Словарь создается в момент входа для сравнения(Аутентификации).
        for key, value in login.items():
            if key in self.users and value == self.users[key]:
                self.current_user = nickname
            else:
                print('Неверный логин или пароль')
        print(f'login - {login}')

    def register(self, nickname, password, age):
        user = User(nickname, password, age)
        if user.nickname in self.users:
            print(f"Пользователь {nickname} уже существует")
            return None
        else:
            self.users[nickname] = hash(password)  # Список пользователей.
            self.current_user = user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)

    def get_videos(self, search):
        search_result = []
        for item in self.videos:
            if search.lower() in item.title.lower():
                search_result.append(item.title)
        return search_result

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return None
        for video in self.videos:
            if video.title is title:
                if video.adult_mode is True and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return self
                while video.duration > video.time_now:
                    video.time_now += 1
                    sleep(1)
                    print(video.time_now, end=' ')
                print('Конец видео')


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка регистрации на существующий аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')

    # Проверка входа в существующий аккаунт
    # ur.log_in('vasya_pupkin', 'lolkekcheburek')
    # print(ur.current_user)
    # ur.log_in('vasya_pupkin', 'nevernijparol')
