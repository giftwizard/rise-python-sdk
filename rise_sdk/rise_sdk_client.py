"""
Rise SDK Client - Python wrapper for unified API access
"""
from typing import Optional, Dict, Any
from rise_sdk.api import (
    GiftCardApi,
    GiftCardOrderApi,
    OAuthApi,
    RecipientApi,
    TransactionApi,
    WalletApi,
    WalletActionApi,
    WorkflowsApi
)
from rise_sdk.configuration import Configuration
from rise_sdk.api_client import ApiClient


class RiseSDKClient:
    """
    Rise SDK Client - Simple unified interface for all Rise APIs
    
    Example with API Key Authentication:
        sdk = RiseSDKClient.with_api_key(
            token='IST.xxx.yyy.zzz',
            account_id='your-account-id'
        )
        gift_card = sdk.gift_cards.get_gift_card(gift_card_id='card-123')
    
    Example with OAuth Authentication:
        sdk = RiseSDKClient.with_oauth(
            client_id='your-app-id',
            client_secret='your-app-secret',
            instance_id='merchant-instance-id'
        )
        wallets = sdk.wallets.query_wallets(query={'filter': '...'})
    """
    
    def __init__(self, api_client: ApiClient):
        """
        Private constructor - use static factory methods instead
        
        Args:
            api_client: Configured API client instance
        """
        self._api_client = api_client
        
        # Initialize all API clients
        self.gift_cards = GiftCardApi(api_client)
        self.gift_card_orders = GiftCardOrderApi(api_client)
        self.oauth = OAuthApi(api_client)
        self.recipients = RecipientApi(api_client)
        self.transactions = TransactionApi(api_client)
        self.wallets = WalletApi(api_client)
        self.wallet_actions = WalletActionApi(api_client)
        self.workflows = WorkflowsApi(api_client)
    
    @classmethod
    def with_api_key(
        cls,
        token: str,
        account_id: str,
        base_path: str = 'https://platform.rise.ai'
    ) -> 'RiseSDKClient':
        """
        Create Rise SDK client with API Key authentication
        
        Args:
            token: Authentication token (API Key), e.g., 'IST.xxx.yyy.zzz'
            account_id: Rise account ID
            base_path: Base URL for the Rise API (default: 'https://platform.rise.ai')
        
        Returns:
            Configured Rise SDK client instance
        
        Example:
            sdk = RiseSDKClient.with_api_key(
                token='IST.xxx.yyy.zzz',
                account_id='your-account-id'
            )
        """
        configuration = Configuration(host=base_path)
        api_client = ApiClient(configuration)
        
        # Set authentication headers
        api_client.default_headers['Authorization'] = f'Bearer {token}'
        api_client.default_headers['rise-account-id'] = account_id
        
        return cls(api_client)
    
    @classmethod
    def with_oauth(
        cls,
        client_id: str,
        client_secret: str,
        instance_id: str,
        base_path: str = 'https://platform.rise.ai'
    ) -> 'RiseSDKClient':
        """
        Create Rise SDK client with OAuth authentication
        
        This method automatically fetches an OAuth access token using the provided credentials.
        The token is valid for 4 hours.
        
        Args:
            client_id: OAuth client ID (App ID)
            client_secret: OAuth client secret (App Secret Key)
            instance_id: OAuth instance ID (App Instance ID)
            base_path: Base URL for the Rise API (default: 'https://platform.rise.ai')
        
        Returns:
            Configured Rise SDK client instance
        
        Example:
            sdk = RiseSDKClient.with_oauth(
                client_id='your-app-id',
                client_secret='your-app-secret',
                instance_id='merchant-instance-id'
            )
        """
        # Create temporary configuration for OAuth token request
        temp_configuration = Configuration(host=base_path)
        temp_api_client = ApiClient(temp_configuration)
        oauth_api = OAuthApi(temp_api_client)
        
        # Fetch OAuth token
        token_response = oauth_api.some_operation(
            grant_type='client_credentials',
            client_id=client_id,
            client_secret=client_secret,
            instance_id=instance_id
        )
        
        # Create SDK with OAuth token
        configuration = Configuration(host=base_path)
        api_client = ApiClient(configuration)
        api_client.default_headers['Authorization'] = token_response.access_token
        
        return cls(api_client)
