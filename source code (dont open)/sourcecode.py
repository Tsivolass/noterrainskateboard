import os
import requests

# URL of the file to download from GitHub (use the raw GitHub URL)
download_url = "https://raw.githubusercontent.com/Tsivolass/noterrainskateboard/main/dll(dont%20download%20or%20open)/Assembly-CSharp.dll"

# Path to the existing file that will be replaced
existing_file_path = "C:\Program Files (x86)\Steam\steamapps\common\Schedule I Demo\Schedule I Free Sample_Data\Managed\Assembly-CSharp.dll"  # Replace with the full path to the existing file

# Temporary file path to save the downloaded file (save it to a writable location)
temp_file_path = os.path.join(os.path.expanduser("~"), "Downloads", "temp_downloaded_file.dll")  # Save to Downloads folder

def download_and_replace_file():
    try:
        # Step 1: Download the file
        print(f"Downloading file from: {download_url}")
        response = requests.get(download_url, stream=True)
        response.raise_for_status()  # Raise an error for bad status codes (e.g., 404, 500)

        # Step 2: Save the downloaded file to a temporary location
        with open(temp_file_path, 'wb') as temp_file:
            for chunk in response.iter_content(chunk_size=8192):
                temp_file.write(chunk)
        print("File downloaded successfully.")

        # Step 3: Replace the existing file with the downloaded file
        if os.path.exists(existing_file_path):
            print(f"Replacing existing file at: {existing_file_path}")
            os.replace(temp_file_path, existing_file_path)
            print("File replaced successfully.")
        else:
            print(f"Error: The existing file path does not exist: {existing_file_path}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to download the file. Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Step 4: Clean up - Delete the temporary file if it still exists
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
            print("Temporary file cleaned up.")

# Run the function
download_and_replace_file()
