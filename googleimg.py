# from google_images_download import google_images_download   #importing the library

# response = google_images_download.googleimagesdownload()   #class instantiation

# arguments = {"keywords":"쿨톤","limit":50,"print_urls":True,"format":'jpg'}   #creating list of arguments
# paths = response.download(arguments)   #passing the arguments to the function
# print(paths)   #printing absolute paths of the downloaded images

from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"이영애, 태연, 손예진, 홍빈, 차은우, 최강창민, 박보검, 이효리, 박보영, 박신혜","limit":50,"print_urls":True,"format":"jpg"}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images