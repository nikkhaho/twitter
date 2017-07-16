import db
import checkdb
def save1(tag):
    if tag=="":
       print("null")
    else:
     p=checkdb.checkindb("tb_tag",tag,"tag")
     if p=="no":
         o=db.saveintb("tb_tag",tag)

