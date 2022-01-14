import sys
import mariadb
import WaterServices

import numpy
import pandas
import datetime
import math
import os

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import RepeatVector
from keras.layers import TimeDistributed
from sklearn.preprocessing import MinMaxScaler

# params chosen arbitrarily
LOOK_BACK = 20
FORECAST_RANGE = 1

def toTrainData(df):
    # GageHeight, Precipitation, Temperature, Turbidity
    a = [[x.get('GageHeight', -1), x.get('Precipitation', -1), x.get("Temperature", -1), x.get("Turbidity", -1)] for x in df.to_dict('records')]
    b = numpy.array(a)
    b[b== ''] = -1
    return b.astype(numpy.float32)

def split_sequence(sequence, look_back, forecast_horizon):
 X, y = list(), list()
 for i in range(len(sequence)):
   lag_end = i + look_back
   forecast_end = lag_end + forecast_horizon
   if forecast_end > len(sequence):
     break
   seq_x, seq_y = sequence[i:lag_end], sequence[lag_end:forecast_end]
   X.append(seq_x)
   y.append(seq_y)
 return numpy.array(X), numpy.array(y)

def inverse_transform(y_test, yhat, scaler):
 y_test_reshaped = y_test.reshape(-1, y_test.shape[-1])
 yhat_reshaped = yhat.reshape(-1, yhat.shape[-1])
 yhat_inverse = scaler.inverse_transform(yhat_reshaped)
 y_test_inverse = scaler.inverse_transform(y_test_reshaped)
 return yhat_inverse, y_test_inverse

def predictForSite(site):
    data = WaterServices.getData(site)
    df = pandas.DataFrame(data)
    df.sort_values(by='datetime')
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled = scaler.fit_transform(toTrainData(df))

    x,y = split_sequence(scaled, LOOK_BACK, FORECAST_RANGE)

    model = Sequential()
    model.add(LSTM(10, activation='relu', input_shape=(LOOK_BACK, 4)))
    model.add(RepeatVector(FORECAST_RANGE))
    model.add(LSTM(10, activation='relu', return_sequences=True))
    model.add(TimeDistributed(Dense(4)))
    model.compile(loss='mae', optimizer='adam')
    model.fit(x, y, epochs=50, batch_size=20, validation_split=0.1, verbose=2, shuffle=False)
    yhat = model.predict(x, verbose=0)
    yhat_inverse, y_test_inverse = inverse_transform(y, yhat, scaler)
    # format for app
    new_time = datetime.datetime.strptime(df.iloc[-1]['datetime'], "%Y-%m-%d %H:%M") + datetime.timedelta(minutes=15)
    results = []
    for i in range(len(yhat_inverse)):
        new_time = datetime.datetime.strptime(df.iloc[i]['datetime'], "%Y-%m-%d %H:%M") + datetime.timedelta(minutes=15)
        results.append({"gageHeight": yhat_inverse[i,0], "Precipitation": yhat_inverse[i,1], "Temperature": yhat_inverse[i,2], "Turbidity": yhat_inverse[i,3], "datetime": new_time, "site": site})

    return results

RiverPredictorModel = {}
RiverPredictorModel['predictForSite'] = predictForSite
__all__ = ["predictForSite", "getSite", "getData"]
