import abc

class Observer(abc.ABC):
    @abc.abstractmethod
    def update(self):
        pass

class InstagramAccount:
    def __init__(self, name):
        self.name = name
        self.__account_followers = []
    
    def attach(self, observer):
        self.__account_followers.append(observer)
    
    def detach(self, observer):
        self.__account_followers.remove(observer)
    
    def notify(self):
        for follower in self.__account_followers:
            follower.update()
    
    def add_new_post(self, message):
        print(f"New post from {self.name}: {message}")
        self.notify()

class Follower(Observer):
    def __init__(self, name):
        self.name = name

    def update(self):
        print(f"New post on Instagram: {self.name}")

def main():
    arayaroma = InstagramAccount("Daniel")
    follower_one = Follower("Cesar")
    follower_two = Follower("Karla")

    arayaroma.attach(follower_one)
    arayaroma.attach(follower_two)

    arayaroma.add_new_post("I see you there, observer.") 

if __name__ == '__main__':
    main()