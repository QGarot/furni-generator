from database import db


class Item:
    def __init__(self, id, sprite_id, item_name, public_name, width, length, stack_height, allow_stack, allow_sit, allow_lay, allow_walk, allow_gift, allow_trade, allow_recycle, allow_marketplace_sell, allow_inventory_stack, type, interaction_type, interaction_modes_count, vending_ids, multiheight, customparams, effect_id_male, effect_id_female, clothing_on_walk):
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

    def add_item_to_database(self):
        sql = "INSERT INTO items_base VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        db.insert(sql, self.data)

    def add_item_to_furnidata(self):
        pass
