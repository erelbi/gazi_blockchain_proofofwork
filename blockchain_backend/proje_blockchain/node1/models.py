from django.db import models
import hashlib



def _pcreateHash():
    """Bu fonksiyon 10 karekterli hash üretir"""
    value = BlockChain.objects.values('id').distinct().last()
    if value is None:

        return 0
    else:
        value = BlockChain.objects.values('hash').distinct().last()
        return  value['hash']


class BlockChain(models.Model):
    data = models.CharField(max_length=2)
    p_hash = models.CharField(max_length=64, default=_pcreateHash, unique=True)
    hash = models.CharField(max_length=64, unique=True,  default=None, null=True)
    status = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)


    class Meta:
        app_label = 'node1'

    def save(self,*args,**kwargs):
        """Bu fonksiyon toplam hash üretir"""
        if self.hash is None:
            value = BlockChain.objects.values('id').distinct().last()
            if value is None:
                md5_key = hashlib.md5(str("12").encode())
                self.hash = md5_key.hexdigest()
                super().save(*args, **kwargs)
            else:
                try:
                    total_value = str(self.p_hash + self.data)
                    print(type(total_value), type(self.p_hash), total_value)
                    self.hash = hashlib.md5(total_value.encode()).hexdigest()
                    super().save(*args,**kwargs)
                except Exception as err:
                    print(err)

