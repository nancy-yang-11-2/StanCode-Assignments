"""
File: weather_master.py
Name: Nancy
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

EXIT = -100


def main():
	"""
	This program will ask for weather temperature.
	Show the highest and lowest temperatures.
	Calculate the average temperature.
	Show the number of days below 16 celsius degrees (cold day).
	"""
	print('stanCode \"Weather Master 4.0"!')
	temp = int(input('Next temperature: (or' + str(EXIT) + ' to quit)? '))

	if temp == EXIT:
		print('No temperatures were entered.')
	else:
		highest = temp
		lowest = temp
		sum_temp = temp
		count = 1
		cold_day = 0
		if temp < 16:  # calculating the number of temperature data entered.
			cold_day += 1
		while True:
			temp = int(input('Next temperature: (or' + str(EXIT) + ' to quit)? '))
			if temp == EXIT:
				break
			else:
				sum_temp += temp  # calculating the sum of the temperature data entered.
				count += 1
				if highest < temp:
					highest = temp
				if lowest > temp:
					lowest = temp
				if temp < 16:
					cold_day += 1
		print('Highest temperature = ', str(highest))
		print('Lowest temperature =', str(lowest))
		average = sum_temp / count
		print('Average = ', str(float(average)))
		print(str(cold_day), 'cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
