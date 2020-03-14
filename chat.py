import database
import config as c

class Chat:
    
    def __init__(self, target_id):
        self.target_id = target_id


    def init_chat(self, all_items="bool"):
        db = database.Db(c.connect_db)
        res = db.get_chat_from_chat_id(self.target_id, all_items)
        return res

    def create_chat(self, message):
        new_chat = [(
            message.chat.id,
            message.chat.title,
            "No",
            "No"
        )]
        db = database.Db(c.connect_db)
        db.create_chat_on_db(new_chat)

    def update_chat(self, chat_id, chat_name, alert_work="No", bot_work="No"):
        up_chat = [(
            chat_name,
            alert_work,
            bot_work,
            chat_id
        )]
        db = database.Db(c.connect_db)
        db.update_chat_on_db(up_chat)

    def delete_chat(self, chat_id):
        del_chat = [(
            chat_id
        )]
        db = database.Db(c.connect_db)
        db.delete_chat_on_db(del_chat)