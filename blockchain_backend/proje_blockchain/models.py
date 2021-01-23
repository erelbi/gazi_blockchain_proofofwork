# import os
# from binascii import hexlify
#
# from django.db import models
#
# def _pcreateHash():
#     """Bu fonksiyon 10 karekterli hash üretir"""
#     return hexlify(os.urandom(5))
#
# def _makehash():
#     """Bu fonksiyon toplam hash üretir"""
#     data = BlockChain.objects.last('data')
#     p_hash = BlockChain.objects.last('p_hash')
#     return hexlify(os.urandom(5))
#
#
# class BlockChain(models.Model):
#     data = models.CharField(max_length=3)
#     p_hash = models.CharField(max_length=10, default=_pcreateHash, unique=True)
#     hash = models.CharField(max_length=10, default=_makehash, unique=True)
#     status = models.BooleanField(default=False)
#     class Meta:
#         app_label = 'node1'
#     def __str__(self):
#         return self.data