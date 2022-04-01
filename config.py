
import configparser


filepath = ".local.config.ini"
config_object = configparser.ConfigParser()  # 创建配置文件对象
config_object.read(filepath, encoding="utf-8")  # 读取配置文件

login_info = dict(config_object.items("login_info"))
login_key = login_info["login_key"]
login_secret = login_info["login_secret"]

