from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg

class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    
    
    class Meta:
        model = Movie
        fields = '__all__'
    
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('rating'))['rating__avg']
        
        if rate:
            return round(rate, 1)

        return None

    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError("Release date cannot be before 1990.")
        return value

    def validate_resume(self, value):
        if len(value) > 200:
                raise serializers.ValidationError("Resume must be at most 200 characters long.")
        return value