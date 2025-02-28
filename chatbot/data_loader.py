import pandas as pd

def load_data(csv_file):
	df = pd.read_csv(csv_file) #read the csv file
	return df

if __name__ == '__main__':
	df = load_data('finData.csv') #calling the function to check whether the data is loaded
	print(df.head()) 
