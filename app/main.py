import os
import urllib.error
import urllib.request

REQUIRED_VARS = ("DATABASE_USER", "DATABASE_PASSWORD", "API_TOKEN")


def get_env(name: str) -> str | None:
    return os.getenv(name)


def validate_env() -> None:
    missing = [name for name in REQUIRED_VARS if not get_env(name)]
    if missing:
        raise SystemExit(
            f"Variáveis obrigatórias ausentes: {', '.join(missing)}"
        )


def simulate_db_connection() -> None:
    database_url = get_env("DATABASE_URL") or "postgresql://localhost:5432/securebank"
    database_user = get_env("DATABASE_USER")

    print(f"Conectando ao banco ({database_url}) como: {database_user}")
    print("Senha do banco carregada: ***")
    print("Conexão com banco simulada com sucesso.")


def simulate_api_call() -> None:
    api_token = get_env("API_TOKEN")
    jwt_secret = get_env("JWT_SECRET")

    print("Token da API carregado: ***")
    if jwt_secret:
        print("JWT_SECRET carregado: ***")

    request = urllib.request.Request(
        "https://httpbin.org/headers",
        headers={"Authorization": f"Bearer {api_token}"},
        method="GET",
    )

    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            print(f"Chamada à API externa simulada (status: {response.status}).")
    except urllib.error.URLError:
        print("Chamada à API externa simulada (rede indisponível, token não exposto).")


def main() -> None:
    print("Iniciando aplicação SecureBank Analytics...")
    validate_env()
    simulate_db_connection()
    simulate_api_call()
    print("Aplicação executada com sucesso.")


if __name__ == "__main__":
    main()
