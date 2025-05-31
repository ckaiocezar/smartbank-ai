def main():
    print(\"Teste de funcionamento do SmartBank AI:\")
    saldo = 1000.0
    saque = 200.0
    saldo -= saque
    print(f\"Saldo inicial: R$ 1000.00\")
    print(f\"Saque efetuado: R$ {saque:.2f}\")
    print(f\"Saldo atual: R$ {saldo:.2f}\")

if __name__ == \"__main__\":
    main()
