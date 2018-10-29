"""
``FinancialHistory`` keeps track of a person's expenses,
income, and balance.

Create ``FinancialHistory`` with $ 100.

    >>> h = FinancialHistory(100)
    >>> h
    <FinancialHistory(100.00): 0 transactions>

Spend some money::

    >>> h.spend(39.95, 'meal')
    >>> h
    <FinancialHistory(60.05): 1 transaction>
    >>> h.balance()
    Decimal('60.0500000')

Decimals can be formatted like floats::

    >>> print(f'${h.balance():0.2f}')
    $60.05

Get more money::

    >>> h.receive(1000.01, "Molly's game")
    >>> h.receive(10.01, 'found on street')
    >>> h
    <FinancialHistory(1070.07): 3 transactions>

Spend more money::

    >>> h.spend(55.35, 'meal')
    >>> h.spend(26.65, 'meal')
    >>> h.spend(300, 'concert')
    >>> h
    <FinancialHistory(688.07): 6 transactions>

Check amount spent on meals::

    >>> h.spent_for('meal')
    Decimal('121.950000')

Check amount spent on travel (zero):

    >>> h.spent_for('travel')
    Decimal('0')

"""

import collections
import decimal
from decimal import Decimal

Transaction = collections.namedtuple("Transaction", "amount party")

decimal.setcontext(decimal.BasicContext)


class FinancialHistory:
    def __init__(self, amount=0):
        self._balance = Decimal(amount)
        self._history = []

    def __repr__(self):
        bal = self._balance
        len_hist = len(self._history)
        plural = "s" if len_hist != 1 else ""
        return f"<FinancialHistory({bal:0.2f}): {len_hist} transaction{plural}>"

    def receive(self, amount, source):
        amount = Decimal(amount)
        self._history.append(Transaction(amount, source))
        self._balance += amount

    def spend(self, amount, reason):
        amount = Decimal(amount)
        self._history.append(Transaction(amount, reason))
        self._balance -= amount

    def balance(self):
        return self._balance

    def spent_for(self, reason):
        select = (t.amount for t in self._history if t.party == reason)
        return sum(select, Decimal(0))
