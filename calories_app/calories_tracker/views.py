from django.db.models import Sum
from rest_framework import viewsets, status, authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from calories_tracker.models import FoodItem, UserFood
from calories_tracker.serializer import FoodItemSerializer, UserFoodSerializer


class FoodItemViewset(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = [u'get', u'post', u'put', u'delete']
    serializer_class = FoodItemSerializer

    def get_queryset(self):
        return FoodItem.objects.all()

    def list(self, request, *args, **kwargs):
        """
        API to list all the food items

        Response:
            {
                "message": "Food Item List",
                "success": true,
                "status": 200,
                "data": [
                    {
                        "id": 2,
                        "food_name": "Puff",
                        "calories": "125.00",
                        "protein": "50.00",
                        "fat": "10.00"
                    }
                ]
            }
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(
            {
                'message': 'Food Item List',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': serializer.data
            }
        )

    def retrieve(self, request, *args, **kwargs):
        """
        API to retrieve particular food item

        Response:
            {
                "message": "Food Item Details",
                "success": true,
                "status": 200,
                "data": {
                    "id": 2,
                    "food_name": "Puff",
                    "calories": "125.00",
                    "protein": "50.00",
                    "fat": "10.00"
                }
            }
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response(
            {
                'message': 'Food Item Details',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': serializer.data
            }
        )

    def create(self, request, *args, **kwargs):
        """
        API to add new food item

        Request:
            {
                "food_name": "Puff",
                "calories": "125",
                "protein": "50",
                "fat": "10"
            }

        Response:
            {
                "message": "Food item added successfully",
                "success": true,
                "status": 200,
                "data": {
                    "id": 3,
                    "food_name": "Puff",
                    "calories": "125.00",
                    "protein": "50.00",
                    "fat": "10.00"
                }
            }
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(
            {
                'message': 'Food item added successfully',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': serializer.data
            }
        )

    def update(self, request, *args, **kwargs):
        """
        API to update food item

        Request:
            {
                "food_name": "Burger",
                "calories": "125",
                "protein": "50",
                "fat": "10"
            }

        Response:
            {
                "message": "Food item updated successfully",
                "success": true,
                "status": 200,
                "data": {
                    "id": 3,
                    "food_name": "Burger",
                    "calories": "125.00",
                    "protein": "50.00",
                    "fat": "10.00"
                }
            }
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(
            {
                'message': 'Food item updated successfully',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': serializer.data
            }
        )

    def destroy(self, request, *args, **kwargs):
        """
        API to delete food item

        Response:
            {
                "message": "Food item deleted successfully",
                "success": true,
                "status": 204,
                "data": []
            }
        """
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response(
            {
                'message': 'Food item deleted successfully',
                'success': True,
                'status': status.HTTP_204_NO_CONTENT,
                'data': []
            },
            status=status.HTTP_204_NO_CONTENT
        )


class UserFoodViewset(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = [u'get', u'post', u'put', u'delete']
    serializer_class = UserFoodSerializer

    def get_queryset(self):
        return UserFood.objects.all()

    def list(self, request, *args, **kwargs):
        """
        API to list all user food items

        Response:
            {
                "message": "User food List",
                "success": true,
                "status": 200,
                "data": [
                    {
                        "id": 2,
                        "user": {
                            "pk": 1,
                            "username": "admin",
                            "first_name": "admin",
                            "last_name": "admin",
                            "email": "admin@admin.com",
                            "mobile": "8141216525",
                            "joined_date": "2023-02-21T09:44:33.844577Z",
                            "update_date": "2023-02-21T09:44:33.955840Z",
                            "is_active": true,
                            "is_staff": true
                        },
                        "food": {
                            "id": 2,
                            "food_name": "Puff",
                            "calories": "125.00",
                            "protein": "50.00",
                            "fat": "10.00"
                        }
                    },
                    {
                        "id": 3,
                        "user": {
                            "pk": 1,
                            "username": "admin",
                            "first_name": "admin",
                            "last_name": "admin",
                            "email": "admin@admin.com",
                            "mobile": "8141216525",
                            "joined_date": "2023-02-21T09:44:33.844577Z",
                            "update_date": "2023-02-21T09:44:33.955840Z",
                            "is_active": true,
                            "is_staff": true
                        },
                        "food": {
                            "id": 2,
                            "food_name": "Puff",
                            "calories": "125.00",
                            "protein": "50.00",
                            "fat": "10.00"
                        }
                    }
                ]
            }
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(
            {
                'message': 'User food List',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': serializer.data
            }
        )

    def retrieve(self, request, *args, **kwargs):
        """
        API to retrieve particular user food item

        Response:
            {
                "message": "User food Details",
                "success": true,
                "status": 200,
                "data": {
                    "id": 2,
                    "user": {
                        "pk": 1,
                        "username": "admin",
                        "first_name": "admin",
                        "last_name": "admin",
                        "email": "admin@admin.com",
                        "mobile": "8141216525",
                        "joined_date": "2023-02-21T09:44:33.844577Z",
                        "update_date": "2023-02-21T09:44:33.955840Z",
                        "is_active": true,
                        "is_staff": true
                    },
                    "food": {
                        "id": 2,
                        "food_name": "Puff",
                        "calories": "125.00",
                        "protein": "50.00",
                        "fat": "10.00"
                    }
                }
            }
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response(
            {
                'message': 'User food Details',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': serializer.data
            }
        )

    def create(self, request, *args, **kwargs):
        """
        API to create user food item

        Request:
            {
                "user_id": 1,
                "food_id": 2
            }

        Response:
            {
                "message": "User food added successfully",
                "success": true,
                "status": 200,
                "data": {
                    "id": 4,
                    "user": {
                        "pk": 1,
                        "username": "admin",
                        "first_name": "admin",
                        "last_name": "admin",
                        "email": "admin@admin.com",
                        "mobile": "8141216525",
                        "joined_date": "2023-02-21T09:44:33.844577Z",
                        "update_date": "2023-02-21T09:44:33.955840Z",
                        "is_active": true,
                        "is_staff": true
                    },
                    "food": {
                        "id": 2,
                        "food_name": "Puff",
                        "calories": "125.00",
                        "protein": "50.00",
                        "fat": "10.00"
                    }
                }
            }
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(
            {
                'message': 'User food added successfully',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': serializer.data
            }
        )

    def update(self, request, *args, **kwargs):
        """
        API to update user food item

        Request:
            {
                "user_id": 1,
                "food_id": 4
            }

        Response:
            {
                "message": "User food added successfully",
                "success": true,
                "status": 200,
                "data": {
                    "id": 5,
                    "user": {
                        "pk": 1,
                        "username": "admin",
                        "first_name": "admin",
                        "last_name": "admin",
                        "email": "admin@admin.com",
                        "mobile": "8141216525",
                        "joined_date": "2023-02-21T09:44:33.844577Z",
                        "update_date": "2023-02-21T09:44:33.955840Z",
                        "is_active": true,
                        "is_staff": true
                    },
                    "food": {
                        "id": 4,
                        "food_name": "Burger",
                        "calories": "160.00",
                        "protein": "20.00",
                        "fat": "40.00"
                    }
                }
            }
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(
            {
                'message': 'User food updated successfully',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': serializer.data
            }
        )

    def destroy(self, request, *args, **kwargs):
        """
        API to delete user food item

        Response:
            {
                "message": "User food deleted successfully",
                "success": true,
                "status": 204,
                "data": []
            }
        """
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response(
            {
                'message': 'User food deleted successfully',
                'success': True,
                'status': status.HTTP_204_NO_CONTENT,
                'data': []
            },
            status=status.HTTP_204_NO_CONTENT
        )


class CalculateUserCaloriesAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = [u'get']

    def get(self, request):
        """
        API to calculate calories for particular user

        Response:
            {
                "message": "User Food Calories Calculation",
                "success": true,
                "status": 200,
                "data": 375.0
            }
        """
        user_food_obj = UserFood.objects.filter(user=request.user).aggregate(Sum('food__calories'))
        total_consumed_calories = user_food_obj.get('food__calories__sum')

        return Response(
            {
                'message': 'User Food Calories Calculation',
                'success': True,
                'status': status.HTTP_200_OK,
                'data': total_consumed_calories
            }
        )
