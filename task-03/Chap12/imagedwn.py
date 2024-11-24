import requests
import os


api_key = '47237060-95775ccb1140c1639d6c1c180'
search_term = 'cats'
images_to_download = 10  


if not os.path.exists('pixabay_images'):
    os.makedirs('pixabay_images')


url = "https://pixabay.com/api/"


params = {
    'key': api_key,
    'q': search_term,
    'per_page': images_to_download,  
    'image_type': 'photo',  
    'safesearch': 'true'
}

response = requests.get(url, params=params)
results = response.json()


total_downloaded = min(images_to_download, len(results['hits']))

for i in range(total_downloaded):
    hit = results['hits'][i]
    image_url = hit['largeImageURL']
    image_name = str(hit['id']) + '.jpg'
    image_path = os.path.join('pixabay_images', image_name)

    img_data = requests.get(image_url).content
    with open(image_path, 'wb') as handler:
        handler.write(img_data)

print("Download completed!")