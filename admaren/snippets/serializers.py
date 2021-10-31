from __future__ import unicode_literals
from rest_framework import serializers
from snippets import models as snippets_models


class SnippetsSerializer(serializers.ModelSerializer):
    tag = serializers.CharField( required=False)

    def create(self, validated_data):
        tag = validated_data.get('tag')
        validated_data['created_by'] = self.context['request'].user
        get_tag_data = snippets_models.Tag.objects.filter(name=tag)
        if get_tag_data.exists():
            validated_data['tag'] = get_tag_data.first()
        else:
            tag_dict = {}
            tag_dict['name'] = tag
            new_tag = snippets_models.Tag(**tag_dict)
            new_tag.save()
            validated_data['tag'] = new_tag
        snippet = snippets_models.TextSnippet(**validated_data)
        snippet.save()
        return snippet

    class Meta:
        model = snippets_models.TextSnippet
        fields =('id','text','datetime_created','datetime_updated','tag','created_by')


class SnippetsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = snippets_models.TextSnippet
        fields =('id','text','datetime_created','datetime_updated','tag','created_by')


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = snippets_models.Tag
        exclude = ()
