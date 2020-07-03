from winney import Winney
from winney.mock import Mock


class MockData(Mock):
    data = {"name": "olivetree"}


if __name__ == "__main__":
    baidu = Winney(host="baidu.com")
    baidu.register(method="get", name="get_home", uri="/home", use_mock=True, mock_data=MockData())
    r = baidu.get_home()
    print(r.json())
