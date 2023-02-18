import abc

class Observer(abc.ABC):
    @abc.abstractmethod
    def update(self):
        pass

class InstagramAccount:
    def __init__(self, username):
        self.username = username
        self.__followers = []
    
    def attach(self, observer):
        self.__followers.append(observer)
    
    def detach(self, observer):
        self.__followers.remove(observer)
    
    def notify(self):
        for follower in self.__followers:
            follower.update()
    
    def add_new_post(self, message):
        print(f"New post from {self.username}: {message}")
        self.notify()

class Follower(Observer):
    def __init__(self, username):
        self.username = username

    def update(self):
        print(f"New post on Instagram: {self.username}")

def main():
    arayaroma = InstagramAccount("Daniel")
    follower_one = Follower("Cesar")
    follower_two = Follower("Karla")

    arayaroma.attach(follower_one)
    arayaroma.attach(follower_two)

    arayaroma.add_new_post("I see you there, observer.") 

if __name__ == '__main__':
    main()