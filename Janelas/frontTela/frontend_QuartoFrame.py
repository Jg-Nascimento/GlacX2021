from Janelas.estiloWidgets.widgets_Glac import LabelGlac
from Janelas.estiloWidgets.widgets_Glac import Entry
from Janelas.estiloWidgets.widgets_Glac import ButtonGlac
from tkinter import Button


class QuartoFrame:
    def quarto_frame(self):
        # Tecnico de reparo
        lbTecnico = LabelGlac(self.top4, 'Tecnico')
        lbTecnico.place(relx=0.02, rely=0.2, relwidth=0.13, relheight=0.3)

        self.entradaTecnico = Entry(self.top4)
        self.entradaTecnico.place(relx=0.02, rely=0.5, relwidth=0.13, relheight=0.3)

        botaotec = Button(self.top4, command=self.busca_tecnico)
        botaotec.configure(text=u'\u23EB', bg='#385679', fg='#4DA5FF', font=('Arial', '16', 'bold'),
            activebackground='#6495ED', activeforeground="lightgray")
        botaotec.place(relx=0.15, rely=0.5, relwidth=0.03, relheight=0.3)

        # label e listbox do numero do orcamento
        lbOrc = LabelGlac(self.top4, 'O.S')
        lbOrc.place(relx=0.33, rely=0.3, relwidth=0.04, relheight=0.4)
        self.listaNumOrc = Entry(self.top4)
        self.listaNumOrc.place(relx=0.37, rely=0.3, relwidth=0.06, relheight=0.4)

        #  Botao Gravar
        msg = 'Inicie uma nova Ordem de Serviço ou Orçamento no Botão Gravar'
        botaoAbreOrc = ButtonGlac(self.top4, 'Gravar', self.abre_orc, msg)
        botaoAbreOrc.place(relx=0.44, rely=0.2, width=63, relheight=0.6)
        #  Botao Buscar
        msg = 'Busque uma Ordem de Serviço ou Orçamento no Botão Buscar'
        botaoCarregaOrc = ButtonGlac(self.top4, 'Buscar', self.busca_orc, msg)
        botaoCarregaOrc.place(relx=0.51, rely=0.2, width=63, relheight=0.6)
        # Botao Alterar
        botaoAlteraOrc = ButtonGlac(self.top4, "Alterar", self.altera_orc)
        botaoAlteraOrc.place(relx=0.58, rely=0.2, width=63, relheight=0.6)
        ###  Botao Imprimir Orçamento
        botaoImprimirOrc = ButtonGlac(self.top4, "", self.imprime_orc)
        botaoImprimirOrc.configure(image=self.button_imprime2)
        botaoImprimirOrc.place(relx=0.92, rely=0.15, relwidth=0.06, relheight=0.7)

        #  Entrada Total
        self.entradatotal = Entry(self.top4)
        self.entradatotal.place(relx=0.856, rely=0.3, relwidth=0.06, relheight=0.4)
        self.entradatotal2 = Entry(self.top4)

        ## Botao Total
        descrtotal = ButtonGlac(self.top4, "Total R$", self.total_orc)
        descrtotal.place(relx=0.78, rely=0.2, width=70, relheight=0.6)
