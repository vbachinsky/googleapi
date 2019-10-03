#! /usr/bin/python3

import requests

url = 'https://maps.googleapis.com/maps/api/geocode/json?'

keys = {'key':'AIzaSyDh5DQw2WWyCRsQ7xbxC2kKpfXO4comnS8'}

def check_correct_value(choise_of_option):
	while True:
		if not choise_of_option.isdigit() or not int(choise_of_option) in (1, 2):
			print('Please, enter the correct value')
			return True
		else:
			return False


class Geodata():
	'''For work with Google API'''
	def check_answer(self, response_dict):
		if response_dict['status'] == 'OK':
			return True
		else:
			print('Somewhere you wrong :(')
			return False

	def get_coordinates(self, lat, lng):
		response = requests.get('{}latlng={},{}&key={}'.format((url),lat,lng,keys['key']))
		response_dict = response.json()
		if self.check_answer(response_dict):
			print(response_dict['results'][0]['formatted_address'])

	def get_location(self, location, region = ''):
		response = requests.get('{}address={}&region={}&key={}'.format((url),location,region,keys['key']))
		response_dict = response.json()
		if self.check_answer(response_dict):
			print('Latitude: ', response_dict['results'][0]['geometry']['location']['lat'], ', longitude: ', response_dict['results'][0]['geometry']['location']['lng'])

def main():
	geoquery = Geodata()
	while True:
		choise_of_option = input('Please select what will you request: coordinates (1) or location (2): ')
		if not check_correct_value(choise_of_option):
			if int(choise_of_option) == 1:
				lat = input('Please input latitude: ')
				lng = input('and longitude: ')
				geoquery.get_coordinates(lat, lng)
				break
			else:
				location = input('Please input location: ')
				region = input('and region: ')
				geoquery.get_location(location, region)
				break

if __name__ == '__main__':
	main()
