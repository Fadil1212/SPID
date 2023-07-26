from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

# Specify the search queries as a list
search_queries = ["Michael Jordan images free download"]

num_images = 100  # Set the desired number of images to download
output_directory = "kobe_bryant_images"  # Set the directory to save the downloaded images

# Define the download arguments
download_args = {
    "limit": num_images,
    "output_directory": output_directory,
}

for query in search_queries:
    download_args["keywords"] = query
    response.download(download_args)
