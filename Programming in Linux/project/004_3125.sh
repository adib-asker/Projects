#!/bin/bash

#exit on error
set -e

#update period in seconds ( 3 minutes)
UPDATE_PERIOD='180'

#Download the web pages
STOCK_SITE='http://online.wsj.com/mdc/public/page/2_3021-activnyse-actives.html?mod=mdc_mstactv'
STOCK_FILE='stocks.html'

while [ 1 -eq 1 ]; do
  wget -O${STOCK_FILE} ${STOCK_SITE}

  #extract information
  python ./web_processing_framework.py ${STOCK_FILE}

  #remove the data file
  #rm -f ${STOCK_FILE}

  #pause for 3 minutes, between updates
  sleep ${UPDATE_PERIOD}
done
