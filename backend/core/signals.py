from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import PointsWallet, PointTransaction, StudyResource, KuppiSession, ResourceReview, Notification
from django.db import transaction

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_wallet(sender, instance, created, **kwargs):
    if created:
        PointsWallet.objects.get_or_create(user=instance)

def _award_points(user, amount, action_type, description):
    """Helper to update wallet and record transaction."""
    with transaction.atomic():
        wallet, created = PointsWallet.objects.get_or_create(user=user)
        wallet.balance += amount
        wallet.lifetime_points += amount
        
        # Update Tier
        if wallet.lifetime_points >= 7000:
            wallet.tier = 'PLATINUM'
        elif wallet.lifetime_points >= 3000:
            wallet.tier = 'GOLD'
        elif wallet.lifetime_points >= 1000:
            wallet.tier = 'SILVER'
        else:
            wallet.tier = 'BRONZE'
            
        wallet.save()
        
        PointTransaction.objects.create(
            wallet=wallet,
            points=amount,
            action_type=action_type,
            description=description
        )

        # Create In-app Notification
        Notification.objects.create(
            user=user,
            title=f"Points Earned: +{amount} BP",
            message=description,
            notification_type='POINTS'
        )


@receiver(post_save, sender=KuppiSession)
def award_points_on_session(sender, instance, created, **kwargs):
    if created:
        _award_points(
            instance.tutor,
            100,
            "Kuppi Session Created",
            f"Scheduled a new session: {instance.title}"
        )

@receiver(post_save, sender=ResourceReview)
def award_points_on_review(sender, instance, created, **kwargs):
    if created and instance.rating >= 4:
        _award_points(
            instance.resource.user, # Uploader gets the points
            10,
            "Positive Review Bonus",
            f"Received a {instance.rating}-star review for {instance.resource.title}"
        )
