## Endpoints

### Emprestimo

* ccb/emprestimos/
* ccb/emprestimos/<uuid>
* ccb/emprestimos/<uuid>/saldo_devedor

### Pagamentos
* ccb/pagamentos/
* ccb/pagamentos/<uuid>

### Autenticação
* Endpoint default do `rest_framework_simplejwt`: `api/token`

## Tests
* `$ python manage.py test`


## Execução

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
