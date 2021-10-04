from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import uuid
import account
import news
import team
import club


app = Flask(__name__)


def genID():
    return uuid.uuid4().fields[1]

@app.route("/")
def home():
    select_result= account.GetAllMemberNames()
    return render_template('home.html',dbresult=select_result)

@app.route('/member', methods=['GET','DELETE'])
def member():
    id = request.args.get('memberid')
    if request.method == 'GET':
        select_result = account.GetMemberDetail(id)
        print(select_result)
        return render_template('memberdetails.html',customerdetails = select_result)
    else:
        select_result = account.DeleteMember(id)
        members()

@app.route('/members', methods=['GET'])
def members():
    select_result = account.GetAllMembers(False)
    print(select_result)
    return render_template('members.html',dbresult = select_result)


@app.route('/member/update', methods=['GET','POST'])
def memberUpdate():
    if request.method == 'POST':
        print(request.form)
        return render_template('dbresult.html',"dbresult","column_names")
    else:
        id = request.args.get('memberid')
        select_result = account.GetMemberDetail(id)
        print(select_result)
        return render_template('memberupdate.html',customerdetails = select_result)

#add a new member
@app.route('/member/add', methods=['GET','POST'])
def addMember():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        phone =  request.form.get('phone')
        address1 = request.form.get('address')
        address2 = request.form.get('region')
        city = request.form.get('city')
        birthdate = request.form.get('birthdate')
        clubid = request.form.get('clubid')
        account.AddMember(firstname,lastname,email,phone,address1,address2,city,birthdate,clubid)
        redirect("/members")
    else:
        select_result = club.GetClubList()
        print(select_result)
        return render_template('memberadd.html',clublist = select_result)

@app.route('/member/delete', methods=['GET'])
def deleteMember():
    id = request.args.get('memberid')
    account.DeleteMember(id)
    redirect("/members")

"""
@app.route('/member/club', methods=['GET','POST'])
def memberaddclub():
    id = request.args.get('memberid')
    firstname = request.args.get('firstname')
    lastname = request.args.get('lastname')
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        phone =  request.form.get('phone')
        address1 = request.form.get('address')
        address2 = request.form.get('region')
        city = request.form.get('city')
        birthdate = request.form.get('birthdate')
        account.AddMember(firstname,lastname,email,phone,address1,address2,city,birthdate)
        return render_template('dbresult.html',"dbresult","column_names")
    else:
        select_result = club.GetAllClub()
        return render_template('memberclub.html',memberId = id, memberName=str(firstname)+" "+str(lastname),dbresult = select_result)
"""


@app.route('/member/team', methods=['GET','POST'])
def memberaddteam():
    id = request.args.get('memberid')
    firstname = request.args.get('firstname')
    lastname = request.args.get('lastname')
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        phone =  request.form.get('phone')
        address1 = request.form.get('address')
        address2 = request.form.get('region')
        city = request.form.get('city')
        birthdate = request.form.get('birthdate')
        account.AddMember(firstname,lastname,email,phone,address1,address2,city,birthdate)
        return render_template('dbresult.html',"dbresult","column_names")
    else:
        select_result = club.GetAllClub()
        return render_template('memberteam.html', memberId = id, memberName=str(firstname)+" "+str(lastname),dbresult = select_result)


@app.route('/news', methods=['GET','POST'])
def allnews():
    if request.method == 'GET':
        select_result = news.GetNews()
        return render_template('news.html',dbresult = select_result)

@app.route('/news/add', methods=['GET','POST']) 
def addnews(): 
    if request.method == 'GET':
        select_result = club.GetClubList()
        return render_template('newsadd.html', clublist = select_result) 
    else:
        clubid = request.form.get('clubid')
        header = request.form.get('header')
        newsbyline = request.form.get('newsbyline')
        context =  request.form.get('context')
        news.AddNews(clubid,header,newsbyline, context)
        redirect("/news")
        

@app.route('/news/details', methods=['GET','POST'])
def newsdetails():
    clubId = request.args.get('clubid')
    if request.method == 'Get':
        select_result = news.GetFristNewsById(clubId)
        return render_template('news.html',dbresult = select_result)
    if request.method == 'POST':
        select_result = news.GetFristNewsById(clubId)
        return render_template('news.html',dbresult = select_result)

@app.route('/news/delete', methods=['GET']) 
def deletenews(): 
    newsId = request.args.get('newsid')
    news.DeleteNews(newsId)
    redirect("/news")