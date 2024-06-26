from rest_framework import serializers
from .models import *

class PieceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PieceImage
        fields = '__all__'

class PieceSerializer(serializers.ModelSerializer):
    thumbs = PieceImageSerializer(many=True,read_only=True)
    # thumbs = serializers.SerializerMethodField()
    piece_images= serializers.ListField(
                child = serializers.ImageField(max_length =1000000,allow_empty_file=False,
                                              use_url = False),
                                               write_only=True
                                               )                               
    class Meta:
        model = Piece
        fields =('id','id_marchand','id_cathegorie','marque','modole','name','price','qt_stock','description','piece_images','thumbs')
    def create(self, validated_data):
        piece_images = validated_data.pop('piece_images')
        piece = Piece.objects.create(**validated_data)

        for piece_image in piece_images:
            PieceImage.objects.create(thumbs=piece,piece_image=piece_image)

        return piece

    def get_thumbs(self,instace):
        queryset = instace.pieceImage.all()
        request = self.context.get('request')
        serializers = PieceImageSerializer(queryset,context={'request':request})
        return serializers.data


class CathegorieSerializer(serializers.ModelSerializer):
    pieces =serializers.SerializerMethodField()
    class Meta:
        model = Cathegorie
        fields = ('id','name','thumbs','pieces')

    def create(self, validated_data):
        
        # pieces = validated_data.pop('pieces')
        # print(validated_data)
        queryset = Cathegorie.objects.create(**validated_data)
        return queryset
    
    def get_pieces(self,instance):
        queryset = instance.pieces.all()
        request= self.context.get('request')
        serializers = PieceSerializer(queryset,many=True,context = {'request':request})
        return serializers.data
    
class CommandeSerializer(serializers.ModelSerializer):
    # piece = PieceSerializer (many = True)
    # multiple_piece_commande = serializers.ListField(
    #     child = PieceSerializer(many = True),
    #     write_only = True 
    # )
    class Meta:
        model = Commande
        fields ='__all__'

    # def create(self, validated_data):
    #     multiple_piece_commande = validated_data.pop('multiple_piece_commande')
    #     commande = Commande.objects.create(**validated_data)
    #     for pieces in multiple_piece_commande:
    #         nem_piece = Piece.objects.create(Commande)