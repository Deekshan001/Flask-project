from flask import Flask, redirect, url_for, render_template,request
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

class Conversion:
	def __init__(self, capacity):
		self.top = -1
		self.capacity = capacity
		self.array = []
		self.output = []
		self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

	def isEmpty(self):
		return True if self.top == -1 else False
	def peek(self):
		return self.array[-1]
	def pop(self):
		if not self.isEmpty():
			self.top -= 1
			return self.array.pop()
		else:
			return "$"
	def push(self, op):
		self.top += 1
		self.array.append(op)
	def isOperand(self, ch):
		return ch.isalpha()
	def notGreater(self, i):
		try:
			a = self.precedence[i]
			b = self.precedence[self.peek()]
			return True if a <= b else False
		except KeyError:
			return False
			
	def infixToPostfix(self, exp):
		table=[]
		for i in exp:
			if self.isOperand(i):
				self.output.append(i)
			elif i == '(':
				self.push(i)
			elif i == ')':
				while( (not self.isEmpty()) and
								self.peek() != '('):
					a = self.pop()
					self.output.append(a)
				if (not self.isEmpty() and self.peek() != '('):
					return -1
				else:
					self.pop()
			else:
				while(not self.isEmpty() and self.notGreater(i)):
					self.output.append(self.pop())
				self.push(i)
			table.append([i,", ".join(self.array),"".join(self.output)])
		while not self.isEmpty():
			self.output.append(self.pop())
		table.append(["_","_","".join(self.output)])
		table.append("".join(self.output))        
		return table

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

@app.route('/stackApp')
def stackApp():
    return render_template('stackApp.html',postfix=[""],ln=0)

@app.route('/stackApp', methods=['POST'])
def stackApp_post():
    exp = request.form['text']
    obj = Conversion(len(exp))
    result=obj.infixToPostfix(exp)
    return render_template('stackApp.html',infix=exp,postfix=result,ln=len(result))

if __name__ == "__main__":
    app.run(debug=True)

