#include <iostream>
#include <list>
#include <string>

class Observer {
public:
  virtual void update() = 0;
};

class Follower : public Observer {
private:
  std::string username;

public:
  Follower(std::string username) { this->username = username; }

  void update() override {
    std::cout << "New post on Instagram: " << username << std::endl;
  }
};

class InstagramAccount {
private:
  std::string username;
  std::list<Observer *> followers;

public:
  InstagramAccount(std::string username) { this->username = username; }

  void attach(Observer *observer) { followers.push_back(observer); }

  void detach(Observer *observer) { followers.remove(observer); }

  void notify() {
    for (auto follower : followers) {
      follower->update();
    }
  }

  void addNewPost(std::string message) {
    std::cout << "New post from " << username << ": " << message << std::endl;
    notify();
  }
};

int main() {
  InstagramAccount arayaroma("Daniel");
  Follower followerOne("Cesar");
  Follower followerTwo("Karla");

  arayaroma.attach(&followerOne);
  arayaroma.attach(&followerTwo);

  arayaroma.addNewPost("I see you there, in C++.");

  return EXIT_SUCCESS;
}