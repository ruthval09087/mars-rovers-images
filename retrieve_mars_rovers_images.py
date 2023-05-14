import requests

# Define the API endpoint
url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"

# Set the API parameters
params = {
    "sol": 1000,  # Martian sol (day) to retrieve images from
    "api_key": "YOUR_API_KEY"  # Replace with your NASA API key
}

# Send a GET request to the API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Retrieve the first image URL from the response
    if data["photos"]:
        image_url = data["photos"][0]["img_src"]
        print("Image URL:", image_url)
    else:
        print("No images available for the given parameters.")
else:
    print("Error:", response.status_code)
