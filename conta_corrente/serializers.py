from conta_corrente.models import ContaCorrente
from rest_framework.serializers import ModelSerializer

class ContaCorrenteSerializer(ModelSerializer):
    class Meta:
        model = ContaCorrente
        fields = ["id", "numero_conta", "saldo"]
