import sender_stand_request
import data

#Función para cambiar el nombre del cuerpo de la solicitud
def get_kit_body(name):
    current_body = data.kit_body_template.copy()
    current_body["name"] = name
    return current_body

#Función para pruebas positivas
def positive_assert(kit_body, auth_token):
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

#Función para pruebas negativas
def negative_assert_code_400(kit_body, auth_token):
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

#Función para recibir el token para el nuevo usuario
def get_new_user_token():
    resp = sender_stand_request.post_new_user(data.user_body)
    assert resp.status_code == 201
    return resp.json()["authToken"]

"""----------------------------------------------Lista de comprobación-----------------------------------------------"""
#1. El número permitido de caracteres (1)
def test_kit_name_one_char():
    token = get_new_user_token()
    positive_assert(get_kit_body("a"), token)

#2. El número permitido de caracteres (511):
def test_kit_name_511_chars():
    token = get_new_user_token()
    positive_assert(get_kit_body(data.five_hundred_eleven_chars), token)

#3. El número de caracteres es menor que la cantidad permitida (0)
def test_kit_name_empty():
    token = get_new_user_token()
    negative_assert_code_400(get_kit_body(""), token)

#4. El número de caracteres es mayor que la cantidad permitida (512)
def test_kit_name_512_chars():
    token = get_new_user_token()
    negative_assert_code_400(get_kit_body(data.five_hundred_twelve_chars), token)

#5. Se permiten caracteres especiales
def test_kit_name_special_chars():
    token = get_new_user_token()
    positive_assert(get_kit_body("№%""@," ), token)

#6. Se permiten espacios
def test_kit_name_with_spaces():
    token = get_new_user_token()
    positive_assert(get_kit_body(" A Aaa "), token)

#7. Se permiten números
def test_kit_name_numbers():
    token = get_new_user_token()
    positive_assert(get_kit_body("123"), token)

#8. El parámetro no se pasa en la solicitud
def test_kit_name_not_param():
    token = get_new_user_token()
    negative_assert_code_400({}, token)

#9. Se ha pasado un tipo de parámetro diferente (número)
def test_kit_name_not_strings():
    token = get_new_user_token()
    negative_assert_code_400({"name": 123}, token)