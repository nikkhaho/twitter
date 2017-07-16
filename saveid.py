import db
import checkdb
def save1(id):
  if id=="":
       print("null")
  else:
    p=checkdb.checkindb("tb_id",id,"id")
    if p=="no":
     o=db.saveintb("tb_id",id)
     print(id+":saved")



