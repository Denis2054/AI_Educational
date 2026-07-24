import json
import requests
from google.colab import userdata
def download(folder, filename):
    """
    Downloads a file from the private GitHub repository using a Colab Secret.
    """
    # 1. Securely retrieve the GitHub token
    try:
        github_token = userdata.get('github')
    except userdata.SecretNotFoundError:
        raise ValueError("GitHub token not found. Add a secret named 'github' in the Colab Secrets panel.")

    # 2. Construct the raw URL
    # (Assuming the main branch of your specific repository)
    repo_base_url = "https://raw.githubusercontent.com/Denis2054/SFT/main"
    url = f"{repo_base_url}/{folder}/{filename}"

    # 3. Set up the authorization header
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3.raw"
    }

    # 4. Download and save the file
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(filename, 'w') as f:
            f.write(response.text)
        print(f"Successfully downloaded {filename} from {folder}/")
    else:
        print(f"Failed to download {filename}. Status code: {response.status_code}")
        print(f"Attempted URL: {url}")
