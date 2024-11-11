# Dízima Periódica para Fração

Este projeto implementa uma função em Python que converte uma dízima periódica em uma fração geratriz usando a biblioteca SymPy. A dízima periódica é fornecida como uma string e a função retorna a fração correspondente.

## Funcionalidades

- Converte dízimas periódicas mistas e simples em frações.
- Trata a parte inteira, a parte não repetitiva e a parte repetitiva da dízima.
- Utiliza a biblioteca SymPy para representar a fração resultante.

## Requisitos

- Python 3.x
- Biblioteca SymPy

## Instalação

1. **Clone o repositório:**
    ```sh
    git clone https://github.com/seu-usuario/repositorio.git
    cd repositorio
    ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
    ```sh
    python -m venv env
    source env/bin/activate  # No Windows, use `env\Scripts\activate`
    ```

3. **Instale a biblioteca SymPy:**
    ```sh
    pip install sympy
    ```

## Uso

1. **Execute o script `dizima_para_fracao.py`:**
    ```sh
    python dizima_para_fracao.py
    ```

2. **Digite a dízima periódica quando solicitado:**
    ```sh
    Digite a dízima periódica (ex: 0.2(2), 0.25(25), 0.7(9)): 
    ```

3. **Aguarde a conversão e a exibição da fração geratriz:**

### Exemplo

#### Entrada:
```plaintext
0.2(2)
```

#### Saída:
```plaintext
A fração geratriz de 0.2(2) é: 2/9
```

## Estrutura do Código

- **Importação e Definição da Função**:
    - Importa a função `Rational` da biblioteca SymPy.
    - Define a função `dizima_periodica_para_fracao(dizima)`.

- **Função `dizima_periodica_para_fracao`**:
    - Verifica se a entrada contém uma dízima periódica (parênteses).
    - Separa a parte inteira, a parte não repetitiva e a parte repetitiva da dízima.
    - Calcula a fração geratriz com base na presença ou ausência da parte não repetitiva.
    - Retorna a fração geratriz como um objeto `Rational`.

- **Execução do Script**:
    - Solicita ao usuário a entrada da dízima periódica.
    - Chama a função `dizima_periodica_para_fracao` e imprime o resultado.

## Contribuição

1. Faça um fork do repositório.
2. Crie um branch para sua feature (`git checkout -b feature/AmazingFeature`).
3. Commit suas alterações (`git commit -m 'Add some AmazingFeature'`).
4. Push para o branch (`git push origin feature/AmazingFeature`).
5. Abra um Pull Request.
