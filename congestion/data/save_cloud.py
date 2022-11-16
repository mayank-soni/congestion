import pandas as pd
from congestion.data.get_data import get_images, get_speeds
from google.cloud import bigquery


def save_local():
    '''
    Wrapper function, downloading image and speeds data and saving locally
    '''
    images = get_images()
    save_images_local(images)
    # Download speeds data as .csv
    current_time, speedsdf = get_speeds()
    save_speeds_local(current_time, speedsdf)


def save_images_local(images: dict, verbose: bool = False):
    '''
    Saves images to local disk.
    '''
    print('Saving images to local disk')
    for i, (filename, data) in enumerate(images.items()):
        if verbose:
            print(f'Saving image {i}')
        full_filename = os.path.join(LOCAL_DATA_PATH, 'data-images', filename)
        with open(full_filename, 'wb') as f:
            f.write(data)


def save_speeds_local(current_time: str, speeds_data: pd.DataFrame):
    '''
    Saves speeds dataframe to local disk
    '''
    print('Saving speeds df to local disk')
    filename = os.path.join(LOCAL_DATA_PATH, 'data-speeds', current_time + '_speed.csv')
    speeds_data.to_csv(filename)


if __name__ == '__main__':
    save_local()
