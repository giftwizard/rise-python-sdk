# Rise Python SDK

The Rise Python SDK provides convenient access to the Rise Platform API from Python applications.

## Installation

```bash
pip install rise-python-sdk
```

## Reference

A full API reference for this library is available [here](./reference.md).

## Usage

The SDK supports two authentication methods: API Key and OAuth.

### API Key Authentication

```python
from rise_sdk.rise_sdk_client import RiseSDKClient

sdk = RiseSDKClient.with_api_key(
    token='IST.xxx.yyy.zzz',
    account_id='your-account-id'
)

# Use the SDK
gift_card = sdk.gift_cards.get_gift_card(gift_card_id='card-123')
print(gift_card)
```

### OAuth Authentication

```python
from rise_sdk.rise_sdk_client import RiseSDKClient

sdk = RiseSDKClient.with_oauth(
    client_id='your-app-id',
    client_secret='your-app-secret',
    instance_id='merchant-instance-id'
)

# Use the SDK
wallets = sdk.wallets.query_wallets(
    query={'filter': '{"email": "customer@example.com"}'}
)
print(wallets)
```

## API Overview

The SDK provides access to the following APIs:

### Gift Cards

Manage gift cards, including creating, updating, and querying gift cards.

```python
# Create a gift card
new_card = sdk.gift_cards.create_gift_card(
    gift_card={'initial_value': 10000, 'currency': 'USD'}
)

# Get a gift card
card = sdk.gift_cards.get_gift_card(gift_card_id='card-123')

# Query gift cards
cards = sdk.gift_cards.query_gift_cards(
    query={'filter': '{"status": "active"}'}
)
```

### Wallets

Manage customer wallets and their associated gift cards.

```python
# Create or get a wallet
wallet = sdk.wallets.get_or_create_wallet(
    customer_reference={'email': 'customer@example.com'}
)

# Query wallets
wallets = sdk.wallets.query_wallets(
    query={'filter': '{"balance": {"$gt": 0}}'}
)
```

### Wallet Actions

Manage wallet actions such as issuing store credit, rewards, and refunds.

```python
# Create a wallet action
action = sdk.wallet_actions.create_wallet_action(
    wallet_action={
        'wallet_id': 'wallet-123',
        'type': 'STORE_CREDIT',
        'amount': 5000,
        'reason': 'Customer appreciation'
    }
)

# Query wallet actions
actions = sdk.wallet_actions.query_wallet_actions(
    query={'filter': '{"wallet_id": "wallet-123"}'}
)
```

### Orders

Manage gift card orders.

```python
# Create an order
order = sdk.gift_card_orders.create_order(
    order={'line_items': [{'gift_card': {'initial_value': 5000, 'currency': 'USD'}}]}
)

# Fulfill an order
fulfilled = sdk.gift_card_orders.fulfill_order(order_id='order-123')
```

### Recipients

Manage gift card recipients.

```python
# Create a recipient
recipient = sdk.recipients.create_recipient(
    recipient={'email': 'recipient@example.com', 'name': 'John Doe'}
)

# Query recipients
recipients = sdk.recipients.query_recipients(
    query={'filter': '{"email": "recipient@example.com"}'}
)
```

### Transactions

Query transaction history.

```python
# Query transactions
transactions = sdk.transactions.query_transactions(
    query={'filter': '{"gift_card_id": "card-123"}'}
)
```
