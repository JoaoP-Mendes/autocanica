from banco import conexao
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QMainWindow

widget = None
tela_login = 0

S = ["", "_2", "_3", "_4", "_5", "_6", "_7", "_8", "_9"]



class ListaBase(QDialog):
    CAMPOS = []
    BOTOES = ["alterarbotao", "excluirbotao"]
    TABELA = ""
    UI = ""
    SQL = ""

    def __init__(self):
        super().__init__()
        loadUi(self.UI, self)
        self.ids = []
        for i, s in enumerate(S):
            getattr(self, f"excluirbotao{s}").clicked.connect(lambda _, x=i: self.excluir(x))
        self.refreshbotao.clicked.connect(self.carregar)
        self.carregar()

    def _toggle(self, show, s):
        for n in self.CAMPOS + self.BOTOES:
            w = getattr(self, f"{n}{s}")
            w.show() if show else w.hide()

    def carregar(self):
        [self._toggle(False, s) for s in S]
        self.ids = []
        cursor = conexao.cursor()
        cursor.execute(self.SQL)
        for i, row in enumerate(cursor.fetchall()):
            self.ids.append(row[0])
            s = S[i]
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



class Login(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("telas/login.ui", self)
        self.entrarbotao.clicked.connect(self.loginfunction)

    def loginfunction(self):
        email, senha = self.email.text(), self.senha.text()
        if not email or not senha:
            return
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM adm WHERE email = %s AND senha = %s", (email, senha))
        resultado = cursor.fetchone()
        cursor.close()
        self.email.clear()
        self.senha.clear()
        if resultado:
            global widget
            widget.addWidget(Inicio())
            widget.setCurrentIndex(widget.currentIndex() + 1)




class Inicio(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("telas/inicio.ui", self)
        self.sairdaconta.clicked.connect(lambda: widget.setCurrentIndex(tela_login))
        self.clientesbotao.clicked.connect(lambda: self._ir(Clientes))
        self.carrosbotao.clicked.connect(lambda: self._ir(Carros))
        self.servicobotao.clicked.connect(lambda: self._ir(Servicos))
        self.osbotao.clicked.connect(lambda: self._ir(Ordemservico))

    def _ir(self, tela_cls):
        global widget
        widget.addWidget(tela_cls())


class Servicos(ListaBase):
    CAMPOS = ["servico", "categoria", "preco", "tempo", "status"]
    TABELA = "servicos"
    UI = "telas/servicos.ui"
    SQL = "SELECT id, nome, categoria, preco, tempo_estimado, status FROM servicos LIMIT 9"

    def __init__(self):
        super().__init__()
        self.novoclientebotao.clicked.connect(lambda: self.ir(Novoservico))
        self.novoclientebotao_8.clicked.connect(lambda: widget.setCurrentIndex(tela_login + 1))
        self.novoclientebotao_7.clicked.connect(lambda: self.ir(Clientes))
        self.novoclientebotao_6.clicked.connect(lambda: self.ir(Carros))
        self.novoclientebotao_5.clicked.connect(lambda: self.ir(Ordemservico))


class Novoservico(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("telas/novoservico.ui", self)
        self.salvarbotao.clicked.connect(self.salvar)
        self.cancelarbotao.clicked.connect(lambda: widget.setCurrentIndex(widget.currentIndex() - 1))

    def salvar(self):
        nome      = self.nomeservico.text()
        categoria = self.categoriaservico.currentText()
        descricao = self.descricaoservico.text()
        status    = self.ativosn.currentText()
        preco     = self.precoservico.text()
        tempo     = self.temposervico.text()
        if not nome or not preco:
            return
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO servicos (nome, categoria, descricao, status, preco, tempo_estimado) VALUES (%s,%s,%s,%s,%s,%s)",
            (nome, categoria, descricao, status, preco, tempo)
        )
        conexao.commit()
        cursor.close()
        widget.setCurrentIndex(widget.currentIndex() - 1)

class Ordemservico(ListaBase):
    CAMPOS = ["nomecliente", "nomecarro", "placaveiculo", "valortotal", "status"]
    TABELA = "ordemservico"
    UI = "telas/ordemservico.ui"
    SQL = "SELECT id, cpf_cliente, placa_veiculo, placa_veiculo, valor_total, status FROM ordemservico LIMIT 9"

    def __init__(self):
        super().__init__()
        self.novoclientebotao.clicked.connect(lambda: self.ir(Novaordemservico))
        self.novoclientebotao_8.clicked.connect(lambda: widget.setCurrentIndex(tela_login + 1))
        self.novoclientebotao_7.clicked.connect(lambda: self.ir(Clientes))
        self.novoclientebotao_6.clicked.connect(lambda: self.ir(Carros))
        self.novoclientebotao_5.clicked.connect(lambda: self.ir(Servicos))

class Novaordemservico(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("telas/novaordemservico.ui", self)
        self.salvarbotao.clicked.connect(self.salvar)
        self.cancelarbotao.clicked.connect(lambda: widget.setCurrentIndex(widget.currentIndex() - 1))

    def salvar(self):
        cpf        = self.cpfcliente.text()
        placa      = self.placaveiculo.text()
        problema   = self.descricaoservico.text()
        servicos   = self.descricaoservico_2.text()
        dataentrada = self.dataentrada.date().toString("yyyy-MM-dd")
        datasaida  = self.datasaida.date().toString("yyyy-MM-dd")
        status     = self.comboBox.currentText()
        if not cpf or not placa:
            return
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO ordemservico (cpf_cliente, placa_veiculo, problema_relatado, servicos, data_entrada, previsao_entrega, status) VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (cpf, placa, problema, servicos, dataentrada, datasaida, status)
        )
        conexao.commit()
        cursor.close()
        widget.setCurrentIndex(widget.currentIndex() - 1)

# ──────────────────────────────────────────────
from janelas_clientes import Clientes, Carros  # 