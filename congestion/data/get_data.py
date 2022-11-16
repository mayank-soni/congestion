import requests
import pandas as pd
import re
from datetime import datetime, timezone, timedelta
from congestion.data.params import LTA_API_HEADERS

def get_images(verbose: bool = False) -> dict:
    '''
    Gets response from LTA images API - contains URL of images
    '''
    print('Getting image URLs')
    url_images = 'http://datamall2.mytransport.sg/ltaodataservice/Traffic-Imagesv2'
    # print(LTA_API_HEADERS)
    images = requests.get(url_images, headers = LTA_API_HEADERS).json()
    print('Downloading images')
    # Regex to extract filename from url (contains camera ID, date and time of image)
    filename_regex = re.compile(r'/([\d_]+.jpg)')
    images_dict = {}
    for i, camera in enumerate(images['value']):
        if verbose:
            print(f'Downloading image {i}')
        imageurl = camera['ImageLink']
        # Make filename from URL
        filename = re.findall(filename_regex, imageurl)[0]
        response = requests.get(imageurl)
        # Save to dictionary
        images_dict[filename] = response.content
    return images_dict


def get_speeds(verbose: bool = False) -> pd.DataFrame:
    '''
    Gets responses from LTA speeds API and saves to DataFrame
    '''
    print('Downloading speeds data')
    url_speeds = 'http://datamall2.mytransport.sg/ltaodataservice/TrafficSpeedBandsv2'
    # Get current time to timestamp the data
    current_time = datetime.now(tz = timezone(timedelta(hours=8))).strftime('%Y-%m-%d_%H%M')
    # 59006 rows in API response, obtained in chunks of 500.
    # Get first chunk of 500, convert to df, and initialise list of dataframes
    if verbose:
        print('Downloading speeds row no. 0 - 499')
    speeds = requests.get(url_speeds, headers = LTA_API_HEADERS).json()
    speeds_df = pd.DataFrame(speeds['value']).set_index('LinkID')
    # Add a column for current time, since dataframe has no timestamp
    speeds_df['Time'] = current_time
    speedsdata = [speeds_df]
    # Get remaining chunks of 500, convert to dfs, and append to list
    for skip in range(500, 59500, 500):
        if verbose:
            print(f'Downloading speeds row no. {skip} - {skip+499}')
        new_speeds = requests.get(url_speeds, headers = LTA_API_HEADERS, params = {'$skip': f'{skip}'}).json()
        speeds_df = pd.DataFrame(new_speeds['value']).set_index('LinkID')
        speeds_df['Time'] = current_time
        speedsdata.append(speeds_df)
    # Combine all chunks and return, together with current time
    return pd.concat(speedsdata)