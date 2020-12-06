# -*- coding: utf -8 -*-
class Simplex:

    def __init__(self): 
        self.tabela = []


    def funcao_objetivo(self, funcao: list): 
        self.tabela.append(funcao)


    def adicionar_restricao(self, sa: list): 
        self.tabela.append(sa)


    def localizar_coluna_que_entra(self) -> int: 
        coluna_pivo = min(self.tabela[0])
        i = self.tabela[0].index(coluna_pivo)

        return i


    def localizar_linha_que_sai(self, coluna_pivo: int) -> int: 
        dados_da_divisao = {} 

        for linha in range(len(self.tabela)):
            if linha > 0:
                if self.tabela[linha][coluna_pivo] > 0:
                    divisao = self.tabela[linha][-1] / self.tabela[linha][coluna_pivo]
                    dados_da_divisao[linha] = divisao

        indice_linha_que_sai = min(dados_da_divisao, key=dados_da_divisao.get)

        return indice_linha_que_sai


    def calcular_linha_pivo(self, coluna_pivo: int, linha_que_sai: int) -> list:

        linha = self.tabela[linha_que_sai] 

        pivo = linha[coluna_pivo]

        nova_linha_pivo = [valor / pivo for valor in linha]

        return nova_linha_pivo


    def calcular_nova_linha(self, linha: list, coluna_pivo: int, linha_pivo: list) -> list:

        pivo = linha[coluna_pivo] * (-1) 

        linha_resultado = [valor * pivo for valor in linha_pivo]

        nova_linha = []

        for i in range(len(linha_resultado)):
            soma = linha_resultado[i] + linha[i]
            nova_linha.append(soma)

        return nova_linha


    def verifica_negativo(self) -> bool: 
        negativo = list(filter(lambda value: value < 0, self.tabela[0]))
        if len(negativo) > 0:
            return True
        return False


    def processar_tabela(self): 

        coluna_pivo = self.localizar_coluna_que_entra()

        linha_que_sai = self.localizar_linha_que_sai(coluna_pivo)

        nova_linha_pivo = self.calcular_linha_pivo(coluna_pivo, linha_que_sai)

        self.tabela[linha_que_sai] = nova_linha_pivo

        copia_tabela = self.tabela.copy()

        i = 0

        while i < len(self.tabela):
            if i != linha_que_sai:
                linha = copia_tabela[i]
                nova_linha = self.calcular_nova_linha(linha, coluna_pivo, nova_linha_pivo)
                self.tabela[i] = nova_linha
            i += 1


    def imprimir_tabela(self): 
        for i in range(len(self.tabela)):
            for j in range(len(self.tabela[0])):
                print(f"{self.tabela[i][j]}\t", end="")
            print()


    def solucionar(self):  

        self.processar_tabela()

        while self.verifica_negativo():
            self.processar_tabela()

        self.imprimir_tabela()


if __name__ == "__main__": 

    simplex = Simplex()
    simplex.funcao_objetivo([1, -100, -150, 0, 0, 0, 0])

    simplex.adicionar_restricao([0, 2, 3, 1, 0, 0, 120])
    simplex.adicionar_restricao([0, 1, 0, 0, 1, 0, 40])
    simplex.adicionar_restricao([0, 0, 1, 0, 0, 1, 30])

    simplex.solucionar()