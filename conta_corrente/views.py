from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from conta_corrente.serializers import ContaCorrenteSerializer
from conta_corrente.models import ContaCorrente

class ContaApiView(viewsets.ViewSet):

    def list(self, request):
        queryset = ContaCorrente.objects.all()
        serializer = ContaCorrenteSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        queryset = ContaCorrente.objects.create(
            numero_conta=request.data["numero_conta"],
            saldo=request.data["saldo"]
        )
        serializer = ContaCorrenteSerializer(queryset)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
            queryset = ContaCorrente.objects.all()
            conta = get_object_or_404(queryset, pk=pk)
            serializer = ContaCorrenteSerializer(conta)
            return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def saque(self, request, pk=None):
        valor = request.data["valor"]
        queryset = ContaCorrente.objects.all()
        conta = get_object_or_404(queryset, pk=pk)
        if conta:
            if conta.saldo > valor:
                conta.saldo = conta.saldo - valor
                conta.save()
            else:
                return Response({"Operação Inválida": "Saldo abaixo do valor de saque"})
        serializer = ContaCorrenteSerializer(conta)
        return Response(serializer.data)


    @action(detail=True, methods=['put'])
    def deposito(self, request, pk=None):
        valor = request.data["valor"]
        queryset = ContaCorrente.objects.all()
        conta = get_object_or_404(queryset, pk=pk)
        if conta:
            conta.saldo = conta.saldo + valor
            conta.save()
        serializer = ContaCorrenteSerializer(conta)
        return Response(serializer.data)
