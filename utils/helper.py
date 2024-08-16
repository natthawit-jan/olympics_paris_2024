import requests
import json 
import os
import hashlib
import matplotlib.pyplot as plt
from PIL import Image, ImageChops
from io import BytesIO
import urllib.request
import pandas as pd

nocs_df = pd.read_csv('csvs/noc.csv')
noc_cd_nm_dict = nocs_df[['noc_code', 'noc_name']].set_index('noc_code')['noc_name'].to_dict()



def load_medal_images():
   medal_size = (50, 50)
   medal_images = dict()
   for medal in ['gold', 'silver', 'bronze']:
      medal_images[medal] = Image.open(f'images/medals/{medal}.png').convert('RGBA').resize(medal_size)
   return medal_images

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


def get_team_members(config, i) -> list:
    l = []
    team_id = i['competitorCode']
    medalType = i['medalType'] 
    TEAM_PROFILE_URL = config['TEAM_PROFILE_URL']
    file_name = f'jsons/team_profile_{team_id}.json'
    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        team_profile = load_json(file_name)
    else:
        team_profile = fetch_json(TEAM_PROFILE_URL.format(code=team_id))
        save_json(team_profile, file_name)
        
    team_profile_list = team_profile['team']['athletes']

    for member in team_profile_list:
        r = dict()
        r['competitorCode'] = member['person']['code']
        r['competitorType'] = 'A'
        r['medalType'] = medalType
        l.append(r)
    return l


def fetch_image(url, code):
    
    def _refetch_img(url):
        print('refetching image ' + str(code))
        # change the last part of the URL from .png to .jpg
        url = url.replace('.png', '.jpg')
        
        image_path = f'images/{code}.jpg'
        if os.path.exists(image_path):
            return Image.open(image_path)
        opener.retrieve(url, image_path)
        return Image.open(image_path)
         
        
        
    
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



def search_and_show(code, combined_athletes_dfs, code_2_disciplines,  medal_count=None):
    
    combined_athletes = pd.concat(combined_athletes_dfs, ignore_index=True)
    combined_athletes['code'] = combined_athletes['code'].astype(str)
    athlete = combined_athletes[combined_athletes['code'] == str(code)].iloc[0]
    
    
    given_name = athlete['given_name']
    family_name = athlete['family_name']
    age = int(athlete['age'])
    noc_full = athlete['noc_full']
    profile_url = athlete['detail_url'] 

    
    discipline = code_2_disciplines[code_2_disciplines['code'] == code]['discipline_desc'].values[0]
    image = fetch_image(athlete['picture_url'], code)
    plt.imshow(image)
    plt.axis('off')
    
    if medal_count:
        plt.title(f"Name: {given_name} {family_name}\nAge: {age}\nCountry: {noc_full}\nDiscipline: {discipline}\n Medal Count: {medal_count}")
    else:
        plt.title(f"Name: {given_name} {family_name}\nAge: {age}\nCountry: {noc_full}\nDiscipline: {discipline}")
    plt.show()
    

def month_number_to_month_name(month_num: int) -> str:
    
    if pd.isna(month_num):
        return 'Unknown'
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    return months[month_num]


def get_full_name_from_short_code(code:str) -> str:
    return  noc_cd_nm_dict.get(code, 'NA')



class WinnerInfo:
    def __init__(self, winner_obj):
        self.code = winner_obj['competitorCode']
        self.medalType = winner_obj['medalType']

    def __str__(self):
        return f"{self.code} - {self.medalType}"
    
    def __repr__(self):
        return f"{self.code} - {self.medalType}"


class Organization:

    def __init__(self, table, config):
        
        self.config = config
        self.country_code = table['organisation']
        self.country_name = get_full_name_from_short_code(self.country_code)
        self.rank = table['rank']

        self.disciplines = dict()
        self.winners = dict()
        
        self._process_all(table)
    
    def __str__(self):
        return f"{self.country_name} ({self.country_code}), Rank: {self.rank},  Total Medals: {self.total_medals['Total']['total']}"

    def __repr__(self):
        return f"{self.country_name} ({self.country_code}), Rank: {self.rank},  Total Medals: {self.total_medals['Total']['total']}"
        
    def _process_all(self, table):
        self._process_discipline_to_medals(table['disciplines'])
        self._process_total_medals(table['medalsNumber'])
        self._process_winners(table['disciplines'])
    
    def _build_winners_lst(self):
        # if self.country_code == 'THA':
        #     print(self.winners)
        l = [w for disc in self.winners.values() for w in disc]
        self.winners_lst = l

        

    def _process_winners(self, disciplines_lst):
        _winner_dict = dict()
        for disc in disciplines_lst:
            disciplineC = disc['code']
            _winner_dict[disciplineC] = _winner_dict[disciplineC] if disciplineC in _winner_dict.keys() else []
            for winner_obj in disc['medalWinners']:
                if winner_obj['competitorType'] == 'A':
                    w = WinnerInfo(winner_obj)
                    _winner_dict[disciplineC].append(w)
                else:
                    expanded_team_lst = get_team_members(self.config, winner_obj)
                    for team_member in expanded_team_lst:
                        w = WinnerInfo(team_member)
                        _winner_dict[disciplineC].append(w)
        self.winners = _winner_dict
        self._build_winners_lst()

    def _process_discipline_to_medals(self, discipline_lst):
        _discipline_to_medals = dict()
        for disc in discipline_lst:
            _discipline_to_medals[disc['code']] = {k: disc[k] for k in ['gold', 'silver', 'bronze']}
        self.disciplines_to_medals = _discipline_to_medals

    def _process_total_medals(self, medals):
        _total_medals = dict()
        for medal in medals:
            _total_medals[medal['type']] = {k: medal[k] for k in ['gold', 'silver', 'bronze', 'total']}
        # print(_total_medals)
        self.total_medals = _total_medals


def countries_won_medals(config):  
    MEDALS_URL = config['MEDAL_URL']
    medals_json = fetch_json(MEDALS_URL)
    save_json(medals_json, 'jsons/medals.json')
    medal_tables = medals_json['medalStandings']['medalsTable']
    return [m['organisation'] for m in medal_tables], medal_tables