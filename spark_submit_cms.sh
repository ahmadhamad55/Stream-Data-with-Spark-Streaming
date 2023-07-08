spark-submit \
    --master yarn \
    --deploy-mode cluster \
    --driver-memory 2g \
    --executor-memory 2g \
    --executor-cores 1 \
    streaming_csv.py