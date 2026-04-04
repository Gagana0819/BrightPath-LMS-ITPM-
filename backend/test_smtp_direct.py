import os
import django
import sys

# Set up Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'brightpath.settings')
django.setup()

from automation.tasks import send_feedback_request_email
from core.models import StudyResource, User

def test_smtp():
    try:
        resource = StudyResource.objects.first()
        if not resource:
            print("No resource found to test with.")
            # Create a mock resource if needed
            return
            
        print(f"Testing SMTP directly (no Celery)...")
        # Call the task function directly (not .delay) to see exceptions here
        result = send_feedback_request_email('brightpathlms2026@gmail.com', resource.id)
        if result:
            print("Email sent successfully according to function return.")
        else:
            print("Email function returned False.")
            
    except Exception as e:
        print(f"SMTP FAILURE: {e}")

if __name__ == '__main__':
    test_smtp()
