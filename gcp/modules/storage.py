from google.cloud import storage

def create_bucket(bucket_name, project, location):
    storage_client = storage.Client(project=project)
    bucket = storage_client.create_bucket(bucket_name, location=location)
    print(f"Bucket {bucket.name} created")
    return bucket

def delete_bucket(bucket_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    if bucket.exists():
        if len(list(bucket.list_blobs())) > 0:
            print(f"Bucket {bucket.name} is not empty. Please empty the bucket before deleting it.")
            return
        else:
            bucket.delete()
            print(f"Bucket {bucket.name} deleted")
    else:
        print(f"Bucket {bucket_name} does not exist.")