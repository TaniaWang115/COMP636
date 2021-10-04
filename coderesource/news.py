import db
from datetime import date, datetime

def GetFristNewsById(clubId):
    sqlCommand = "select newsID, newsheader, newsbyline, newsdate, news from ClubNews where clubId={} orderby newsdate limit 3;".format(clubId)
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result

def AddNews(clubId,newsheader, newsbyline, news):
    today  = datetime.today()
    date = today.strftime("%y-%m-%d")
    sqlCommand = "insert into ClubNews (clubId,newsheader, newsbyline,news,newsdate) values('{}','{}', '{}','{}','{}');".format(clubId,newsheader, newsbyline, news,date)
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result

def GetNews():
    sqlCommand = "select newsID, ClubName, newsheader, newsbyline, newsdate, news from ClubNews join Clubs on ClubNews.ClubId= Clubs.ClubId;"
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result

def DeleteNews(newsId):
    sqlCommand = "delete from ClubNews where newsId = {};".format(newsId)
    print(f"{sqlCommand}")
    select_result = db.DBOperator(sqlCommand)
    print(f"{select_result}")
    return select_result