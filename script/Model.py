from tool import hash_, log as _log
from peewee import *
import os
from config import BASE_DIR
from datetime import datetime

db = SqliteDatabase( os.path.join(BASE_DIR, 'data', 'kwork.db') )
log = _log("Model", "model.log")

class UsersProject(Model):
    title = TextField()
    description = TextField()
    author = TextField()
    proposal_count = TextField()
    price = TextField()
    timer = TextField()
    link  = TextField( unique=True )
    timestamp = IntegerField()

    @staticmethod
    def custom_insert(rows):
        temp = []
        for row in rows:
            row_dict = row._asdict()
            try:
                # UsersProject.insert_many(rows).execute()
                UsersProject.insert(row_dict).execute()
                temp.append( row )
                # log.info("Insert row %s" % str(row) )
            except IntegrityError as e:
                log.error("Error Integrity: %s : Link %s" % (e, row_dict['link']) )
        return temp

    class Meta:
        database = db

UsersProject.create_table()

class Project:
    def __init__(self, *args):
        self.title = args[0]
        self.description = args[1]
        self.author = args[2]
        self.proposal_count = args[3]
        self.price = args[4]
        self.timer = args[5]
        self.link  = args[6]
        self.timestamp = datetime.now().timestamp()

    def _asdict(self):
        return self.__dict__.copy()

    def __str__(self):
        string = "{}\n\n{}\n\nPrice: {}\nLink: [on project]({})".format(
            self.title, self.description[:3000], self.price, self.link
        )
        end =  "\n" + ("=" * 20)
        string += end
        return string

    def hash(self):
        return hash_(self.link)


if __name__ == '__main__':
    query = UsersProject.select()
    log.info("Len: %s" % len(query)  )
