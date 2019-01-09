from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICE, STYLE_CHOICE

# class SnippetSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style=['base_template', 'textarea.html'])
#     lineons = serializers.BooleanField(required=False)
#     language = serializers.CharField(choices=LANGUAGE_CHOICE, default='python')
#     style = serializers.CharField(choices=STYLE_CHOICE, default='friendly')

#     def create(self, validated_data):
#         return Snippet.objectes.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.lineons = validated_data.get('lineons', instance.lineons)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
