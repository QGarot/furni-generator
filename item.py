from database import db
from manager import Manager


class Item:
    def __init__(self, id, sprite_id, item_name, public_name, width, length, stack_height, allow_stack, allow_sit, allow_lay, allow_walk, allow_gift, allow_trade, allow_recycle, allow_marketplace_sell, allow_inventory_stack, type, interaction_type, interaction_modes_count, vending_ids, multiheight, customparams, effect_id_male, effect_id_female, clothing_on_walk, page_id, offer_id, song_id, order_number, catalog_name, cost_credits, cost_points, points_type, amount, limited_sells, limited_stack, extradata, have_offer, club_only):
        self.data = (
            id,
            sprite_id,
            item_name,
            public_name,
            width,
            length,
            stack_height,
            allow_stack,
            allow_sit,
            allow_lay,
            allow_walk,
            allow_gift,
            allow_trade,
            allow_recycle,
            allow_marketplace_sell,
            allow_inventory_stack,
            type,
            interaction_type,
            interaction_modes_count,
            vending_ids,
            multiheight,
            customparams,
            effect_id_male,
            effect_id_female,
            clothing_on_walk,
        )

        self.data_catalog = (
            id,
            id,
            page_id,
            offer_id,
            song_id,
            order_number,
            catalog_name,
            cost_credits,
            cost_points,
            points_type,
            amount,
            limited_sells,
            limited_stack,
            extradata,
            have_offer,
            club_only
        )

    def add_item_to_database(self):
        """
        SQL request
        """
        # items_base
        sql1 = "INSERT INTO items_base VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        db.insert(sql1, self.data)
        print("[items_base] Chargé!")

        # catalog_items
        sql2 = "INSERT INTO catalog_items VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        db.insert(sql2, self.data_catalog)
        print("[catalog_items] Chargé!")

        with open("files/log.txt", "a") as log:
            log.write("ID: " + self.data[0] + " | item_name: " + self.data[2] + "\n")

    def add_item_to_furnidata(self):
        """
        Save item in furnidata.xml file
        """
        Manager.write_in_furnidata(Manager.furnidata_text(self))

    def load_files(self):
        """
        Download icon and swf files and put it in selected folders
        """
        Manager.add_furni_files(self.data[2])
