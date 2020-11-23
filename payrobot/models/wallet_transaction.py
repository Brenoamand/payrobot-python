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


class WalletTransaction(object):
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
        'amount': 'str',
        'addresses': 'list[AddressDetail]',
        'timestamp': 'int'
    }

    attribute_map = {
        'amount': 'amount',
        'addresses': 'addresses',
        'timestamp': 'timestamp'
    }

    def __init__(self, amount=None, addresses=None, timestamp=None, local_vars_configuration=None):  # noqa: E501
        """WalletTransaction - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amount = None
        self._addresses = None
        self._timestamp = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if addresses is not None:
            self.addresses = addresses
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def amount(self):
        """Gets the amount of this WalletTransaction.  # noqa: E501

        Amount of the transaction:   * `Negative number (< 0)` is a withdrawal   * `Positive number (> 0)` is a deposit   # noqa: E501

        :return: The amount of this WalletTransaction.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this WalletTransaction.

        Amount of the transaction:   * `Negative number (< 0)` is a withdrawal   * `Positive number (> 0)` is a deposit   # noqa: E501

        :param amount: The amount of this WalletTransaction.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def addresses(self):
        """Gets the addresses of this WalletTransaction.  # noqa: E501

        Address(es) involved:   * `payments` address(es) where payment was received   * `withdrawals` address(es) where funds were sent   # noqa: E501

        :return: The addresses of this WalletTransaction.  # noqa: E501
        :rtype: list[AddressDetail]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this WalletTransaction.

        Address(es) involved:   * `payments` address(es) where payment was received   * `withdrawals` address(es) where funds were sent   # noqa: E501

        :param addresses: The addresses of this WalletTransaction.  # noqa: E501
        :type: list[AddressDetail]
        """

        self._addresses = addresses

    @property
    def timestamp(self):
        """Gets the timestamp of this WalletTransaction.  # noqa: E501

        Timestamp of the transaction expressed in `Unix Timestamp`  # noqa: E501

        :return: The timestamp of this WalletTransaction.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this WalletTransaction.

        Timestamp of the transaction expressed in `Unix Timestamp`  # noqa: E501

        :param timestamp: The timestamp of this WalletTransaction.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

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
        if not isinstance(other, WalletTransaction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WalletTransaction):
            return True

        return self.to_dict() != other.to_dict()