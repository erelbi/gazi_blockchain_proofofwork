from django.db.models.signals import post_save,pre_init
from django.dispatch import receiver, Signal
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

miner_resp = Signal(providing_args=["resp"])

def miner_response(**kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "miner", {"type": "working.miner",
                   "event": "mining",
                   "resp": kwargs["resp"]})
