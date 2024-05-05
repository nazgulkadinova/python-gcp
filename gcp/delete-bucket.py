from modules.storage import delete_bucket

def main():
    bucket_name = input("Enter the name of the bucket to delete: ")
    delete_bucket(bucket_name)

if __name__ == "__main__":
    main()