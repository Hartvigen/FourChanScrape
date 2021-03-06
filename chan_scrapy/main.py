import subprocess
import os
import shutil
import time
from PIL import Image
from trans import has_transparency

download_folder = "chan_scrapy\\DownloadedImages\\full"
kept_folder = "chan_scrapy\\KeptImages"

#downloader = subprocess.Popen('scrapy crawl chanCrawler', shell=True)
downloader = subprocess.Popen('scrapy crawl chanCrawler', shell=True)
downloader.wait()

for file in os.listdir(download_folder):
    filename = os.fsdecode(file)
    if filename.endswith(".png"):
        im = Image.open(download_folder + "\\" + file, 'r')
        im.load() #file is loaded so that it closes sorting of images finishes, even if the image itself is not sorted
        if has_transparency(im):
            shutil.move(download_folder + "\\" + file, kept_folder + "\\" + file)
            print(filename + " is transparent!")
        


#remove any files not matching your criteria
#shutil.rmtree(download_folder)
