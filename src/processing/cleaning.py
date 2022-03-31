# import '../data/load-training-datasets.py'
from src.data.load_training_datasets import load_n_transaction, load_fee_per_transaction_dataset, number_of_transaction_per_month_dataset, trading_volume_dataset, transaction_per_min_dataset

# circulating_bitcoins.merge( n_transactions, how='outer', right_index=True, left_index=True) \
#   .merge( fee_transaction, how='outer', right_index=True, left_index=True) \
#   .merge( marketcap, how='outer', right_index=True, left_index=True)\
#   .merge( n_trade, how='outer', right_index=True, left_index=True) \
#   .merge(yahoo_data, how='outer', right_index=True, left_index=True).fillna(0)
# six = pd.merge(five, trading_volume, how='outer', right_index=True, left_index=True)