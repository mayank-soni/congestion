import pandas as pd
import os
from congestion.data.params import LOCAL_DATA_PATH, MACHINE, VM_DATA_PATH
from congestion.data.get_data import get_images, get_speeds

def save_local():
    '''
    Wrapper function, downloading image and speeds data and saving locally
    '''
    images = get_images()
    save_images_local(images)
    speedsdf = get_speeds()
    save_speeds_local(speedsdf)


def save_images_local(images: dict, verbose: bool = False):
    '''
    Saves images to local disk.
    '''
    print('Saving images to local disk')
    for i, (filename, data) in enumerate(images.items()):
        if verbose:
            print(f'Saving image {i}')
        machine_filename = os.path.join(get_image_path(), filename)
        with open(machine_filename, 'wb') as f:
            f.write(data)


def save_speeds_local(speeds_data: pd.DataFrame):
    '''
    Saves speeds dataframe to local disk
    '''
    print('Saving speeds df to local disk')
    filename = os.path.join(LOCAL_DATA_PATH, 'data-speeds', 'speeds.csv')
    # Write header to file if it is new, otherwise, no header
    if os.path.exists(filename):
        speeds_data.to_csv(filename, mode = 'a', header = False)
    else:
        speeds_data.to_csv(filename, mode = 'a', header = True)


def get_image_path() -> str:
    '''
    Returns correct path to local folder for saving images, depending on MACHINE.
    '''
    if MACHINE == 'local':
        machine_image_folder = os.path.join(LOCAL_DATA_PATH, 'data-images')
    elif MACHINE == 'vm':
        machine_image_folder = os.path.join(VM_DATA_PATH, 'data-images')
    else:
        raise ValueError(f'Value of $MACHINE, {MACHINE = }, not recognised')
    return machine_image_folder


if __name__ == '__main__':
    save_local()
