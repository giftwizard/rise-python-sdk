# Rise Python SDK

[![PyPI version](https://badge.fury.io/py/rise-python-sdk.svg)](https://pypi.org/project/rise-python-sdk/)

The Rise Python SDK provides convenient access to the Rise Platform API from Python applications.

## Installation

```bash
pip install rise-python-sdk
```

## Prerequisites


Before using the Rise Python SDK, ensure you have the following:

#### Choosing an Authentication Method

- Use API keys for server-side applications and scripts that require direct access to your Rise account.
- Use OAuth for applications that need to integrate with multiple merchant accounts or require delegated access.


### Authentication


The SDK supports two authentication methods:

#### API Key Authentication
- **API Key** - A valid API key from your Rise account
- **Account ID** - Your Rise account identifier

#### OAuth Authentication
- **Client ID** - Your application's client ID (also known as App ID)
- **Client Secret** - Your application's client secret
- **Instance ID** - The merchant's instance ID (obtained during app installation)
- OAuth tokens are valid for 4 hours and automatically refresh
- Requires completing the [app installation flow](https://platform.rise.ai/docs#tag/Integrate-your-application-with-Rise/App-Installation-Flow/Step-2-or-Handle-installation-authentication-in-your-app)

For more information on OAuth authentication and the app installation flow, see the [Rise Platform Documentation](https://platform.rise.ai/docs#tag/Integrate-your-application-with-Rise/App-Installation-Flow/Step-2-or-Handle-installation-authentication-in-your-app).

## Reference

A full API reference for this library is available [here](./reference.md).

## Usage

### API Key Authentication

```python
from rise_sdk.rise_sdk_client import RiseSDKClient

sdk = RiseSDKClient.with_api_key(
    token='IST.xxx.yyy.zzz',
    account_id='your-account-id'
)
```

### OAuth Authentication

OAuth tokens are valid for 4 hours.

```python
from rise_sdk.rise_sdk_client import RiseSDKClient

sdk = RiseSDKClient.with_oauth(
    client_id='your-app-id',
    client_secret='your-app-secret',
    instance_id='instance-id'
)
```

## API Overview

The SDK provides access to the following APIs:


### Gift Cards

Manage gift cards, including creating, retrieving, and querying gift cards.

```python
new_card = sdk.gift_cards.create_gift_card(
    gift_card={
        'initial_value': '100',
        'source_info': {
            'type': 'MANUAL',
            'manual_options': {
                'note': 'new gift card'
            }
        }
    }
)

new_generated_giftcard_id = new_card.data.gift_card.id

new_generated_giftcard = sdk.gift_cards.get_gift_card(new_generated_giftcard_id)

cards = sdk.gift_cards.query_gift_cards(
    query={
        'cursor_paging': {
            'limit': 10
        }
    }
)
```

### Wallets

Manage customer wallets and their associated gift cards.

```python
wallet = sdk.wallets.get_or_create_wallet(
    customer_reference={
        'email': 'customer@example.com',
        'source_channel_id': 'channel-id',
        'source_tenant_id': 'tenant-id',
        'source_customer_id': 'customer-id'
    }
)

wallets = sdk.wallets.query_wallets(
    query={
        'paging': {
            'limit': 10
        }
    }
)
```

### Wallet Actions

Manage wallet actions such as issuing store credit, rewards, and refunds.

```python
action = sdk.wallet_actions.create_wallet_action(
    wallet_action={
        'wallet_id': 'wallet-id',
        'amount': '5000',
        'type': 'REWARD',
        'store_credit_context': {
            'source_channel_id': 'channel-id',
            'source_tenant_id': 'tenant-id'
        }
    }
)

actions = sdk.wallet_actions.query_wallet_actions(
    query={
        'paging': {
            'limit': 10
        }
    }
)
```

### Recipients

Manage gift card recipients.

```python
recipient = sdk.recipients.create_recipient(
    recipient={
        'email': 'recipient@example.com',
        'name': 'John Doe',
        'gift_card_id': 'giftcard-id'
    }
)

recipients = sdk.recipients.query_recipients(
    query={
        'cursor_paging': {
            'limit': 5
        }
    }
)
```

### Transactions

Query transaction history.

```python
transactions = sdk.transactions.query_transactions(
    query={
        'cursor_paging': {
            'limit': 5
        }
    }
)
```