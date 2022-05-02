circulating_bitcoins.merge( n_transactions, how='outer', right_index=True, left_index=True) \
  .merge( fee_transaction, how='outer', right_index=True, left_index=True) \
  .merge( marketcap, how='outer', right_index=True, left_index=True)\
  .merge( n_trade, how='outer', right_index=True, left_index=True) \
  .merge(yahoo_data, how='outer', right_index=True, left_index=True).fillna(0)
six = pd.merge(five, trading_volume, how='outer', right_index=True, left_index=True)