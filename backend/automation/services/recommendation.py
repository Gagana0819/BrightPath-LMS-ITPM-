from collections import Counter
from core.models import User, UserActivity, Module

class RecommendationEngine:
    @staticmethod
    def get_recommendations_for_user(user_id, limit=5):
        try:
            user = User.objects.get(id=user_id)
            stream = user.stream
            
            # Find what modules other users in the same stream interacted with recently
            peer_activities = UserActivity.objects.filter(
                user__stream=stream
            ).exclude(user_id=user_id)
            
            # Count the frequency of interactions per module
            module_counter = Counter(activity.module_id for activity in peer_activities)
            
            # Exclude modules the user has already interacted with
            user_interacted_modules = set(
                UserActivity.objects.filter(user_id=user_id).values_list('module_id', flat=True)
            )
            
            # Get the top recommended module IDs
            recommended_module_ids = [
                m_id for m_id, count in module_counter.most_common()
                if m_id not in user_interacted_modules
            ][:limit]
            
            # Fetch the actual Module objects
            modules_dict = Module.objects.in_bulk(recommended_module_ids)
            recommended_modules = [modules_dict[m_id] for m_id in recommended_module_ids if m_id in modules_dict]
            
            return recommended_modules
            
        except User.DoesNotExist:
            return []
