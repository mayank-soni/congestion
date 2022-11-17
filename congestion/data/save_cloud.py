import os
import sys
from google.cloud import bigquery
from congestion.data.params import (PROJECT, DATASET, BUCKET_NAME)
from congestion.data.get_data import get_images, get_speeds
from google.cloud import storage
from congestion.data.save_local import save_images_local, get_image_path


def save_images_cloud(verbose: bool = False):
    '''
    Saves images to cloud.
    '''
    images = get_images()
    # Save images locally first
    save_images_local(images)
    # Then transfer to cloud
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


def save_speeds_cloud():
    '''
    Saves speeds dataframe to cloud
    '''
    speedsdf = get_speeds()
    print('Saving speeds df to BigQuery')
    table = f"{PROJECT}.{DATASET}.speedsdata"
    client = bigquery.Client()
    job_config = bigquery.LoadJobConfig(schema = [bigquery.SchemaField("LinkID", "STRING")])
    client.load_table_from_dataframe(speedsdf, table, job_config = job_config)


if __name__ == '__main__':
    if sys.argv[1] == 'images':
        save_images_cloud()
    if sys.argv[1] == 'speeds':
        save_speeds_cloud()
