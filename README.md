# Composer CI/CD Dags
## Descrição
Este projeto automatiza o processo de implantação de DAGs do Cloud Composer usando pipelines de CI/CD. Ele envolve a criação de instâncias do Composer com Terraform, configuração de DAGs de exemplo e arquivos de teste, e configuração de jobs de CI/CD para ambientes de desenvolvimento e produção.

## Estrutura do Projeto

```bash
├── .github/workflows
│   ├── pipeline-composer-dags-dsv.yml
│   ├── pipeline-composer-dags-prd.yml
├── CreateComposerInstance
│   ├── main.tf
│   ├── variables.tf
├── dags
│   ├── dag.py
├── tests
│   ├── test.py
├── .gitignore
├── requirements.txt
├── requirements-test.txt
├── README.md
``````

## Requisitos

Certifique-se de ter os seguintes pré-requisitos instalados:

- [Terraform](https://www.terraform.io/)
- [Google Cloud SDK](https://cloud.google.com/sdk)
- [Python](https://www.python.org/)

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/yourusername/composer-ci-cd.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd composer-ci-cd
    ```

3. Crie e ative um ambiente virtual Python:
    - Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    - Windows:
         ```bash
        python3 -m venv venv
        .\venv\Scripts\activate
         ```
4. Instale os pacotes Python necessários:

    ```bash
    pip install -r requirements.txt
    pip install -r requirements-test.txt
    ```

Dessa forma, você terá um ambiente Python isolado para o projeto, evitando conflitos entre dependências de outros projetos.

## Uso

### Criação de Instância do Composer

1. Navegue até o diretório do Terraform:

    ```bash
    cd CreateComposerInstance-{env}
    ```

2. Crie e defina o arquivo `vars_{env}.tfvars` com os parâmetros a serem passados para o Terraform:

    ```tf
    work_environ                = "ambiente de execução"
    project_id                  = "id do seu projeto"
    region                      = "localização do seu projeto"
    image_version_composer      = "composer-2.4.4-airflow-2.5.3"
    composer_name               = "nome do composer"
    sa_composer_name            = "nome da Service Account que será utilizada pelo Composer"
    bucket_name_composer        = "Nome do bucket que será utilizado pelo Composer."
    ```

3. Execute `terraform init` para inicializar o ambiente Terraform.
4. Execute `terraform apply -var-file='vars_{environ}.tfvars'` para criar o Composer na GCP de acordo com o ambiente.

⚠️ Certifique-se de substituir `{env}` pela flag de ambiente que será executada.

### Criando Dags e Tests
Crie suas dags e seus arquivos de teste carregando as dags no diretório `dags/` e os testes em `tests/`.

#### Executando os Testes

Para executar os testes automatizados deste projeto, execute:

```bash
pytest -s tests/
```
Estes testes validam a funcionalidade das DAGs implantadas.

### Configurando CI/CD
Configure os jobs de CI/CD no GitHub Actions seguindo o exemplo dos arquivos `pipeline-composer-dags-dsv.yml` e `pipeline-composer-dags-prd.yml`. Esses arquivos fornecem um modelo para configurar os pipelines de integração contínua e entrega contínua para os ambientes de desenvolvimento e produção, respectivamente.

### Fluxo do CI/CD

1. **Pipeline de Desenvolvimento**: O pipeline de CI/CD para o ambiente de desenvolvimento é acionado por pushs na branch `develop`. Ele executa as seguintes etapas:
    - Executa testes automatizados nas DAGs.
    - Autentica no Google Cloud.
    - Configura o SDK do Google Cloud.
    - Faz o upload das DAGs para o Cloud Storage develop.

    ```yaml
    pipeline-composer-dags-dsv.yml
    ```

2. **Pipeline de Produção**: O pipeline de CI/CD para o ambiente de produção é acionado por pull requests na branch `main`. Ele executa as seguintes etapas:
    - Autentica no Google Cloud.
    - Configura o SDK do Google Cloud.
    - Faz o upload das DAGs para o Cloud Storage de produção.

    ```yaml
    pipeline-composer-dags-prd.yml
    ```

## Implantação

Siga estas etapas para implantar o projeto:

1. Crie uma instância de desenvolvimento do Composer usando o Terraform.
2. Crie uma instância de produção do Composer usando o Terraform.
3. Crie uma DAG de exemplo e um arquivo de teste.
4. Configure jobs de CI/CD para ambientes de desenvolvimento e produção.
5. Acione o pipeline CI/CD para cada ambiente conforme necessário.

## Links Úteis

- [Documentação do Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli)
- [Documentação do Google Cloud SDK](https://cloud.google.com/sdk)
- [Python](https://www.python.org/)
- [GitHub Actions](https://docs.github.com/pt/actions)
- [pytest](https://docs.pytest.org/en/7.0.x/)
- [Google Cloud Composer](https://cloud.google.com/composer)
