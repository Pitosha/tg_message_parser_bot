import MySQLdb
import gc

class Db:
    def __init__(self, connect_db):
        try:
            self.conn = MySQLdb.connect(connect_db[0], connect_db[1], connect_db[2], connect_db[3],
                                        use_unicode=True, charset="utf8mb4")
            self.cursor = self.conn.cursor()
        except Exception:
            self.conn.close()
            gc.collect()
            print("Ошибка подключения БД")

    def create_chat_on_db(self, new_chat):
        self.cursor.executemany("INSERT INTO chat(chat_id, chat_name, chek_alert_mes, chek_bot_work) VALUES(%s, %s, %s, %s)", new_chat)
        self.conn.commit()
        self.conn.close()
        gc.collect()

    def update_chat_on_db(self, up_chat):
        self.cursor.executemany("""UPDATE chat SET chat_name=%s, chek_alert_mes=%s, chek_bot_work=%s WHERE chat_id=%s""", (up_chat))
        self.conn.commit()
        self.conn.close()
        gc.collect()

    #возвращает чат по id чата
    def get_chat_from_chat_id(self, chat_id, all_items):
        self.cursor.execute("SELECT chat_id, chat_name, chek_alert_mes, chek_bot_work FROM chat WHERE chat_id={}".format(str(chat_id)))
        res = self.cursor.fetchall()

        if len(res) == 0:
            self.conn.close()
            gc.collect()
            return False
        else:
            if all_items == "obj":
                self.conn.close()
                gc.collect()
                return res[0]
            else:
                self.conn.close()
                gc.collect()
                return True


    def delete_chat_on_db(self, chat_id):
        self.cursor.execute("""DELETE FROM chat WHERE chat_id=%s""", (chat_id))
        self.conn.commit()
        self.conn.close()
        gc.collect()