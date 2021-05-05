from flask import Flask, redirect, url_for, render_template
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
def queueData():
    data=[]
    URL = 'https://www.studytonight.com/data-structures/queue-data-structure'
    page = requests.get(URL)
    content = page.content
    soup = BeautifulSoup(content,'html.parser')
    job_elems = soup.find_all('div', id='body-content')
    for d in job_elems:
        n=list()
        for i in d.find_all('p'):
            n.append(i.get_text().strip())
        ol=list()
        for i in d.find_all('ol'):
            li=list()
            for j in i.find_all('li'):
                li.append(j.get_text().strip())
            ol.append(li)
        ul=list()
        for i in d.find_all('ul'):
            li=list()
            for j in i.find_all('li'):
                li.append(j.get_text().strip())
            ul.append(li)
        img='https://www.studytonight.com/data-structures/'+d.find('img')['src']
        data.append(n[0])
        data.append(n[2])
        data.append(n[4])
        data.append(img)
        data.append(ol[0])
        data.append(n[6])
        data.append(ol[1])
        data.append(n[15])
        data.append(ul[1])
        return data

def stackData():
    data=[]
    URL = 'https://www.studytonight.com/data-structures/stack-data-structure'
    page = requests.get(URL)
    content = page.content
    soup = BeautifulSoup(content,'html.parser')
    job_elems = soup.find_all('div', id='body-content')
    for d in job_elems:
        n=list()
        for i in d.find_all('p'):
            n.append(i.get_text().strip())
        ol=list()
        for i in d.find_all('ol'):
            li=list()
            for j in i.find_all('li'):
                li.append(j.get_text().strip())
            ol.append(li)
        ul=list()
        for i in d.find_all('ul'):
            li=list()
            for j in i.find_all('li'):
                li.append(j.get_text().strip())
            ul.append(li)
        img='https://www.studytonight.com/data-structures/'+d.find('img')['src']
        data.append(n[0])
        data.append(img)
        data.append(ol[0])
        data.append(n[2])
        data.append(n[3])
        data.append(ol[1])
        data.append(n[8])
        data.append(ul[0])
        data.append(n[9])
        return data

app = Flask(__name__)

@app.route("/")
def stack():
    return render_template("stack.html")

@app.route("/queue")
def queue():
    return render_template("queue.html")

@app.route("/stackArr")
def stackArr():
    return render_template("stackArr.html")

@app.route("/queueLL")
def queueLL():
    return render_template("queueLL.html")

@app.route("/queueArr")
def queueArr():
    return render_template("queueArr.html")

@app.route("/stackLL")
def stackLL():
    return render_template("stackLL.html")

@app.route("/queueDes")
def queueDes():
    return render_template("queueDes.html",info=queueData())

@app.route("/stackDes")
def stackDes():
    return render_template("stackDes.html",info=stackData())
if __name__ == "__main__":
    app.run(debug=True)

