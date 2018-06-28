from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = File
        fields = ('file','owner')
        read_only_fields = ('owner',)
        
    def validate_file(self, value):
        if not value.content_type.startswith('audio'):
            raise serializers.ValidationError("Non-audio file provided - check the file extension")            
        return value    
