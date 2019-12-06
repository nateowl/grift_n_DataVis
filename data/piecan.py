import csv
import matplotlib.pyplot as plt

# total medal trends - sample some years (20 year increments)

# 1924, 1948, 1968, 1984, 2006, 2014
# columns 0 (year) and column 4 (country)
#
USA = 0
CAN = 0

#remove row 1 because it is
categories = []


#opens up csv file with csv reader
with open('OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)

	line_count = 0

#removing the first line of code so that it isn't included in our chart.
	for row in reader:
			if line_count == 0:
				#parse the first row of the text data out of the file
				categories.append(row)
				line_count += 1

			else:
				if row[4] == "USA":
					USA += 1
				elif row[4] == "CAN":
					CAN += 1


#output a chart here! a line chart would probably be best

plt.title("USA vs. CAN")
countries = [USA, CAN]
label = ["United States", "Canada"]
colors = ["#3679ff", "#ff6d57"]

plt.pie(countries, labels=label, colors=colors, startangle=90, autopct='%.1f%%')
plt.show()
