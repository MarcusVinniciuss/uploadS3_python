import boto3
import logging
import glob, os
from botocore.exceptions import NoCredentialsError
from botocore.exceptions import F
from pathlib import Path
from datetime import date

ACCESS_KEY = 'your access_key'
SECRET_KEY = 'your secret_key'

logging.root.handlers = []
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO , filename='uploadS3.log')
console = logging.StreamHandler()
console.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
console.setFormatter(formatter)
logging.getLogger("").addHandler(console)

today = date.today()


def upload_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    try:
        s3.upload_file(local_file, bucket, s3_file)
        logging.info("File {} uploaded was successful".format(file))
        print("Upload Successful - {}".format(file))
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

os.chdir("path_files")
for file in glob.glob("*.txt"):
    uploaded = upload_aws(file, 'your_bucket_name', file)