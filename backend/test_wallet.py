import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'brightpath.settings')
django.setup()

from core.models import PointsWallet, StudyResource
from django.contrib.auth import get_user_model

User = get_user_model()

print("Checking Wallet stats logic...")
try:
    total_resources = StudyResource.objects.count()
    total_students = User.objects.filter(is_active=True).count()
    lecturers = User.objects.filter(is_staff=True).count()
    print(f"Stats: {total_resources}, {total_students}, {lecturers}")
except Exception as e:
    print(f"Error in stats: {e}")

print("Checking Leaderboard logic...")
try:
    top_wallets = PointsWallet.objects.all().order_by('-lifetime_points')[:10]
    for wallet in top_wallets:
        user = wallet.user
        full_name = getattr(user, 'full_name', user.username)
        print(f"User: {full_name}, Points: {wallet.lifetime_points}")
except Exception as e:
    print(f"Error in leaderboard: {e}")
