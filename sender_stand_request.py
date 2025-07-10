import configuration
import requests
import data


def post_new_user(body):
    """Crea un nuevo usuario y devuelve la respuesta completa."""
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers=data.headers)

def post_new_client_kit(kit_body, auth_token):
    body = kit_body.copy()
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"

    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
        json=body,
        headers=headers)
