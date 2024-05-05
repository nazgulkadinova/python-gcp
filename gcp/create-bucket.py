from modules.storage import create_bucket

if __name__ == "__main__":
    bucket_name = "python-bucket-aika"
    project = "proven-dryad-417822"
    location = "us-central1"
    create_bucket(bucket_name, project, location)