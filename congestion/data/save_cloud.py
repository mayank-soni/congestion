import pandas as pd
import os
from google.cloud import bigquery
from congestion.data.params import (PROJECT, DATASET, BUCKET_NAME)
from congestion.data.get_data import get_images, get_speeds
from google.cloud import storage
from congestion.data.save_local import save_images_local, get_image_path


def save_cloud():
    '''
    Wrapper function, downloading image and speed data and saving on cloud
    '''
    images = get_images()
    save_images_cloud(images)
    speedsdf = get_speeds()
    save_speeds_cloud(speedsdf)


def save_images_cloud(images: dict, verbose: bool = False):
    '''
    Saves images to cloud.
    '''
    save_images_local(images)
    print('Saving images to cloud')
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    for i, filename in enumerate(images.keys()):
        if verbose:
            print(f'Saving image {i}')
        cloud_filename = f"data-images/{filename}"
        machine_filename = os.path.join(get_image_path(), filename)
        blob = bucket.blob(cloud_filename)
        blob.upload_from_filename(machine_filename)
        # Delete local data after uploading to cloud
        if os.path.exists(machine_filename):
            os.remove(machine_filename)


def save_speeds_cloud(speedsdf: pd.DataFrame):
    '''
    Saves speeds dataframe to cloud
    '''
    print('Saving speeds df to BigQuery')
    table = f"{PROJECT}.{DATASET}.speedsdata"
    client = bigquery.Client()
    job_config = bigquery.LoadJobConfig(schema = [bigquery.SchemaField("LinkID", "STRING")])
    client.load_table_from_dataframe(speedsdf, table, job_config = job_config)


if __name__ == '__main__':
    save_cloud()
