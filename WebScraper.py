import os
import requests
from bs4 import BeautifulSoup


website = input("Please paste the imgur link of the album: ")
request = requests.get(website)

soup = BeautifulSoup(request.text, 'html.parser')
found_images = soup.findAll('div', {'class': 'post-image-container'})


ids = ['http://i.imgur.com/' + x['id'] + '.jpg' for x in found_images]
counter = 1
save_directory = soup.title.text.strip().replace(' - Album on Imgur', '')

try:
    os.mkdir(save_directory)
except:
    pass

for id in ids:
    image_request = requests.get(id).content
    with open('{0}/{0} - {1}.jpg'.format(save_directory, counter) , 'wb') as file:
        file.write(image_request)
    counter += 1

print('Done')
input("Press ANY KEY to exit")


