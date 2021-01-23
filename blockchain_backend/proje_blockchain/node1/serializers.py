from .models import BlockChain
from rest_framework import serializers

class BlockChainSerializer(serializers.ModelSerializer):
    # def create(self,**validated_data):
    #     print(validated_data)
    #     return BlockChain.objects.create(**validated_data)
    class Meta:
        model = BlockChain
        # fields = ['data']
        fields = '__all__'