from winney import Winney
from winney.mock import Mock


class MockData(Mock):
    data = {"name": "olivetree"}


if __name__ == "__main__":
    wy = Winney(host="class.h3c.com", port=5007)
    wy.register(method="get", name="get_app_list", uri="/ilearning/app/list", use_mock=True, mock_data=MockData())
    r = wy.get_app_list()
    print(r.get_json())
