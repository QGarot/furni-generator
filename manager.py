import json
import urllib.request


class Manager:
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
        old_furnidata = Manager.get_actual_furnidata()
        with open(Manager.get_furnidata(), "w", encoding="UTF8") as furnidata:
            furnidata.write(old_furnidata.replace("<furnidata>\n<roomitemtypes>", "<furnidata>\n<roomitemtypes>\n\n"+arg+"\n\n"))
            print("[Furnidata] Mis à jour!")

    @staticmethod
    def add_furni_files(name):
        urllib.request.urlretrieve(
            "https://swf.habbocity.me/dcr/hof_furni/"+str(name)+".swf",
            Manager.get_swfs()+str(name)+".swf")
        print("[SWF File] Ajouté!")

        urllib.request.urlretrieve(
            "https://swf.habbocity.me/dcr/hof_furni/icons2/"+str(name)+"_icon.png",
            Manager.get_icons()+str(name)+"_icon.png")
        print("[PNG File] Icone ajoutée !")

    @staticmethod
    def furnidata_text(item):
        with open("files/furnidatatext.txt") as ftext:
            text = ftext.read().replace("{id}", item.data[0]).replace("{name}", item.data[2]).replace("{public_name}", item.data[3])
            return text

    @staticmethod
    def get_actual_furnidata():
        with open(Manager.get_furnidata(), "r", encoding="UTF8") as furnidata:
            return furnidata.read()
