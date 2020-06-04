"""
>> FurniGenerator <<
@author: Tig3r
@version: 1.0
@arcturusversion: 2.3.1 &+
@project: Yobba
@catalog: Frost
"""
import item


launched = True
while launched:

    # furni
    id = str(input("Id > "))
    sprite_id = str(input("Sprite_id > "))
    item_name = str(input("item_name > ")).lower()
    public_name = str(input("public_name > "))
    width = str(input("width > "))
    length = str(input("length > "))
    stack_height = str(input("stack_height > "))
    allow_stack = str(input("allow_stack > "))
    allow_sit = str(input("allow_sit > "))
    allow_lay = str(input("allow_lay > "))
    allow_walk = str(input("allow_walk > "))
    allow_gift = str(input("allow_gift > "))
    allow_trade = str(input("allow_trade > "))
    allow_recycle = str(input("allow_recycle > "))
    allow_marketplace_sell = str(input("allow_marketplace_sell > "))
    allow_inventory_stack = str(input("allow_inventory_stack > "))
    type = str(input("type > "))
    interaction_type = str(input("interaction_type > "))
    interaction_modes_count = str(input("interaction_modes_count > "))
    vending_ids = str(input("vending_ids > "))
    multiheight = str(input("multiheight > "))
    customparams = str(input("customparams > "))
    effect_id_male = str(input("effect_id_male > "))
    effect_id_female = str(input("effect_id_female > "))
    clothing_on_walk = str(input("clothing_on_walk > "))

    #catalog
    page_id = str(input("page_id > "))
    offer_id = str(input("offer_id > "))
    song_id = str(input("song_id > "))
    order_number = str(input("order_number > "))
    catalog_name = str(input("catalog_name > "))
    cost_credits = str(input("cost_credits > "))
    cost_points = str(input("cost_points > "))
    points_type = str(input("points_type > "))
    amount = str(input("amount > "))
    limited_sells = str(input("limited_sells > "))
    limited_stack = str(input("limited_stack > "))
    extradata = str(input("extradata > "))
    have_offer = str(input("have_offer > "))
    club_only = str(input("club_only > "))

    print("\n\n")
    furni = item.Item(id, sprite_id, item_name, public_name, width, length, stack_height, allow_stack, allow_sit,
                      allow_lay, allow_walk, allow_gift, allow_trade, allow_recycle, allow_marketplace_sell,
                      allow_inventory_stack, type, interaction_type, interaction_modes_count, vending_ids, multiheight,
                      customparams, effect_id_male, effect_id_female, clothing_on_walk, page_id, offer_id, song_id, order_number, catalog_name, cost_credits, cost_points, points_type, amount, limited_sells, limited_stack, extradata, have_offer, club_only)
    try:
        furni.add_item_to_database()
        furni.add_item_to_furnidata()
        furni.load_files()
    except:
        print("Ré-essaye")

    print("\n\n")
    a = str(input("Continuer ? (Oui/Non) >"))
    launched = a == "Oui" or a == "oui"
