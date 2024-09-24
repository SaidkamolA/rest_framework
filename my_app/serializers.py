from rest_framework import serializers

from my_app.models import Note


class NoteSerializer(serializers.ModelSerializer):


    class Meta:
        model = Note
        fields = ['id', 'name', 'description', 'created_at', 'done']
        extra_kwargs = {
            'description': {
                'write_only': True
            }
        }


