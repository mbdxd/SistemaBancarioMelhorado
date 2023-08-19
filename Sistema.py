class SistemaBancario:
    def __init__(self):
        self.saldo = 0.0
        self.depositos = []
        self.saque_limite_diario = 3
        self.saque_restante = self.saque_limite_diario

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and valor <= 500 and self.saque_restante > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                self.saque_restante -= 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para saque.")
        else:
            print("Valor inválido para saque ou limite diário de saques atingido.")

    def extrato(self):
        print("Extrato de transações:")
        for i, deposito in enumerate(self.depositos, start=1):
            print(f"Depósito {i}: R$ {deposito:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print(f"Saque(s) restante(s) hoje: {self.saque_restante}")


def main():
    sistema = SistemaBancario()

    while True:
        print("\n1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor a ser depositado: "))
            sistema.depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor a ser sacado: "))
            sistema.sacar(valor)
        elif opcao == '3':
            sistema.extrato()
        elif opcao == '4':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Escolha novamente.")


if __name__ == "__main__":
    main()