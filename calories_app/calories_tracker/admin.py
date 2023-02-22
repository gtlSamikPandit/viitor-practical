from django.contrib import admin

from calories_tracker.models import FoodItem, UserFood


class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'calories', 'protein', 'fat')
    readonly_fields = ('created', 'modified')
    ordering = ('id',)


class UserFoodAdmin(admin.ModelAdmin):
    list_display = ('get_food_item',)
    readonly_fields = ('created', 'modified')
    ordering = ('id',)

    def get_food_item(self, obj):
        return str(obj.food.id) + ' | ' + obj.food.food_name


admin.site.register(FoodItem, FoodItemAdmin)
admin.site.register(UserFood, UserFoodAdmin)
