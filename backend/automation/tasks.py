from celery import shared_task
from django.core.mail import send_mail
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
        
        send_mail(
            subject,
            message,
            from_email,
            emails,
            fail_silently=False,
        )
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
