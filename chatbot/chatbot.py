import pandas as pd

class InvestmentChatbot:
	def __init__(self, df): #Initializing dataframe and feature columns
		self.df = df
		self.feature_columns = ['Total Revenue', 'Net Income', 'Total Assets', 'Total Liabilities', 'Cash Flow from Operating Activitites']

	def get_company_list(self): #to retrieve the list of companies
		return ", ".join(self.df['Company'].unique())

	def get_feature_list(self): #to retrieve the list of features
		return ", ".join(self.feature_columns)

	def get_data_by_company(self, company_name): #to get data by the company name
		company_data = self.df[self.df['Company'] == company_name]
		if not company_data.empty:
			return company_data.to_dict('records')
		else:
			return "Company not found"

	def get_feature_for_company(self, company_name, feature_name): #to get specific feature for a company
		if company_name not in self.df['Company'].values:
			return "Company not found"
		if feature_name not in self.feature_columns:
			return "Feature not found"

		company_data = self.df[self.df['Company'] == company_name]
		values = []
		for index,row in company_data.iterrows():
			year = row['Year']
			value = row[feature_name]
			values.append(f"In {year}: {value}")

		if values:
			return "\n".join(values)
		else:
			return f"No data found for {company_name} and {feature_name}"

	def process_query(self, query):

		if "list of companies" in query.lower() or "available companies" in query.lower(): #query to return list of companies
			return self.get_company_list()
		elif "list of features" in query.lower() or "available features" in query.lower(): #query to return list of features
			return self.get_feature_list()
		elif "data about" in query.lower(): #query to get data by the company name
			company_name = query.split("data about ")[1].strip() #retrieve company name from the query
			return self.get_data_by_company(company_name)
		elif "what is" in query.lower() and "of" in query.lower():
			try:
				parts = query.split("what is ")[1].split(" of ")
				feature_name = parts[0].strip().title() #retrieve feature name
				company_name = parts[1].strip().title() #retrieve company name
				company_name = company_name.rstrip('?') #remove '?' which is retained in the company name
				return self.get_feature_for_company(company_name, feature_name)
			except IndexError:
				return "Invalid query format. Try 'What is [feature] of [company]?'"
		else:
			return "I'm sorry, I don't understand that query. Ask me about companies, features, data about a company, or a specific feature of a company"

