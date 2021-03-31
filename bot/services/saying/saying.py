import pymongo
import re
import os
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

dblist = myclient.list_database_names()
mydb = myclient["chatbot"]
mycol = mydb["saying"]

def LoadSaying():
    with  open(os.getcwd()+"/data/saying","r",encoding="UTF-8") as file:
        for line in file:
            tmp = re.search(r"(.*)《(.*)》(.*)",line)
            if(tmp== None) : continue
            # print(str(mycol.find({"Content":tmp.group(1)}).count()!=0)+":"+tmp.group(1))
            if(mycol.find({"Content":tmp.group(1)}).count()!=0) : continue
            mycol.insert_one({"Content":tmp.group(1),"AnimeName":tmp.group(2)})
            # print(tmp.group(1))
            # print(tmp.group(2))

def InitDateBase():
    mycol.delete_many({})

def RandomGetSaying():
    result = list(mycol.aggregate([{ '$sample': { 'size': 1 } }]))[0]
    ret =result['Content']+"\n                      ——出自《"+result["AnimeName"]+"》"
    # print(ret)
    return ret

# InitDateBase()
# LoadSaying()
# randomGet()




  

