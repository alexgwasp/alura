# -*- coding: UTF-8 -*-

class Perfil(object):
    'Classe para padrão de perfis de usuários'

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0
    
    def curtir(self):
        self.__curtidas+=1

    def obter_curtidas(self):
        return self.__curtidas

    @classmethod
    def gerar_perfis(classe, nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        perfis = []
        for linha in arquivo:
            valores = linha.split(',')
            if(len(valores) is not 3):
                raise ValueError('Uma linha no arquivo %s deve ter 3 valores' % nome_arquivo)
            perfis.append(classe(*valores))
        arquivo.close()
        return perfis

    def imprimir(self):
        print 'Nome: %s, Telefone: %s, Empresa: %s' % (self.nome, self.telefone, self.empresa)

class Perfil_Vip(Perfil):
    'Classe para padrão de perfis de usuários VIPs'

    def __init__(self, nome, telefone, empresa, apelido=''):
        super(Perfil_Vip, self).__init__(nome, telefone, empresa)
        self.apelido = apelido

    def obter_creditos(self):
        return super(Perfil_Vip, self).obter_curtidas() * 10.0
