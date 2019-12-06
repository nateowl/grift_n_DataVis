import csv
import matplotlib.pyplot as plt

# total medal trends - sample some years (20 year increments)

# 1924, 1948, 1968, 1984, 2006, 2014
# columns 0 (year) and column 4 (country)
#
m_1924 = 0
m_1928 = 0
m_1932 = 0
m_1936 = 0
m_1940 = 0
m_1944 = 0
m_1948 = 0
m_1952 = 0
m_1956 = 0
m_1960 = 0
m_1964 = 0
m_1968 = 0
m_1972 = 0
m_1976 = 0
m_1980 = 0
m_1984 = 0
m_1988 = 0
m_1992 = 0
m_1994 = 0
m_1998 = 0
m_2002 = 0
m_2006 = 0
m_2010 = 0
m_2014 = 0

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
				if (row[0] == "1924") and (row[4] == "CAN"):
					m_1924 += 1
				elif (row[0] == "1928") and (row[4] == "CAN"):
					m_1928 += 1
				elif (row[0] == "1932") and (row[4] == "CAN"):
					m_1932 += 1
				elif (row[0] == "1936") and (row[4] == "CAN"):
					m_1936 += 1
				elif (row[0] == "1940") and (row[4] == "CAN"):
					m_1940 += 1
				elif (row[0] == "1944") and (row[4] == "CAN"):
					m_1944 += 1
				elif (row[0] == "1948") and (row[4] == "CAN"):
					m_1948 += 1
				elif (row[0] == "1952") and (row[4] == "CAN"):
					m_1952 += 1
				elif (row[0] == "1956") and (row[4] == "CAN"):
					m_1956 += 1
				elif (row[0] == "1960") and (row[4] == "CAN"):
					m_1960 += 1
				elif (row[0] == "1964") and (row[4] == "CAN"):
					m_1964 += 1
				elif (row[0] == "1968") and (row[4] == "CAN"):
					m_1968 += 1
				elif (row[0] == "1972") and (row[4] == "CAN"):
					m_1972 += 1
				elif (row[0] == "1976") and (row[4] == "CAN"):
					m_1976 += 1
				elif (row[0] == "1980") and (row[4] == "CAN"):
					m_1980 += 1
				elif (row[0] == "1984") and (row[4] == "CAN"):
					m_1984 += 1
				elif (row[0] == "1988") and (row[4] == "CAN"):
					m_1988 += 1
				elif (row[0] == "1992") and (row[4] == "CAN"):
					m_1992 += 1
				elif (row[0] == "1994") and (row[4] == "CAN"):
					m_1994 += 1
				elif (row[0] == "1998") and (row[4] == "CAN"):
					m_1998 += 1
				elif (row[0] == "2002") and (row[4] == "CAN"):
					m_2002 += 1
				elif (row[0] == "2006") and (row[4] == "CAN"):
					m_2006 += 1
				elif (row[0] == "2010") and (row[4] == "CAN"):
					m_2010 += 1
				elif (row[0] == "2014") and (row[4] == "CAN"):
					m_2014 += 1

#output a chart here! a line chart would probably be best
medalCounts = [m_1924, m_1928, m_1932, m_1936, m_1940, m_1944, m_1948, m_1952, m_1956, m_1960, m_1964, m_1968, m_1972, m_1976, m_1980, m_1984, m_1988, m_1992, m_1994, m_1998, m_2002, m_2006, m_2010, m_2014]
years = [1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014]

plt.plot(years, medalCounts, color="gold", linewidth=6.0)
plt.xlabel("Olympic Year")
plt.ylabel("Medals by Year")
plt.title("Gold medals won by Canada")
plt.show()
