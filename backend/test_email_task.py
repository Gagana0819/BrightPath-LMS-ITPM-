import os
import django
import sys

# Set up Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'brightpath.settings')
django.setup()

from automation.tasks import send_feedback_request_email
from core.models import StudyResource

def test_task():
    try:
        resource = StudyResource.objects.first()
        if not resource:
            print("No resource found to test with.")
            return
            
        print(f"Triggering test task for resource: {resource.title} and user: brightpathlms2026@gmail.com")
        # Trigger immediately for testing (no countdown)
        result = send_feedback_request_email.delay('brightpathlms2026@gmail.com', resource.id)
        print(f"Task sent to Celery. Task ID: {result.id}")
        
    except Exception as e:
        print(f"Error triggering test task: {e}")

if __name__ == '__main__':
    test_task()
