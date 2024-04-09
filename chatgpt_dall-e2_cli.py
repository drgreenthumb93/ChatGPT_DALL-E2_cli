import requests
import json

def generate_image(prompt, api_key):
    # Set API-Endpoint
    url = "https://api.openai.com/v1/images/generations"

    # Create request for image generation
    image_request = {
        "model": "image-alpha-001",
        "prompt": prompt,
        "num_images": 1,
        "size": "1024x1024"
    }

    # Set header with API-KEY
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key
    }

    # send request
    response = requests.post(url, headers=headers, json=image_request)

    # check response
    if response.status_code == 200:
        image_url = response.json()["data"][0]["url"]
        return image_url
    else:
        print("Error while generating image, status code:", response.status_code)
        print("Answer:", response.text)
        return None

def main():
    # setup API-KEY
    api_key = input("Input your API-KEY: ")

    # enter prompt for image gen
    prompt = input("Input your prompt for image geneartion: ")

    # gen image
    image_url = generate_image(prompt, api_key)

    if image_url:
        print("image-URL:", image_url)

if __name__ == "__main__":
    main()
