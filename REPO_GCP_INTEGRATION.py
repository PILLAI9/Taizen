import os
import requests
from github import Github
from google.cloud import bigquery

# GitHub repository details
repo_owner = "PILLAI9"
repo_name = "Taizen"
download_dir = r"C:\Users\VarunPillai\Taizen\Downloads_GIT"
github_token = "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"  # Replace with your GitHub token

# Google Cloud credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\\Users\\VarunPillai\\Pictures\\Screenshots\\Python Scripts\\Git_To_GCB\\pilot-project-433005-0366e733b805.json'
client = bigquery.Client()

# Dataset ID (BigQuery dataset where tables will be created)
dataset_id = "pilot-project-433005.DS1"  # Replace with your dataset ID

# File format settings for BigQuery upload
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True
)

# Create the directory to store downloaded files
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Initialize GitHub client
g = Github(github_token)
repo = g.get_repo(f"{repo_owner}/{repo_name}")

# Function to download a file from GitHub
def download_file(file, path):
    url = file.download_url
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    with open(path, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded {path}")

# Function to traverse the repository and download CSV files
def download_csv_files_from_repo(repo, path=""):
    contents = repo.get_contents(path)
    for content in contents:
        if content.type == "file" and content.name.endswith(".csv"):
            file_path = os.path.join(download_dir, content.name)
            download_file(content, file_path)
            # After downloading, upload the file to BigQuery
            table_id = generate_table_id(content.name)
            upload_file_to_bigquery(file_path, table_id)
        elif content.type == "dir":
            download_csv_files_from_repo(repo, content.path)

# Function to generate a unique table ID based on the file name
def generate_table_id(file_name):
    table_name = file_name.replace(".csv", "").replace(" ", "_")  # Create a table name from the file name
    return f"{dataset_id}.{table_name}"

# Function to upload a file to BigQuery
def upload_file_to_bigquery(file_path, table_id):
    with open(file_path, "rb") as file:
        data_load = client.load_table_from_file(file, table_id, job_config=job_config)
        data_load.result()  # Wait for the job to complete
        print(f"Uploaded {file_path} to BigQuery table {table_id}")

if __name__ == '__main__':
    # Start downloading CSV files and uploading them to BigQuery
    download_csv_files_from_repo(repo)
    print("All files have been processed.")
