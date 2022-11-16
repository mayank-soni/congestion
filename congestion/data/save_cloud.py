import pandas as pd
import os
from google.cloud import bigquery
from congestion.data.params import PROJECT, DATASET, LOCAL_DATA_PATH
from congestion.data.get_data import get_images, get_speeds

def save_cloud():
    '''
    Wrapper function, downloading image and speed data and saving on cloud
    '''
    # images = get_images()
    # save_images_cloud(images)
    # speedsdf = get_speeds()
    speedsdf = pd.read_csv(os.path.join(LOCAL_DATA_PATH, 'data-speeds', 'speeds.csv'))
    save_speeds_cloud(speedsdf)


def save_images_cloud(images: dict, verbose: bool = False):
    '''
    Saves images to cloud.
    '''
    pass # TODO
    # print('Saving images to cloud')
    # for i, (filename, data) in enumerate(images.items()):
    #     if verbose:
    #         print(f'Saving image {i}')
    #     full_filename = os.path.join(LOCAL_DATA_PATH, 'data-images', filename)
    #     with open(full_filename, 'wb') as f:
    #         f.write(data)


def save_speeds_cloud(speedsdf: pd.DataFrame):
    '''
    Saves speeds dataframe to cloud
    '''
    print('Saving speeds df to BigQuery')

    table = f"{PROJECT}.{DATASET}.speeds"
    client = bigquery.Client()
    job_config = bigquery.LoadJobConfig(autodetect=True)
    client.load_table_from_dataframe(speedsdf, table, job_config = job_config)


if __name__ == '__main__':
    save_cloud()
