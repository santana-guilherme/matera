## Endpoints

### Emprestimo

* ccb/emprestimos/
* ccb/emprestimos/`<uuid>`
* ccb/emprestimos/`<uuid>`/saldo_devedor

### Pagamentos
* ccb/pagamentos/
* ccb/pagamentos/`<uuid>`

### Autenticação
* Endpoint default do `rest_framework_simplejwt`: `api/token`

## Testes
* `$ python manage.py test`


## Execução
* Create a `local_settings.py` file under `matera` folder using the `local_settings.py-sample` as an example
* install uv: https://docs.astral.sh/uv/getting-started/installation/
* `$ uv sync`
* `$ source .venv/bin/activate`
* `$ python manage.py migrate`
* Load the data to the database: `$ python manage.py loaddata init_db_data.json`
* `$ python manage.py runserver`
* Get the non admin user token (or for admin user, username: `admin`, password: `pw`)
    ```bash
    curl --request POST \
    --url http://localhost:8000/api/token/ \
    --header 'content-type: application/json' \
    --data '{
    "username": "noadmin",
    "password": "changeMe123"
    }'
    ```
## Organização do projeto
* As funcionalidades pedidas foram implementadas no app ccb
```
ccb
├── README.md
├── __init__.py
├── admin.py
├── apps.py
├── migrations
├── models
│   ├── __init__.py
│   ├── emprestimo.py # As regras de negócio de saldo devedor foi implementada na model de emprestimo
│   └── pagamento.py
├── serializers
│   ├── __init__.py
│   ├── emprestimo.py
│   └── pagamento.py
├── tests
│   ├── __init__.py
│   ├── e2e
│   │   ├── __init__.py
│   │   └── test_emprestimo.py
├── urls.py
└── views
    ├── __init__.py
    ├── emprestimo.py
    └── pagamento.py
```