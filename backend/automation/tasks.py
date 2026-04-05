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
from django.core.mail import EmailMultiAlternatives

@shared_task
def send_feedback_request_email(user_email, resource_id):
    from core.models import StudyResource
    try:
        print(f"CELERY DEBUG: Attempting to send feedback email to {user_email} for resource_id {resource_id}")
        resource = StudyResource.objects.get(id=resource_id)
        
        review_url = f"http://localhost:5173/digital-library?review_resource={resource_id}"
        
        subject = f"How was '{resource.title}'?"
        
        # Plain text version
        text_content = f"Hello,\n\nYou recently downloaded '{resource.title}'. We'd love to hear your feedback!\n\nRate it here: {review_url}\n\nThank you,\nBrightPath Team"
        
        # HTML version (Attractive/Premium)
        html_content = f"""
        <div style="font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; max-width: 550px; margin: 0 auto; padding: 40px; border: 1px solid #eee; border-radius: 20px; background: #ffffff;">
            <div style="text-align: center; margin-bottom: 35px;">
                <div style="display: inline-block; padding: 15px; background: #4A90E2; border-radius: 15px; margin-bottom: 15px;">
                   <svg width="40" height="40" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" fill="white"/>
                   </svg>
                </div>
                <h1 style="color: #1e293b; font-size: 26px; font-weight: 800; margin: 0;">We Value Your Opinion!</h1>
            </div>
            
            <p style="color: #475569; font-size: 16px; line-height: 1.6; margin-bottom: 25px;">
                Hi there,<br><br>
                You recently downloaded <strong>{resource.title}</strong>. Did it help with your studies? Your feedback helps thousands of other students on BrightPath find the best resources.
            </p>
            
            <div style="text-align: center; margin: 40px 0;">
                <a href="{review_url}" style="background-color: #4A90E2; color: #ffffff; padding: 18px 40px; text-decoration: none; border-radius: 14px; font-weight: 800; font-size: 16px; display: inline-block; box-shadow: 0 10px 15px -3px rgba(74, 144, 226, 0.3);">
                    Rate & Review Now
                </a>
            </div>
            
            <p style="color: #64748b; font-size: 14px; text-align: center; margin-top: 45px; border-top: 1px solid #f1f5f9; padding-top: 25px;">
                <strong>BrightPath LMS</strong><br>
                The ultimate academic resource hub.
            </p>
        </div>
        """
        
        from_email = settings.EMAIL_HOST_USER
        
        msg = EmailMultiAlternatives(subject, text_content, from_email, [user_email])
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=False)
        
        print(f"CELERY DEBUG: HTML EMAIL SENT SUCCESSFULLY to {user_email}")
        logger.info(f"Successfully sent premium feedback request email to {user_email} for resource {resource_id}")
        return True
    except StudyResource.DoesNotExist:
        print(f"CELERY ERROR: Resource {resource_id} not found in DB")
        logger.error(f"Resource {resource_id} not found for feedback request")
        return False
    except Exception as e:
        print(f"CELERY ERROR: {str(e)}")
        logger.error(f"Failed to send feedback request email: {e}")
        return False
