from winney import Winney

if __name__ == "__main__":
    wy = Winney(host="class.h3c.com", port=5007)
    wy.add_url(method="get", uri="/ilearning/app/list", function_name="get_app_list", cache_time=5)
    r = wy.get_app_list()
    # t = r.get_bytes()
    # print(t)
    # r = wy.download()
    print(r.get_json())
