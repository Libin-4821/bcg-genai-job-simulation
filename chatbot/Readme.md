#Financial Chatbot

##Overview
This project implements an investment chatbot using Flask, Pandas and Python. The chatbot is designed to provide information about companies' [Apple, Microsoft, Tesla] financial data, including revenue, net income, assets, liabilities and cash flow.
The application consists of a Flask web application that interacts with chatbot backend.
The chatbot uses Pandas Dataframe containing financial data to answer user queries.


```
app.py
chatbot.py
data_loader.py
finData.csv
requirements.txt
templates/index.html
```

##1.app.py
This file contains the Flask application code.
Functionality:
* Initializes the Flask application
* Loads data from `finData.csv` using the `load_data` functino from `data_loader.py`.
* Initializes the `InvestmentChatbot` with the loaded data.
* Defines routes for the web application:
	* `/`: Renders the `index.html` template.
	* `/get_response`: Handles POST requests to get chatbot responses based on user input.
* Runs the Flask application in debug mode.

###Dependencies:
* Flask
* `data_loader.py`
* `chatbot.py`

##2.chatbot.py
This file contains the `InvestmentChatbot` class, which handles the chatbot logic.

Class: `InvestmentChatbot`

`__init__(self, df)`

* Initializes the InvestmentChatbot with a Pandas DataFrame.

* Defines the feature columns to be used in the chatbot.

```
self.feature_columns = ['Total Revenue', 'Net Income', 'Total Assets', 'Total Liabilities', 'Cash Flow from Operating Activitites']
```

`get_company_list(self)`

* Returns a comma-separated string of unique company names from the DataFrame.

`get_feature_list(self)`

* Returns a comma-separated string of feature columns.

`get_data_by_company(self, company_name)`

* Retrieves all data for a specific company.

* Returns a dictionary of records if the company is found.

* Returns "Company not found" if the company is not found.

`get_feature_for_company(self, company_name, feature_name)`

* Retrieves a specific feature for a company.

* Returns the feature values for each year available.

* Returns "Company not found" if the company is not found.

* Returns "Feature not found" if the feature is not in the feature columns.

* Returns "No data found" if no data is found for the company and feature.

`process_query(self, query)`

* Processes the user query and returns the appropriate response.

* Handles queries for:

	* Listing available companies.

	* Listing available features.

	* Getting data about a specific company.

	* Getting a specific feature of a company.

* Returns an error message if the query is not understood.

##3.data_loader.py

This file contains the function to load data from CSV file.

###Function: 
`load_data(csv_file)`
* Loads data from a CSV file into a Pandas DataFrame using `pd.read_csv()`.
* Returns the DataFrame

##4.finData.csv
This CSV file contains the financial data for different companies.

###Columns
* `Company:` Name of the company.

* `Year:` Year of the financial data.

* `Total Revenue:` Total revenue of the company.

* `Net Income:` Net income of the company.

* `Total Assets:` Total assets of the company.

* `Total Liabilities:` Total liabilities of the company.

* `Cash Flow From Operating Activities:` Cash flow from operating activities of the company.

###Data
The file contains data for Apple, Microsoft and Tesla for the years 2022,2023 and 2024, extracted from SEC documents.

##5.`requirements.txt`
This file lists the Python packages required to run the application.

###Dependencies
* Flask==3.1.0
* pandas==2.2.3

##6.templates/index.html
This HTML file provides the user interface for the chatbot.

###Functionality
* Displays a simple chat interface with an input field for the user to type their query.
* Sends user query to Flask application and displays the response.

##Setup and Installation
###1.Clone the repository:

```
git clone <repository_url>
cd <repository_directory>
```
Or unzip the zip file.

###2.Create a virtual environment (recommended):

````
python -m venv venv
source venv/bin/activate   # On Linux/macOS
venv\Scripts\activate.bat  # On Windows
```

###3.Install the dependencies:

```
pip install -r requirements.txt
```

###4.Run the Flask application:

```
python app.py
```
###5.Access the application in your web browser:

Open your web browser and go to http://127.0.0.1:5000/ to interact with the chatbot.
[Check with the port number]

###Usage
1. Open the web application in your browser.

2. Type your query in the input field and press Enter.

	* To get a list of available companies, type "list of companies" or "available companies".

	* To get a list of available features, type "list of features" or "available features".

	* To get data about a specific company, type "data about [company name]".

	* To get a specific feature of a company, type "what is [feature] of [company]?"

		* For example: "What is Total Revenue of Apple?"

3. The chatbot will display the response below the input field.

###Example Queries

* "List of companies"

* "List of features"

* "Data about Apple"

* "What is Total Revenue of Apple?"

* "What is Net Income of Microsoft?"

###Notes
* The application is set to run in debug mode, which is useful for development.

* The chatbot can be extended to support more complex queries and data sources.

* The index.html file can be modified to improve the user interface.

* Error handling and input validation can be added to improve the robustness of the application.

