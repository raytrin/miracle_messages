# ✨ Miracle Messages ✨

> 💌 Uma automação espiritual que vai alimentar a sua alma todos os dias! 
> 💌 Envia e-mail com uma frase aleatória do livro *Um Curso em Milagres*, para te lembrar do que realmente importa.
> 💌 Criado com Python, amor e fé.

---

## 📧 Como Funciona

O sistema roda automaticamente todos os dias e:

1. **Seleciona uma mensagem aleatória** do arquivo `mensagem.txt`
2. **Formata o email** com emojis e layout personalizado
3. **Envia por email** usando SMTP do Gmail
4. **Trata erros** para garantir funcionamento contínuo

**Exemplo de email enviado:**
```
Assunto: ✨ Miracle Messages! ✨

⭐ Mensagem do dia ⭐

"Entrego o futuro nas Mãos de Deus."

 - Um Curso em Milagres
```

---

## 🚀 Rodando localmente

1. **Configure as credenciais** no arquivo `dados.py`:
```python
meu_email = "seu_email@gmail.com"
password = "sua_senha_de_app"  # Use senha de aplicativo do Gmail
```

2. **Execute o programa**:
```bash
python main.py
```

## ☁️ **Rodando na nuvem**:

O projeto está automatizado na plataforma [PythonAnywhere](https://www.pythonanywhere.com/), executando todos os dias automaticamente.
Para automação diária, configure um cron job ou use PythonAnywhere.

---

## 📁 Estrutura do Projeto

```
├── main.py                      # Arquivo principal que executa o envio
├── dados.py                     # Credenciais de email (não incluído no repositório)
├── mensagem.txt                 # Arquivo com todas as mensagens do livro
└── README.md                    # Este arquivo
```

---

## 🛠️ Funcionalidades

- **Seleção aleatória** de frases do livro
- **Envio automático** por email via SMTP
- **Tratamento de erros** para arquivos e conexão
- **Deploy em produção** (PythonAnywhere)

---

## 🧰 Tecnologias

- **Python 3.x**
- **smtplib** (envio de emails)
- **email.message** (formatação de emails)
- **random** (seleção aleatória)
- **PythonAnywhere** (deploy e automação)

---

## 🔧 Configuração do Gmail

Para usar o Gmail SMTP, você precisa:

1. Ativar a **verificação em duas etapas**
2. Gerar uma **senha de aplicativo** específica
3. Usar essa senha no arquivo `dados.py`

---

## 💡 Motivação

Durante um momento difícil da minha vida, o livro Um Curso em Milagres me trouxe consolo e paz.
Decidi criar esse projeto para receber uma mensagem todos os dias no meu e-mail e manter a minha conexão com a minha fé.

--- 

## ⭐ Gratidão
Agradeço profundamente ao Amor e ao aprendizado que me inspirou a criar esse projeto.
Ele é um pedacinho do que eu acredito: a tecnologia pode ser gentil e significativa.
