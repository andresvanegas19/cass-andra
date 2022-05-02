# Machine learning Model

### Gated Recurrent Unit Model for predice the Bitcoin Price

This scripts will be the model for predicting the price of btc

para el modelo se tiene dos opciones

gated recurrent units (GRU), long short term memory units (LSTM), and bidirectional LSTM units (BiLSTM). <!--  -->

change the opinion see the rendimiento of the GRU y HHM

y es lstm por el tema de memoria
y time forecasting para el tema de tiempo

RNN vs LSTM vs GRU

# NOTES

```
    model LSTM layers with d 32 layers hidden with dropout will be overfitting.
```

```
    The sequence == 100, means the model learn long-term between time steps of 100d at a time.
```

```
    Signo de mal ajuste pudo ser en el entrenamiento de prueba, resolverlo puede aumentar el numero de epocas.
```

Mean Absolute Error (MAE) which is the average of the absolute errors in the test data.