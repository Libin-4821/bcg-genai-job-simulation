#Importing necesary libraries
from flask import Flask, render_template, request
from data_loader import load_data  #Import load_data function
from chatbot import InvestmentChatbot  #Import InvestmentChatbot class

app = Flask(__name__) #Initializing app

csv_file = 'finData.csv' #Loading the dataset
df = load_data(csv_file)
chatbot = InvestmentChatbot(df) #Initializing InvestmentChatbot object

@app.route("/")
def index():
	return render_template("index.html") #Rendering the html page

@app.route("/get_response", methods=["POST"])
def get_bot_response(): #generates response via class method
	query = request.form["msg"]
	response = chatbot.process_query(query)
	return response

if __name__ == "__main__":
	app.run(debug=True)
