from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import FoodItemViewset, UserFoodViewset, CalculateUserCaloriesAPIView

router = DefaultRouter()

router.register(r'food-item', FoodItemViewset, basename='food_item')
router.register(r'user-food', UserFoodViewset, basename='user_food')

urlpatterns = router.urls

urlpatterns += [
    path('calories-calculation/', CalculateUserCaloriesAPIView.as_view(), name='candidate'),
]
