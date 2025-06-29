
Quotex AI Backend - Deployment Guide

1. Install requirements:
   pip install -r requirements.txt

2. Make sure the 'quotex_signal_model.h5' file is in the same folder.

3. Run the server:
   python app.py

4. POST to /predict with JSON:
   {
       "input": [[[50 OHLCV values, each row: open, high, low, close, volume]]]
   }
