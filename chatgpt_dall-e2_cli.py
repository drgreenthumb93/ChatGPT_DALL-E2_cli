import requests

# set API endpoint
url = "https://api.openai.com/v1/images/generations"

# set API key
api_key = "!SET_YOUR_KEY_HERE!"

# The image generation request
prompt = input("Enter your prompt for the image: ")
image_request = {
  "model": "image-alpha-001",
  "prompt": prompt,
  "num_images":1,
  "size":"1024x1024"
}

# adding API Key to the header
headers = {
  "Content-Type": "application/json",
  "Authorization": "Bearer " + api_key
}

# send the request
response = requests.post(url, headers=headers, json=image_request)

# check the response status code
if response.status_code == 200:
  image = response.json()["data"][0]["url"]
  print("Image URL:", image)
else:
  print("Failed to generate image, status code:", response.status_code)
  print("Response:", response.text)
