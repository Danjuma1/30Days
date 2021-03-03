import os
import requests
import shutil

def download_file(url, directory, fname=None):
    if fname == None:
        fname = os.path.basename(url)
    dl_path = os.path.join(directory, dl_filename)
    with requests.get(url, stream=True) as r:
        with open(dl_path, 'wb') as file_obj:
            shutil.copyfileobj(r.raw, file_obj)
    return dl_filename