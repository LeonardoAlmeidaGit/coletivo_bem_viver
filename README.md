# 🍲 Coletivo Bem Viver — Plataforma de Cozinhas Comunitárias

Plataforma web para gestão de cozinhas comunitárias, desenvolvida para apoiar a atuação da ONG **Coletivo Bem Viver** (Fortaleza/CE). O sistema permite que cada cozinha gerencie seu cardápio, avisos e informações, e ajuda a população a **encontrar as cozinhas mais próximas** por geolocalização.

> Projeto desenvolvido na disciplina de Projetos Experimentais do curso de Ciência da Computação, em parceria com a ONG.

---

## 🎯 Funcionalidades

- **Cadastro de cozinhas** com foto, endereço e **geolocalização automática** via Google Maps API
- **Mapa interativo** com todas as cozinhas e **busca por proximidade** a partir do endereço do usuário
- **Cardápios** por data, com itens e fotos
- **Avisos** de cada cozinha (ex.: fechamento, mudança de horário)
- **Avaliações** com estrelas (1 a 5) e comentário
- **Autenticação** de responsáveis, com **autorização a nível de objeto** (cada responsável só edita a própria cozinha)
- **Comando de gestão** customizado para geocodificar cozinhas em lote

---

## 🧱 Arquitetura e tecnologias

- **Back-end:** Python, Django 6 (Class-Based Views)
- **Banco de dados:** PostgreSQL
- **Integração externa:** Google Maps Geocoding API
- **Front-end:** Django Templates, Bootstrap
- **Infra:** Docker e Docker Compose

**Destaques técnicos:**
- Autorização a nível de objeto via `KitchenOwnerMixin`
- Modelo de usuário customizado (`AbstractUser`)
- Ordenação de cozinhas por distância geográfica
- Management command `geocode_kitchens` para preencher coordenadas faltantes

---

## 📁 Estrutura do projeto

```bash
.
├── app/          # Configurações do projeto (settings, urls, mixins, context processors)
├── api/          # Integração com a Google Maps API (geocoding)
├── kitchens/     # Cozinhas, geolocalização e mapa
├── menus/        # Cardápios e itens
├── notices/      # Avisos das cozinhas
├── reviews/      # Avaliações
├── users/        # Autenticação e usuário customizado
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## 📋 Pré-requisitos

- **Docker** e **Docker Compose** instalados
- Uma **chave da Google Maps API** com a *Geocoding API* e a *Maps JavaScript API* habilitadas

---

## 🚀 Como executar com Docker

**1. Clone o repositório**
```bash
git clone https://github.com/LeonardoAlmeidaGit/coletivo_bem_viver.git
cd coletivo_bem_viver
```

**2. Crie o arquivo `.env`** na raiz, com base no exemplo abaixo:
```env
SECRET_KEY=sua-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost, 127.0.0.1

GOOGLE_MAPS_API_KEY=sua-chave-do-google-maps

DB_ENGINE=django.db.backends.postgresql
DB_NAME=coletivo_bem_viver
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=coletivo_bem_viver_db
DB_PORT=5432
```
> `DB_HOST=coletivo_bem_viver_db` corresponde ao nome do serviço do banco no Docker Compose.

**3. Suba os containers**
```bash
docker compose up --build
```
As migrations são aplicadas automaticamente na inicialização. Acesse **http://localhost:8000**.

**4. Crie um superusuário** (em outro terminal)
```bash
docker compose exec coletivo_bem_viver_web python manage.py createsuperuser
```

**5. (Opcional) Geocodifique cozinhas sem coordenadas**
```bash
docker compose exec coletivo_bem_viver_web python manage.py geocode_kitchens
```

---

## 🔐 Segurança da chave do Google Maps

A chave da Maps JavaScript API é enviada ao navegador (necessário para renderizar o mapa no lado do cliente). Por isso, **restrinja a chave por referrer HTTP** no Google Cloud Console, permitindo apenas os seus domínios — assim ela não pode ser reutilizada por terceiros.

---

## 👨‍💻 Autor

Leonardo Almeida — [LinkedIn](https://www.linkedin.com/in/leonardo-almeida-dev/) · [GitHub](https://github.com/LeonardoAlmeidaGit)
