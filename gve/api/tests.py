import json

from datetime import date
from django.test import TestCase
from rest_framework import status
from api.models import CarroModel
from api.models import RegistroModel
from api.models import CdcModel
from django.urls import reverse, resolve


class CarroTestClass(TestCase):
    '''
    Classe para testes do recurso carros:list
    '''

    def setUp(self):
        '''
        Inicialização das varíaveis que serão
        utilizadas durante o teste
        '''

        self.data = {'fabricante': 'FORD', 'modelo': 'HB20',
                     'data_criacao': '11/03/2020', 'placa': 'IRD0808', 'quilometragem': 12000}

    def test_get(self):
        '''
        Testa a listagem dos objetos do recurso
        '''

        response = self.client.get(reverse('carros-list'))
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        '''
        Testa a inserção de um novo recurso
        '''

        response = self.client.post(reverse('carros-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CarroModel.objects.count(), 1)
        self.assertEqual(CarroModel.objects.get().fabricante, 'FORD')
        self.assertEqual(CarroModel.objects.get().modelo, 'HB20')
        self.assertEqual(CarroModel.objects.get().data_criacao, date.today())
        self.assertEqual(CarroModel.objects.get().placa, 'IRD0808')
        self.assertEqual(CarroModel.objects.get().quilometragem, 12000)


class CarroDetailTestClass(TestCase):
    '''
    Classe para testes do recurso carros:detail
    '''

    def setUp(self):
        '''
        Inicialização das varíaveis que serão
        utilizadas durante o teste
        '''

        self.data = {'fabricante': 'FORD', 'modelo': 'HB20',
                     'data_criacao': '11/03/2020', 'placa': 'IRD0808', 'quilometragem': 12000}

        self.putdata = json.dumps({'fabricante': 'FORD', 'modelo': 'Ka',
                                   'data_criacao': '11/03/2020', 'placa': 'IRD0808', 'quilometragem': 12000})

        self.client.post(reverse('carros-list'), self.data)

        self.url = reverse("carros-detail", kwargs={"pk": 1})

    def test_get(self):
        '''
        Testa a leitura de um objeto do recurso
        '''

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put(self):
        '''
        Testa a atualização de um objeto do recurso
        '''

        response = self.client.put(
            self.url, data=self.putdata, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        '''
        Testa a deleção de um objeto do recurso
        '''

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CdcTestClass(TestCase):
    '''
    Classe para testes do recurso cdc:list
    '''

    def setUp(self):
        '''
        Inicialização das varíaveis que serão
        utilizadas durante o teste
        '''

        self.data = {'nome': 'Inovação'}

    def test_get(self):
        '''
        Testa a listagem dos objetos do recurso
        '''

        response = self.client.get(reverse('cdcs-list'))
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        '''
        Testa a inserção de um novo recurso
        '''

        response = self.client.post(reverse('cdcs-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CdcModel.objects.count(), 1)
        self.assertEqual(CdcModel.objects.get().nome, 'Inovação')


class CdcDetailTestClass(TestCase):
    '''
    Classe para testes do recurso cdcs:detail
    '''

    def setUp(self):
        '''
        Inicialização das varíaveis que serão
        utilizadas durante o teste
        '''

        self.data = {'nome': 'Inovação'}

        self.putdata = json.dumps({'nome': 'Operações'})

        self.client.post(reverse('cdcs-list'), self.data)

        self.url = reverse("cdcs-detail", kwargs={"pk": 1})

    def test_get(self):
        '''
        Testa a leitura de um objeto do recurso
        '''

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put(self):
        '''
        Testa a atualização de um objeto do recurso
        '''

        response = self.client.put(
            self.url, data=self.putdata, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        '''
        Testa a deleção de um objeto do recurso
        '''

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class RegistroTestClass(TestCase):
    '''
    Classe para testes do recurso registro:list
    '''

    def setUp(self):
        '''
        Inicialização das varíaveis que serão
        utilizadas durante o teste
        '''
        self.data = {'data_final': '', 'condutor': 'Josnei da Silva', 'descricao': 'Visita na empresa X',
                     'quilometragem_inicial': 1002, 'quilometragem_final': '', 'id_carro': 1, 'id_cdc': 1}
        self.client.post(reverse('carros-list'), data={'fabricante': 'FORD', 'modelo': 'HB20',
                                                       'data_criacao': '11/03/2020', 'placa': 'IRD0808', 'quilometragem': 12000})
        self.client.post(reverse('cdcs-list'), data={'nome': 'Inovação'})

    def test_get(self):
        '''
        Testa a listagem dos objetos do recurso
        '''
        response = self.client.get(reverse('registros-list'))
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        '''
        Testa a inserção de um novo recurso
        '''
        response = self.client.post(reverse('registros-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RegistroModel.objects.count(), 1)
        self.assertEqual(
            RegistroModel.objects.get().data_inicial, date.today())
        self.assertEqual(RegistroModel.objects.get().condutor,
                         'Josnei da Silva')
        self.assertEqual(RegistroModel.objects.get().id_carro.placa, 'IRD0808')
        self.assertEqual(RegistroModel.objects.get().id_carro.modelo, 'HB20')
        self.assertEqual(RegistroModel.objects.get().id_cdc.nome, 'Inovação')
        self.assertEqual(
            RegistroModel.objects.get().quilometragem_inicial, 1002)


class RegistroDetailTestClass(TestCase):
    '''
    Classe para testes do recurso registros:detail
    '''

    def setUp(self):
        '''
        Inicialização das varíaveis que serão
        utilizadas durante o teste
        '''

        self.client.post(reverse('carros-list'), data={'fabricante': 'FORD', 'modelo': 'HB20',
                                                       'data_criacao': '11/03/2020', 'placa': 'IRD0808', 'quilometragem': 12000})
        self.client.post(reverse('cdcs-list'), data={'nome': 'Inovação'})

        self.client.post(reverse('registros-list'), {'data_final': '', 'condutor': 'Josnei da Silva', 'descricao': 'Visita na empresa X',
                                                     'quilometragem_inicial': 1002, 'quilometragem_final': '', 'id_carro': 1, 'id_cdc': 1})

        self.putdata = json.dumps({'data_final': '2020-02-11', 'condutor': 'Josnei da Silva', 'descricao': 'Visita na empresa X',
                                   'quilometragem_inicial': 1002, 'quilometragem_final': 2000, 'id_carro': 1, 'id_cdc': 1})

        self.url = reverse("registros-detail", kwargs={"pk": 1})

    def test_get(self):
        '''
        Testa a leitura de um objeto do recurso
        '''

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put(self):
        '''
        Testa a atualização de um objeto do recurso
        '''

        response = self.client.put(
            self.url, data=self.putdata, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        '''
        Testa a deleção de um objeto do recurso
        '''

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
