from sympy import Rational


def dizima_periodica_para_fracao(dizima):
    # Verifica se a entrada é uma dízima periódica
    if '(' in dizima:
        # Separa a parte inteira, não repetitiva e repetitiva
        parte_inteira, parte_repetitiva = dizima.split('(')
        parte_repetitiva = parte_repetitiva.rstrip(')')
        parte_nao_repetitiva = parte_inteira.split('.')[-1] if '.' in parte_inteira else ''
        parte_inteira = parte_inteira.split('.')[0] if '.' in parte_inteira else parte_inteira

        parte_inteira = int(parte_inteira) if parte_inteira else 0
        parte_nao_repetitiva = parte_nao_repetitiva if parte_nao_repetitiva else ''

        # Cálculo para dízima periódica
        if parte_nao_repetitiva:
            n = len(parte_nao_repetitiva)
            m = len(parte_repetitiva)
            numerador = int(parte_inteira) * (10 ** (n + m)) + int(parte_nao_repetitiva + parte_repetitiva) - int(
                parte_inteira) * (10 ** n) - int(parte_nao_repetitiva)
            denominador = (10 ** (n + m)) - (10 ** n)
            return Rational(numerador, denominador)
        else:
            # Apenas dízima repetitiva
            m = len(parte_repetitiva)
            numerador = int(parte_inteira) * (10 ** m) + int(parte_repetitiva) - int(parte_inteira)
            denominador = (10 ** m) - 1
            return Rational(numerador, denominador)

    else:
        # Se não contém parênteses, trata como uma fração normal
        return Rational(dizima)


# Solicita a entrada do usuário
entrada = input("Digite a dízima periódica (ex: 0.2(2), 0.25(25), 0.7(9)): ")
resultado = dizima_periodica_para_fracao(entrada)

# Exibe o resultado
print(f"A fração geratriz de {entrada} é: {resultado}")
