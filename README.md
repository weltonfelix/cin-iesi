# Confirmação de Consultas por Mensagem

Este projeto tem como objetivo enviar mensagens de confirmação de consultas médicas para pacientes utilizando a API do TISaúde e mensagens via SMS ou WhatsApp. Ele é desenvolvido em Python e utiliza bibliotecas como `requests` para fazer requisições HTTP.

## Configuração do Ambiente

Para configurar o ambiente, siga os passos abaixo:

1. Clone este repositório para sua máquina local.
2. Crie um ambiente virtual Python:

   ```bash
   python -m venv venv
   ```

3. Ative o ambiente virtual:
   - No Windows:

     ```bash
     venv\Scripts\activate
     ```

   - No macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

5. Crie um arquivo `.env` na raiz do projeto e configure as variáveis de ambiente conforme o exemplo fornecido no arquivo `.env.example`.

## Uso

Para executar o script de confirmação de consultas, utilize o seguinte comando:

```bash
python main.py
```

## Contribuição

Ao instalar novas dependências, lembre-se de atualizar o arquivo `requirements.txt` utilizando:

```bash
pip freeze > requirements.txt
```

## Licença

Este projeto está licenciado sob a Licença Apache 2.0. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
