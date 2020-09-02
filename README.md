# Backend

## Installation

### Docker

- Build images:
```bash
docker-compose build
```

- Run migrations
```bash
docker-compose run web make migrate
```

- Load data into database
```bash
docker-compose run web make load_data
```

- Run services
```bash
docker-compose up -d
```

### Virtualenv

- Install [poetry](https://pip.pypa.io/en/stable/).

- Setup PostgreSQL database

- Install dependencies
```bash
poetry install
```

- Run migrations
```bash
make migrate
```

- Load data into database
```bash
make load_data
```

- Run development server
```bash
make run
```

## Running tests

### Docker

```bash
docker-compose run web make test
```

### Virtualenv

```bash
make test
```

## Running linters

### Docker

```bash
docker-compose run web make lint
```

### Virtualenv

```bash
make lint
```

## API

```bash
GET /books
```

| Query Param | Type | Description |
| :--- | :--- | :--- |
| `title` | `string` | Optional |
