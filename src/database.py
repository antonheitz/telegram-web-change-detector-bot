from dataclasses import dataclass
import sqlite3
from typing import List, Tuple

@dataclass
class WatchItem:
    id: int
    user_id: int
    url: str
    interval: int
    checksum: str
    last_checked: float

class Database:
    def __init__(self):
        self.database_file_name: str = "./data/database.db"
        db = sqlite3.connect(self.database_file_name)
        cursor = db.cursor()
        # check if table is already known
        if not cursor.execute("SELECT name FROM sqlite_master").fetchone():
            # insert table
            cursor.execute("CREATE TABLE watch_items(id integer primary key AUTOINCREMENT, chat_id, url, interval, checksum, last_checked)")
        
    def add_url(self, chat_id: int, url: str, interval: int) -> None:
        db, cursor = self._get_connection()
        cursor.execute(f"""
            INSERT INTO watch_items VALUES
                (null, {chat_id}, "{url}", {interval}, "", 0)
        """)
        db.commit()

    def get_urls(self, chat_id: int = None) -> List[WatchItem]:
        db, cursor = self._get_connection()
        items: List[WatchItem] = []
        for item in cursor.execute("SELECT * FROM watch_items"):
            if not chat_id or chat_id == item[0]:
                print(item)
                items.append(WatchItem(
                    id=item[0],
                    user_id=item[1],
                    url=item[2],
                    interval=item[3],
                    checksum=item[4],
                    last_checked=item[5]
                ))
        return items

    def _get_connection(self) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
        db = sqlite3.connect(self.database_file_name)
        cursor = db.cursor()
        return db, cursor