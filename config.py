import json
import urllib.request


class Config:
    """
    This class manages the file creation (icons/swfs) and the writing in a file (furnidata)
    """

    @staticmethod
    def get_furnidata():
        with open("config.json") as json_file:
            return json.load(json_file)["path.furnidata"]

    @staticmethod
    def get_swfs():
        with open("config.json") as json_file:
            return json.load(json_file)["path.swfs"]

    @staticmethod
    def get_icons():
        with open("config.json") as json_file:
            return json.load(json_file)["path.icons"]

    @staticmethod
    def write_in_furnidata(arg):
        with open(Config.get_furnidata(), "a") as furnidata:
            furnidata.write(arg + "\n")
            print("[Furnidata] Mis à jour!")

    @staticmethod
    def add_furni_files(name):
        urllib.request.urlretrieve(
            "https://swf.habbocity.me/dcr/hof_furni/"+str(name)+".swf",
            Config.get_swfs()+str(name)+".swf")
        print("[SWF File] Added!")

        urllib.request.urlretrieve("https://swf.habbocity.me/dcr/hof_furni/icons2/"+str(name)+"_icon.png", )
