import os
import django
import sys

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'brightpath.settings')
django.setup()

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def test_s3_upload():
    try:
        path = 'test_upload.txt'
        content = ContentFile(b'Hello Supabase S3!')
        filename = default_storage.save(path, content)
        print(f"File uploaded successfully to: {filename}")
        
        # Verify URL
        url = default_storage.url(filename)
        print(f"File URL: {url}")
        
        # Cleanup
        # default_storage.delete(filename)
        # print("Test file deleted from S3.")
    except Exception as e:
        print(f"Error during S3 upload: {e}")

if __name__ == "__main__":
    test_s3_upload()
