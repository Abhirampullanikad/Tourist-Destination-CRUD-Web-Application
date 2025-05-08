from rest_framework import serializers
from .models import Destination

from rest_framework import serializers
from .models import Destination

class DestinationSerializer(serializers.ModelSerializer):
    # Handling multiple images (Optional)
    images = serializers.ListField(
        child=serializers.ImageField(), 
        required=False
    )
    
    class Meta:
        model = Destination
        fields = '__all__'
    
    def validate_image(self, value):
        # Optional validation for image size (5MB max)
        if value.size > 5 * 1024 * 1024:
            raise serializers.ValidationError("Image size should not exceed 5MB.")
        return value


        
    