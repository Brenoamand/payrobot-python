# coding: utf-8

"""
    Payrobot API Documentation & Reference

    # Introduction Accept, store, send or forward Bitcoin, Litecoin and Bitcoin Cash for your website or app and protect your privacy.  Supported crytocurrencies:   * BTC Bitcoin   * LTC Litecoin   * BCH Bitcoin Cash   ## Benefits    * **Anonymous** No personal details are required and transactions are mixed among all payments. You can forward your payments so as soon payrobot.io receives it forwards it to another address under your control.      * **No Registration** No registration, sign-up, application or form required to use payrobot.io      * **Easy Integration** Integrate your web / app through our simple RESTful API, you can accept payments with just one line of code!      * **Instant Payment Notification** Our servers notify your web / app the status of your payments. No polling, daemons or cronjobs required on your side!      * **Secure** Payrobot.io works with SSL and bank-level security protocols. Your transactions are safe!   ## Features **Payment Forward** Generate one-time addresses to recieve payments. Payrobot will notify your web /app through callbacks (webhooks) the status of the payment. As soon as it's confirmed the payment is forwarded to your desired address.  **Wallet** Receive, send payments and store your coins in a secure, private and anonymous wallet. All events are notified to your web / app through callbacks (webhooks). You can generate wallets with just one line of code without registration or further information  ## Fees **Only 0.90% per inbound transaction** (receive payments), NO HIDDEN FEES. All outbound transactions (send funds) are totally free.  Minimum fees applies, therefore the largest amount is going to be considered as fee either: `(inboundAmount*feePct)` or `the minimum fee`  **Inbound Fees (Receive payments)**    - `Bitcoin` 0.90% *(Minimum fee 0.00005 BTC)*   - `Litecoin` 0.90% *(Minimum fee 0.0005 LTC)*   - `Bitcoin Cash` 0.90% *(Minimum fee 0.0005 BCH)*     **Outbound Fees (Send funds)**    - `Bitcoin` 0.00%   - `Litecoin` 0.00%   - `Bitcoin Cash` 0.00%   ## Rate Limit To guarantee the good performance of the service and its fair use. The API is **limited to receiving 120 requests per minute per IP**, which is sufficient for most use cases.  Payrobot.io is asynchronous in most API methods to communicate with your application through callbacks (webhooks), thus reducing unnecessary calls to the service.  **If the limit is exceeded, the IP will be banned for 1 minute.**  If you require an upper limit for your application, do not hesitate to contact us  ## Considerations    * Amounts in responses are expresed as `strings`      * Wallets are not multi-currency, you have to create a different wallet per cryptocurrency (You can't store Litecoin in a Bitcoin wallet and vice-versa)      * Payment forwarding has to be of the same type of currency (You can't forward a Bitcoin Cash payment to a Bitcoin address and vice-versa)      # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: contact@payrobot.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from payrobot.configuration import Configuration


class WalletSendRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'currency': 'CryptoCurrency',
        'wallet_id': 'str',
        'request_id': 'str',
        'timestamp': 'int',
        'lastupdate': 'int',
        'amount': 'str',
        'callback': 'str',
        'destination': 'list[AddressDetail]',
        'txid': 'str',
        'status': 'int',
        'error': 'bool'
    }

    attribute_map = {
        'currency': 'currency',
        'wallet_id': 'walletId',
        'request_id': 'requestId',
        'timestamp': 'timestamp',
        'lastupdate': 'lastupdate',
        'amount': 'amount',
        'callback': 'callback',
        'destination': 'destination',
        'txid': 'txid',
        'status': 'status',
        'error': 'error'
    }

    def __init__(self, currency=None, wallet_id=None, request_id=None, timestamp=None, lastupdate=None, amount=None, callback=None, destination=None, txid=None, status=0, error=None, local_vars_configuration=None):  # noqa: E501
        """WalletSendRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._currency = None
        self._wallet_id = None
        self._request_id = None
        self._timestamp = None
        self._lastupdate = None
        self._amount = None
        self._callback = None
        self._destination = None
        self._txid = None
        self._status = None
        self._error = None
        self.discriminator = None

        if currency is not None:
            self.currency = currency
        if wallet_id is not None:
            self.wallet_id = wallet_id
        if request_id is not None:
            self.request_id = request_id
        if timestamp is not None:
            self.timestamp = timestamp
        if lastupdate is not None:
            self.lastupdate = lastupdate
        if amount is not None:
            self.amount = amount
        if callback is not None:
            self.callback = callback
        if destination is not None:
            self.destination = destination
        if txid is not None:
            self.txid = txid
        if status is not None:
            self.status = status
        if error is not None:
            self.error = error

    @property
    def currency(self):
        """Gets the currency of this WalletSendRequest.  # noqa: E501


        :return: The currency of this WalletSendRequest.  # noqa: E501
        :rtype: CryptoCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this WalletSendRequest.


        :param currency: The currency of this WalletSendRequest.  # noqa: E501
        :type: CryptoCurrency
        """

        self._currency = currency

    @property
    def wallet_id(self):
        """Gets the wallet_id of this WalletSendRequest.  # noqa: E501

        Unique ID of the new created Wallet  # noqa: E501

        :return: The wallet_id of this WalletSendRequest.  # noqa: E501
        :rtype: str
        """
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, wallet_id):
        """Sets the wallet_id of this WalletSendRequest.

        Unique ID of the new created Wallet  # noqa: E501

        :param wallet_id: The wallet_id of this WalletSendRequest.  # noqa: E501
        :type: str
        """

        self._wallet_id = wallet_id

    @property
    def request_id(self):
        """Gets the request_id of this WalletSendRequest.  # noqa: E501

        ID of this transaction, it can be used letter in the callback or to query it  # noqa: E501

        :return: The request_id of this WalletSendRequest.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this WalletSendRequest.

        ID of this transaction, it can be used letter in the callback or to query it  # noqa: E501

        :param request_id: The request_id of this WalletSendRequest.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def timestamp(self):
        """Gets the timestamp of this WalletSendRequest.  # noqa: E501

        Request creation date expressed in UNIX timestamp  # noqa: E501

        :return: The timestamp of this WalletSendRequest.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this WalletSendRequest.

        Request creation date expressed in UNIX timestamp  # noqa: E501

        :param timestamp: The timestamp of this WalletSendRequest.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def lastupdate(self):
        """Gets the lastupdate of this WalletSendRequest.  # noqa: E501

        Last update expressed in UNIX timestamp  # noqa: E501

        :return: The lastupdate of this WalletSendRequest.  # noqa: E501
        :rtype: int
        """
        return self._lastupdate

    @lastupdate.setter
    def lastupdate(self, lastupdate):
        """Sets the lastupdate of this WalletSendRequest.

        Last update expressed in UNIX timestamp  # noqa: E501

        :param lastupdate: The lastupdate of this WalletSendRequest.  # noqa: E501
        :type: int
        """

        self._lastupdate = lastupdate

    @property
    def amount(self):
        """Gets the amount of this WalletSendRequest.  # noqa: E501

        Total amount sent from wallet  # noqa: E501

        :return: The amount of this WalletSendRequest.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this WalletSendRequest.

        Total amount sent from wallet  # noqa: E501

        :param amount: The amount of this WalletSendRequest.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def callback(self):
        """Gets the callback of this WalletSendRequest.  # noqa: E501

        Optional callback to notify your web / app as soon as the send request has been fully broadcasted to the network  # noqa: E501

        :return: The callback of this WalletSendRequest.  # noqa: E501
        :rtype: str
        """
        return self._callback

    @callback.setter
    def callback(self, callback):
        """Sets the callback of this WalletSendRequest.

        Optional callback to notify your web / app as soon as the send request has been fully broadcasted to the network  # noqa: E501

        :param callback: The callback of this WalletSendRequest.  # noqa: E501
        :type: str
        """

        self._callback = callback

    @property
    def destination(self):
        """Gets the destination of this WalletSendRequest.  # noqa: E501

        Array with all the destination coin addres(es) and the amount(s) to send   # noqa: E501

        :return: The destination of this WalletSendRequest.  # noqa: E501
        :rtype: list[AddressDetail]
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this WalletSendRequest.

        Array with all the destination coin addres(es) and the amount(s) to send   # noqa: E501

        :param destination: The destination of this WalletSendRequest.  # noqa: E501
        :type: list[AddressDetail]
        """

        self._destination = destination

    @property
    def txid(self):
        """Gets the txid of this WalletSendRequest.  # noqa: E501

        Tx Hash. *Only available in requests with confirmed status*   # noqa: E501

        :return: The txid of this WalletSendRequest.  # noqa: E501
        :rtype: str
        """
        return self._txid

    @txid.setter
    def txid(self, txid):
        """Sets the txid of this WalletSendRequest.

        Tx Hash. *Only available in requests with confirmed status*   # noqa: E501

        :param txid: The txid of this WalletSendRequest.  # noqa: E501
        :type: str
        """

        self._txid = txid

    @property
    def status(self):
        """Gets the status of this WalletSendRequest.  # noqa: E501

        Status of this send request:   * `0: Queued` Request has been queued for broadcasting. It usually takes few seconds under normal conditions   * `1: Broadcasted` Request has been fully broadcasted to Bitcoin Network    # noqa: E501

        :return: The status of this WalletSendRequest.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WalletSendRequest.

        Status of this send request:   * `0: Queued` Request has been queued for broadcasting. It usually takes few seconds under normal conditions   * `1: Broadcasted` Request has been fully broadcasted to Bitcoin Network    # noqa: E501

        :param status: The status of this WalletSendRequest.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def error(self):
        """Gets the error of this WalletSendRequest.  # noqa: E501

        `true` is there was a problem. `false` if not   # noqa: E501

        :return: The error of this WalletSendRequest.  # noqa: E501
        :rtype: bool
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this WalletSendRequest.

        `true` is there was a problem. `false` if not   # noqa: E501

        :param error: The error of this WalletSendRequest.  # noqa: E501
        :type: bool
        """

        self._error = error

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WalletSendRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WalletSendRequest):
            return True

        return self.to_dict() != other.to_dict()