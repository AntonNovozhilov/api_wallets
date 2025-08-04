BASE_URL = "/wallets"


def test_get_all_wallets_as_superuser(client_with_superuser):
    response = client_with_superuser.get(BASE_URL)
    assert (
        response.status_code == 200
    ), f"Доступ к {BASE_URL} должен быть только у администратора."


def test_get_all_wallets_as_user(test_client):
    response = test_client.get(BASE_URL)
    assert (
        response.status_code == 403
    ), f"Доступ к {BASE_URL} должен быть только у администратора."


def test_get_wallet_by_owner(test_client, test_wallet):
    response = test_client.get(f"{BASE_URL}/{test_wallet.id}")
    assert (
        response.status_code == 200
    ), f'Доступ к "{BASE_URL}/{test_wallet.id}" должен быть только у владельца кошелька.'
    data = response.json()
    assert data["id"] == test_wallet.id
    assert data["balance"] == test_wallet.balance


def test_get_wallet_not_owner(client_with_superuser, test_wallet):
    response = client_with_superuser.get(f"{BASE_URL}/{test_wallet.id}")
    assert (
        response.status_code == 403
    ), f'Доступ к "{BASE_URL}/{test_wallet.id}" должен быть только у владельца кошелька.'


def test_deposit_to_wallet(test_client, test_wallet):
    payload = {"operation_type": "DEPOSIT", "amount": 100.0}
    response = test_client.post(
        f"{BASE_URL}/{test_wallet.id}/operation", json=payload
    )
    assert response.status_code == 200
    data = response.json()
    assert data["balance"] == test_wallet.balance + 100


def test_withdraw_from_wallet(test_client, test_wallet):
    payload = {"operation_type": "WITHDRAW", "amount": 200.0}
    response = test_client.post(
        f"{BASE_URL}/{test_wallet.id}/operation", json=payload
    )
    assert (
        response.status_code == 200
    ), f'Операция {payload["operation_type"]} должна быть доступна только владельцу.'
    data = response.json()
    assert data["balance"] == test_wallet.balance - 200


def test_withdraw_more_than_balance(test_client, test_wallet):
    payload = {
        "operation_type": "WITHDRAW",
        "amount": test_wallet.balance + 1000.0,
    }
    response = test_client.post(
        f"{BASE_URL}/{test_wallet.id}/operation", json=payload
    )
    assert response.status_code == 400
