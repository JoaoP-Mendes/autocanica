from banco import conexao
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog

widget = None
S = ["", "_2", "_3", "_4", "_5", "_6", "_7", "_8", "_9"]


class ListaBase(QDialog):
    CAMPOS = []
    BOTOES = ["alterarbotao", "excluirbotao"]
    TABELA = ""
    UI = ""
    SQL = ""
    S_DISPONIVEIS = S

    def __init__(self):
        super().__init__()
        loadUi(self.UI, self)
        self.ids = []
        for i, s in enumerate(self.S_DISPONIVEIS):
            getattr(self, f"excluirbotao{s}").clicked.connect(lambda _, x=i: self.excluir(x))
        self.refreshbotao.clicked.connect(self.carregar)
        self.carregar()

    def _toggle(self, show, s):
        for n in self.CAMPOS + self.BOTOES:
            w = getattr(self, f"{n}{s}")
            w.show() if show else w.hide()

    def carregar(self):
        [self._toggle(False, s) for s in self.S_DISPONIVEIS]
        self.ids = []
        cursor = conexao.cursor()
        cursor.execute(self.SQL)
        for i, row in enumerate(cursor.fetchall()):
            self.ids.append(row[0])
            s = self.S_DISPONIVEIS[i]
            for j, campo in enumerate(self.CAMPOS):
                getattr(self, f"{campo}{s}").setText(str(row[j + 1]))
            self._toggle(True, s)
        cursor.close()

    def excluir(self, index):
        if index >= len(self.ids):
            return
        cursor = conexao.cursor()
        cursor.execute(f"DELETE FROM {self.TABELA} WHERE id = %s", (self.ids[index],))
        conexao.commit()
        cursor.close()
        self.carregar()

    def ir(self, tela_cls):
        global widget
        widget.addWidget(tela_cls())
        widget.setCurrentIndex(widget.currentIndex() + 1)





class Clientes(ListaBase):
    CAMPOS = ["nomecliente", "cpfcliente", "telefonecliente", "statuscliente"]
    BOTOES = ["alterarbotao", "excluirbotao"]
    TABELA = "clientes"
    UI = "telas/clientes.ui"
    SQL = "SELECT id, nome, cpf, telefone, status FROM clientes LIMIT 9"
    S_DISPONIVEIS = [""]

    def __init__(self):
        super().__init__()
        self.refreshbotao.clicked.connect(self.carregar)


        self.novoclientebotao.clicked.connect(lambda: self.ir(Novocliente))
        self.botaoirinicio.clicked.connect(lambda: widget.setCurrentIndex(self._ir_inicio()))
        self.botaoircarros.clicked.connect(lambda: self.ir(Carros))
        self.botaoirservicos.clicked.connect(lambda: self._ir_servicos("Servicos"))
        self.botaoiros.clicked.connect(lambda: self._ir_servicos("Ordemservico"))

    def _ir_inicio(self):
        from janelas import tela_login
        return tela_login + 1

    def _ir_servicos(self, nome):
        import janelas
        self.ir(getattr(janelas, nome))

    # def _ir_os(self):
    #     from janelas import Ordemservico
    #     self.ir(Ordemservico)


class Novocliente(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("telas/novocliente.ui", self)
        self.salvarbotao.clicked.connect(self.salvar)
        self.cancelarbotao.clicked.connect(lambda: widget.setCurrentIndex(widget.currentIndex() - 1))

    def salvar(self):
        nome = self.nome.text()
        cpf = self.cpf.text()

        if not nome or not cpf:
            return
        
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO clientes (nome, cpf, telefone, email, cep, cidade, status, observacoes) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
            (nome, cpf, self.telefone.text(), self.email.text(), self.cep.text(), self.cidade.text(), self.ativosn.currentText(), self.observacoes.text())
        )
        conexao.commit()
        cursor.close()
        widget.setCurrentIndex(widget.currentIndex() - 1)


class Carros(ListaBase):
    CAMPOS = ["carro", "placacarro", "anocarro", "statuscliente"]
    BOTOES = ["alterarbotao", "excluirbotao"]
    TABELA = "carros"
    UI = "telas/carros.ui"
    SQL = "SELECT id, marca, placa, ano, cpf_cliente FROM carros LIMIT 9"
    S_DISPONIVEIS = [""] 

    def __init__(self):
        super().__init__()

        #self.refreshbotao.clicked.connect(self.carregar)
        self.novocarrobotao.clicked.connect(lambda: self.ir(Novocarro))
        self.botaoirinicio.clicked.connect(lambda: widget.setCurrentIndex(self._ir_inicio()))
        self.botaoirclientes.clicked.connect(lambda: self.ir(Clientes))
        self.botaoirservicos.clicked.connect(lambda: self._ir_servicos("Servicos"))
        self.botaoiros.clicked.connect(lambda: self._ir_servicos("Ordemservico"))

    def _ir_inicio(self):
        from janelas import tela_login
        return tela_login + 1

    def _ir_servicos(self, nome):
        import janelas
        self.ir(getattr(janelas, nome))

    # def _ir_os(self):
    #     from janelas import Ordemservico
    #     self.ir(Ordemservico)


class Novocarro(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("telas/novocarro.ui", self)
        self.salvarbotao.clicked.connect(self.salvar)
        self.cancelarbotao.clicked.connect(lambda: widget.setCurrentIndex(widget.currentIndex() - 1))

    def salvar(self):
        cpf = self.cpfcliente.text() 
        placa = self.placacarro.text()

        if not cpf or not placa:
            return
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO carros (cpf_cliente, placa, marca, ano, modelo, cor, combustivel, km_atual, observacoes) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (cpf, placa, self.marcacarro.currentText(), self.anocarro.text(), self.modelocarro.text(), self.corcarro.text(), self.combustivelcarro.currentText(), self.kmatualcarro.text(), self.observacoes.text())
        )
        conexao.commit()
        cursor.close()
        widget.setCurrentIndex(widget.currentIndex() - 1)