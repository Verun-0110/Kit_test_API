import sender_stand_request
import data


def get_kit_body(name):
    return {"name": name}


def get_user_token():
    return sender_stand_request.post_new_user(data.user_body).json()["authToken"]


def positive_assert(name):
    kit_response = sender_stand_request.post_new_client_kit(get_user_token(), get_kit_body(name))

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name


def test_create_kit_name_1_letter_in_kit_body_get_success_response():
    positive_assert("a")


def test_create_kit_name_511_letter_in_kit_body_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


def test_create_kit_name_english_letter_in_kit_body_get_success_response():
    positive_assert("QWErty")


def test_create_kit_name_russian_letter_in_kit_body_get_success_response():
    positive_assert("Мария")


def test_create_kit_name_has_special_symbol_in_kit_body_get_success_response():
    positive_assert("\"№%@\",")


def test_create_kit_name_has_space_in_kit_body_get_success_response():
    positive_assert("Человек и Ко")


def test_create_kit_name_has_number_in_kit_body_get_success_response():
    positive_assert("123")


def negative_assert_kit_name(name):
    response = sender_stand_request.post_new_client_kit(get_user_token(), get_kit_body(name))
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Не все необходимые параметры были переданы"


def test_create_kit_name_0_get_error_response():
    negative_assert_kit_name("")


def test_create_kit_name_512_letter_in_get_error_response():
    negative_assert_kit_name("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


def test_create_kit_no_name_in_get_error_response():
    negative_assert_kit_name()


def test_create_kit_name_number_in_get_error_response():
    negative_assert_kit_name(123)


test_create_kit_name_1_letter_in_kit_body_get_success_response()
test_create_kit_name_511_letter_in_kit_body_get_success_response()
test_create_kit_name_english_letter_in_kit_body_get_success_response()
test_create_kit_name_russian_letter_in_kit_body_get_success_response()
test_create_kit_name_has_special_symbol_in_kit_body_get_success_response()
test_create_kit_name_has_space_in_kit_body_get_success_response()
test_create_kit_name_has_number_in_kit_body_get_success_response()
test_create_kit_name_0_get_error_response()
test_create_kit_name_512_letter_in_get_error_response()
test_create_kit_no_name_in_get_error_response()
test_create_kit_name_number_in_get_error_response()
