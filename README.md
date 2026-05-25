# 📊 Lambda Bedrock Analytics

![Python Version](https://img.shields.io/badge/python-3.11%2B-blue?logo=python)
![Firebase Functions](https://img.shields.io/badge/Firebase_Functions-0.5%2B-FFCA28?logo=firebase)
![AWS Bedrock](https://img.shields.io/badge/AWS_Bedrock-Generative_AI-FF9900?logo=amazonaws)
![Architecture](https://img.shields.io/badge/Architecture-Serverless-orange)
![License](https://img.shields.io/badge/license-MIT-green)

> **Aplicação serverless de análise estatística**
>
> Exposta como uma Firebase Cloud Function, a API recebe amostras numéricas, calcula automaticamente a tabela de distribuição de frequências. Desenvolvida para a disciplina de **Estatística Aplicada** da FATEC Carapicuíba.

---

## 📋 Sumário

- [Sobre o Projeto](#-sobre-o-projeto)
- [Arquitetura](#-arquitetura)
- [O que é calculado](#-o-que-é-calculado)
- [Tech Stack](#-tech-stack)
- [Como Executar](#-como-executar)
- [Estrutura do Projeto](#-estrutura-do-projeto)

---

## 💡 Sobre o Projeto

O **Lambda Bedrock Analytics** é uma Cloud Function que recebe um conjunto de amostras numéricas e devolve uma análise estatística completa. O serviço calcula a tabela de distribuição de frequências, média, variância e desvio padrão — tudo de forma automática.

---

## 🏗 Arquitetura

```
Cliente HTTP
    │
    ▼
Firebase Cloud Function (main.py)
    │
    ├── ValidateInputPipe
    │       └── Valida o JSON recebido e extrai as amostras
    │
    ├── Controller
    │       └── Orquestra o fluxo e repassa para o service
    │
    ├── DistruibuitionProcessService
    │       ├── Ordena as amostras
    │       ├── Calcula número de classes (Regra de Sturges)
    │       ├── Calcula amplitude dos intervalos
    │       ├── Monta a tabela de distribuição de frequências
    │       └── Calcula média, variância e desvio padrão
    │
    └── ErrorHandler
            ├── BodyNullException       → 400 Bad Request
            └── InputValidationException → 400 Bad Request
```

---

## 📐 O que é Calculado

Para cada conjunto de amostras enviado, o `DistruibuitionProcessService` produz:

| Métrica | Descrição |
| :--- | :--- |
| **Número de classes (k)** | Calculado pela Regra de Sturges: `k = 1 + 3.3 * log10(n)` |
| **Amplitude (ai)** | `(max - min) / k`, arredondado para baixo |
| **fi** | Frequência absoluta por classe |
| **Fi** | Frequência acumulada absoluta |
| **xi** | Ponto médio do intervalo de classe |
| **fi·xi** | Produto da frequência pelo ponto médio |
| **fi·xi²** | Produto da frequência pelo quadrado do ponto médio |
| **fri** | Frequência relativa (`fi / n`) |
| **pi** | Frequência percentual (`fri * 100`) |
| **Média** | `Σ(fi·xi) / n` |
| **Variância** | `Σ(fi·xi²) / n - média²` |
| **Desvio Padrão** | `√variância` |

---

## 🚀 Tech Stack

- **Linguagem:** Python 3.11+
- **Serverless:** Firebase Cloud Functions (`firebase_functions`)
- **Framework HTTP:** Flask 3.1+
- **Deploy:** Firebase CLI
- **Servidor local:** Gunicorn + Uvicorn

---

## ⚡ Como Executar

### Pré-requisitos

- Python 3.11+
- [Firebase CLI](https://firebase.google.com/docs/cli) instalado
- Projeto Firebase criado

### Passo a Passo

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/Gusales/lambda-bedrock-analytcs.git
    cd lambda-bedrock-analytcs
    ```

2. **Crie e ative o ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```

3. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure o Firebase:**
    ```bash
    cp .firebaserc.example .firebaserc
    # Edite .firebaserc com o ID do seu projeto Firebase
    ```

5. **Execute localmente:**
    ```bash
    firebase emulators:start --only functions
    ```

    Ou diretamente com o Functions Framework:
    ```bash
    functions-framework --target=lambda_handler --debug
    ```

### Exemplo de requisição

```bash
curl -X POST http://localhost:8080 \
  -H "Content-Type: application/json" \
  -d '{"samples": [12, 45, 23, 67, 34, 89, 55, 41, 28, 76]}'
```

**Resposta esperada:**
```json
{
  "data": {
    "classes": 4,
    "amplitude": 19,
    "media": 47.0,
    "variance": 532.75,
    "standard_deviation": 23.08,
    "table": [
      { "i": 1, "class": "12 -> 31", "fi": 3, "Fi": 3, "xi": 21.5, "fri": 0.3, "pi": 30.0 },
      "..."
    ]
  }
}
```

---

## 📁 Estrutura do Projeto

```
lambda-bedrock-analytcs/
├── main.py                                          # Entrypoint da Cloud Function
├── requirements.txt                                 # Dependências Python
├── firebase.json                                    # Configuração do Firebase
├── .firebaserc.example                              # Exemplo de config do projeto Firebase
├── controllers/
│   └── lambda_controller.py                        # Orquestra o fluxo de negócio
├── services/
│   └── distribuition_process_service/
│       └── distribuition_process_service.py        # Cálculos estatísticos + integração Bedrock
├── validators/
│   └── validate_input_pipe.py                      # Validação e transformação do input
└── errors/
    ├── body_null_exception.py                      # Exceção para body ausente
    └── input_validation_exception.py               # Exceção para input inválido
```

---

## 🎓 Contexto Acadêmico

Projeto desenvolvido para a disciplina de **Estatística Aplicada** da [FATEC Carapicuíba](https://www.fateccarapicuiba.edu.br/), com o objetivo de aplicar na prática os conceitos de distribuição de frequências, medidas de tendência central e dispersão, utilizando IA generativa em uma arquitetura serverless moderna.
