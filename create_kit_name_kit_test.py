import sender_stand_request
import data


# создание тела набора
def get_kit_body(name):
    return {"name": name}


# получение Token пользователя
def get_user_token():
    return sender_stand_request.post_new_user(data.user_body).json()["authToken"]


# Позитивные проверки по валидции в названии набора
def positive_assert(name):
    kit_response = sender_stand_request.post_new_client_kit(get_user_token(), get_kit_body(name))

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name


# Позитивная проверка - допустимое количество символов (1)
def test_create_kit_name_1_letter_in_kit_body_get_success_response():
    positive_assert("a")


# Позитивная проверка - допустимое количество символов (511)
def test_create_kit_name_511_letter_in_kit_body_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# Позитивная проверка - разрешены английские буквы
def test_create_kit_name_english_letter_in_kit_body_get_success_response():
    positive_assert("QWErty")


# Позитивная проверка - разрешены русские буквы
def test_create_kit_name_russian_letter_in_kit_body_get_success_response():
    positive_assert("Мария")

# Позитивная проверка - разрешены спецсимволы
def test_create_kit_name_has_special_symbol_in_kit_body_get_success_response():
    positive_assert("\"№%@\",")


# Позитивная проверка - разрешены пробелы
def test_create_kit_name_has_space_in_kit_body_get_success_response():
    positive_assert("Человек и Ко")


# Позитивная проверка - разрешены цифры
def test_create_kit_name_has_number_in_kit_body_get_success_response():
    positive_assert("123")


# Негативные проверки по валидации в названии набора
def negative_assert_kit(body):
    response = sender_stand_request.post_new_client_kit(get_user_token(), body)
    assert response.status_code == 400
    assert response.json()["code"] == 400


def negative_assert_kit_name(name):
    negative_assert_kit(get_kit_body(name))


# Негативные проверки - количество символов меньше допустимого (0)
def test_create_kit_name_0_get_error_response():
    negative_assert_kit_name("")


# Негативные проверки - количество символов больше допустимого (512)
def test_create_kit_name_512_letter_in_get_error_response():
    negative_assert_kit_name("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


# Негативные проверки - параметр не передан в запрос
def test_create_kit_no_name_in_get_error_response():
    negative_assert_kit({})


# Негативные проверки - передан другой тип параметра
def test_create_kit_name_number_in_get_error_response():
    negative_assert_kit_name(123)
