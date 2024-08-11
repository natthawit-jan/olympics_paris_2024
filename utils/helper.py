import requests
import json 
import os
import hashlib
import matplotlib.pyplot as plt
from PIL import Image, ImageChops
from io import BytesIO
import urllib.request
# Function to make an API request and read JSON result
def fetch_json(api_url, return_json=True):
    headers = {'user-agent': 'Insomnia 9.1'}
    response = requests.get(api_url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        if return_json:
            data = response.json()  # Parse the JSON response
            if data == {}:
                return None
            return data
        else:
            return response.text
    else:
        raise Exception(f"Failed to fetch data. HTTP Status code: {response.status_code}")


# Function to save JSON data to a file
def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        
def load_json(json_file_path):
    with open(json_file_path, 'r') as file:
        json_data = json.load(file)
    return json_data

def initialize(base_api_url, reload_override=False, json_file_path='data.json'):
    # Path to save the JSON file
    fetch = True
    # Fetch the JSON data from the API
    try:
        
        if os.path.exists(json_file_path) and os.path.isfile(json_file_path) and os.path.getsize(json_file_path) > 0:
            if reload_override:
                fetch = True
                os.remove(json_file_path)
            else:
                fetch = False
        if fetch:
            json_data = fetch_json(f'{base_api_url}')
            # Save the JSON data to a file
            save_json(json_data, json_file_path)
            print(f"JSON data saved to {json_file_path}")
        else:
            print(f"JSON data already exists at {json_file_path}")
            # read and store the data in dictionary
            # with open(json_file_path, 'r') as file:
            #     json_data = json.load(file)
            #     # print(json_data)
    except Exception as e:
        print(e)
        
def hash_json(data):
    """Generate a hash for the given JSON data."""
    json_str = json.dumps(data, sort_keys=True)
    return hashlib.md5(json_str.encode('utf-8')).hexdigest()


# show picture from url 
def show_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    plt.imshow(img)
    plt.axis('off')
    plt.show()
    
def get_ImageStream(url):
    url = url.replace("'", '')
    headers = {'user-agent': 'Insomnia 9.1'}
    response = requests.get(url, headers=headers).content   
    return Image.open(BytesIO(response))


class CustomURLOpener(urllib.request.FancyURLopener):
    version = 'Insomnia 9.1'
opener = CustomURLOpener()
opener.addheaders = [
    ('User-Agent', 'Insomnia 9.1')
]



def fetch_image(url, code):
    
    def _refetch_img(url):
        print('refetching image ' + str(code))
        # change the last part of the URL from .png to .jpg
        url = url.replace('.png', '.jpg')
        
        image_path = f'images/{code}.jpg'
        if os.path.exists(image_path):
            print('Image already exists')
            return Image.open(image_path)
        return opener.retrieve(url, image_path)
         
        
        
    
    url = url.replace("'", '')
    default_image = 'images/default_from_src.png'
    image_path = f'images/{code}.png'  # specify the path to save the image
    try:
        if os.path.exists(image_path) and not images_are_equal(image_path, default_image):
            image = Image.open(image_path)
            return image
    
        else:
        
            # download the image from the URL
            
            opener.retrieve(url, image_path)
            image = Image.open(image_path)
            
            if images_are_equal(image_path, default_image):
                print(code, ' is being refetched')
                return _refetch_img(url)
    
                
    except Exception as e:
        print('gello')
        print(e)
        image = Image.open('images/default.png')
    except ValueError as e:
        print(e)
        # _refetch_img()
    return image


def compute_md5(image_path):
    hasher = hashlib.md5()
    with open(image_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def images_are_equal(img1_path, img2_path):
    hash1 = compute_md5(img1_path)
    hash2 = compute_md5(img2_path)
    return hash1 == hash2


def add_medal(image, medal, shift):
    image.paste(medal, shift, medal)
    return image