import hashlib
import random
import string
from time import sleep

import requests
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from channels.layers import get_channel_layer
from django.http import HttpRequest, HttpResponse, StreamingHttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework import viewsets, permissions
from proje_blockchain.node1.models import BlockChain
from proje_blockchain.node1.serializers import BlockChainSerializer
from rest_framework.response import Response
from rest_framework import status
import json
from .signals import miner_resp
import subprocess


class CreatBlock(APIView):
    queryset = BlockChain.objects.all()

    def post(self, request: HttpRequest, *args, **kwargs):
        print(request.body.decode('utf-8'))
        serializer = BlockChainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Mining(APIView):

    def get(self, request: HttpRequest, *args, **kwargs):
        print(request.get_full_path())
        status = request.GET.get('status')
        raw_data = BlockChain.objects.filter(status=status)
        if raw_data.count() == 0:
            return Response({'id': None})
        else:
            return Response(raw_data.values('id', 'p_hash', 'hash').first())

    def put(self, request: HttpRequest, *args, **kwargs):
        value = json.loads(request.body.decode("utf-8"))
        print(type(value))
        block = BlockChain.objects.filter(id=int(value['id'])).update(status=True)
        return HttpResponse(status=200)


class BlockView(viewsets.ReadOnlyModelViewSet):
    queryset = BlockChain.objects.all()
    serializer_class = BlockChainSerializer
    permission_classes = [permissions.AllowAny]


def gen_message(msg):
    return json.dumps({'data': msg})


def register(id):
    BlockChain.objects.filter(id=id).update(status=True)


def search_unregister():
    try:
        raw_data = BlockChain.objects.filter(status=False)
        resp = raw_data.values('id', 'p_hash', 'hash').first()
    except Exception as err:
        print(err)
    mining(resp['id'], resp['p_hash'], resp['hash'])


def mining(id, p_hash, hash_value):
    c = 0
    while True:
        data_x = ''.join(random.choices(string.ascii_letters + string.digits, k=2))
        ws(p_hash)
        c += 1
        if p_hash == "0":
            hash_calc = hashlib.md5(data_x.encode())
            ws("ilk düğüm  : {}---->\n{}<----\n".format(hash_calc.hexdigest(), hash_value))
        else:
            total_value = str(p_hash + data_x)
            hash_calc = hashlib.md5(total_value.encode())
            # print("yeni düğüm ekleniyor : {}----->{}".format(hash_calc.hexdigest(), hash_value))
            if c % 10:
                ws("{}------->{}".format(hash_calc.hexdigest(), hash_value))
        if hash_calc.hexdigest() == hash_value:
            ws("Bulunan hash: {}".format(hash_calc.hexdigest()))
            ws("Buldun Tebrikler")
            sleep(3)
            ws("Düğüm onaylanıyor........")
            register(id)
            break


def ws(data):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "miner", {"type": "miner.miner",
                  "event": "mining",
                  "resp": data})


def run_miner(request: HttpRequest):
    search_unregister()
    return HttpResponse(status=200)
