# winney
![pypi](https://img.shields.io/pypi/v/winney?color=blue) ![Codacy Badge](https://app.codacy.com/project/badge/Grade/6e1a16da7b3747e0b69440fd3826e8f3)

## Install
> pip install winney

## Tutorial
``` python
from winney.winney import Address
from winney import Winney, retry
from winney.mock import Mock


class UserMock(Mock):
    data = {"name": "olivetree"}


class UserCenter(object):
    def __init__(self):
        self.winney = Winney(host="localhost", port=5000)
        self.init_functions()

    def init_functions(self):
        self.winney.register(method="post",
                             name="login",
                             uri="/api/login",
                             mock=False,
                             mock_data=None)
        self.winney.register(method="get",
                             name="get_user",
                             uri="/api/user",
                             mock=True,
                             mock_data=UserMock())

    def login(self, account, password):
        r = self.winney.login(json={"account": account, "password": password})
        return r.json()

    def get_user(self, user_id):
        r = self.winney.get_user(data={"user_id": user_id})
        return r.json()


if __name__ == "__main__":
    uc = UserCenter()
    uc.login("hello", "123456")

```
