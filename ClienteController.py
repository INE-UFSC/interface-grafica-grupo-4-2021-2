from ClienteView import ClienteView
from Cliente import Cliente
import PySimpleGUI as sg 

class ClienteController:
    def __init__(self):
        self.__telaCliente = ClienteView(self)
        self.__clientes = {} #lista de objetos Cliente

    def inicia(self):
        self.__telaCliente.tela_consulta()
        
        # Loop de eventos
        rodando = True
        resultado = ''
        while rodando:
            event, values = self.__telaCliente.le_eventos()

            if event == sg.WIN_CLOSED:
                rodando = False
            elif event == 'Cadastrar':
                repetido = False
                for i in self.__clientes.keys():
                    if values['codigo'] == i:
                        repetido = True
                numero = self.__checar_numero(values['codigo'])
                if repetido:
                    resultado = 'Usuário já existe'
                elif not numero:
                    resultado = "Codigo deve ser um numero inteiro!"
                else:
                    resultado = 'Usuário cadastrado com sucesso'
                    self.adiciona_cliente(values['codigo'], values['nome'])

            elif event == 'Consultar':
                tem_cliente = False
                for i in self.__clientes.keys():
                    if values['codigo'] == i:
                        tem_cliente = True

                if tem_cliente:
                    cliente = self.__clientes[values['codigo']]
                    resultado = f'Nome: {cliente.nome}, Código: {cliente.codigo}'
                else:
                    resultado = "Não encontrado"
            
            if resultado != '':
                dados = str(resultado)
                self.__telaCliente.mostra_resultado(dados)

        self.__telaCliente.fim()


    def busca_codigo(self, codigo):
        try:
            return self.__clientes[codigo]
        except KeyError:
            raise KeyError

    # cria novo OBJ cliente e adiciona ao dict
    def adiciona_cliente(self, codigo, nome):
        self.__clientes[codigo] = Cliente(codigo, nome)
    
    def busca_nome(self, nome):
        for key, val in self.__clientes.items():
            if val.nome == nome:
                return key 

        raise LookupError

    @staticmethod
    def __checar_numero(numero):
        if numero.isdecimal():
            return True
        else:
            return False 
