from celery import shared_task
from django.core.mail import EmailMessage
from django.conf import settings
from automation.services.recommendation import RecommendationEngine
from core.models import User
import logging

logger = logging.getLogger(__name__)

@shared_task
def send_resource_notification_email_task(emails, resource_title):
    try:
        subject = f"New Resource Uploaded: {resource_title}"
        message = f"Hello,\n\nA new resource '{resource_title}' has been uploaded to BrightPath LMS. Check it out now!\n\nBest,\nBrightPath Team"
        from_email = settings.EMAIL_HOST_USER
        
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=from_email,
            to=[from_email], # Send to self
            bcc=emails       # BCC all users to protect privacy
        )
        email.send(fail_silently=False)
        
        logger.info(f"Successfully sent notification emails to {len(emails)} users for resource '{resource_title}'")
        return True
    except Exception as e:
        logger.error(f"Failed to send email notification: {e}")
        return False

@shared_task
def request_user_feedback_task():
    # Periodic delayed task to request user feedback
    logger.info("Running requested user feedback periodic task...")
    return "Feedback requests processed"

@shared_task
def update_peer_recommendations_task():
    # Logic to aggregate peer recommendations via Celery
    logger.info("Starting peer recommendation background task...")
    users = User.objects.all()
    for user in users:
        recommendations = RecommendationEngine.get_recommendations_for_user(user.id)
        if recommendations:
            rec_titles = [m.title for m in recommendations]
            logger.info(f"Generated recommendations for User {user.username}: {rec_titles}")
            
    return "Peer recommendations updated"
@shared_task
def send_feedback_request_email(user_email, resource_id):
    from core.models import StudyResource
    try:
        print(f"CELERY DEBUG: Attempting to send feedback email to {user_email} for resource_id {resource_id}")
        resource = StudyResource.objects.get(id=resource_id)
        subject = f"How was the resource: {resource.title}?"
        message = f"Hello,\n\nYou recently downloaded '{resource.title}'. We would love to hear your feedback!\n\nPlease take a moment to rate and review it to help other students.\n\nThank you,\nBrightPath Team"
        from_email = settings.EMAIL_HOST_USER
        
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=from_email,
            to=[user_email]
        )
        email.send(fail_silently=False)
        print(f"CELERY DEBUG: EMAIL SENT SUCCESSFULLY to {user_email}")
        
        logger.info(f"Successfully sent feedback request email to {user_email} for resource {resource_id}")
        return True
    except StudyResource.DoesNotExist:
        print(f"CELERY ERROR: Resource {resource_id} not found in DB")
        logger.error(f"Resource {resource_id} not found for feedback request")
        return False
    except Exception as e:
        print(f"CELERY ERROR: {str(e)}")
        logger.error(f"Failed to send feedback request email: {e}")
        return False
