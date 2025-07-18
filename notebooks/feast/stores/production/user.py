from google.protobuf.duration_pb2 import Duration

from feast import Entity, Feature, FeatureView, FileSource, ValueType


user_hourly_purchases = FileSource(
    path="data/user_hourly_purchases.parquet",
    event_timestamp_column="event_timestamp",  # Name of column containing timestamp when event data occurred
    created_timestamp_column="created",  # Name of column containing timestamp when data is created
)

user = Entity(
    name="user_id", 
    value_type=ValueType.INT64, 
    description="User unique identifier",
)

user_hourly_purchases_view = FeatureView(
    name="user_hourly_purchases",
    entities=["user_id"],
    ttl=Duration(seconds=86400 * 1),
    features=[
        Feature(name="conv_rate", dtype=ValueType.FLOAT),
        Feature(name="acc_rate", dtype=ValueType.FLOAT),
        Feature(name="avg_daily_trips", dtype=ValueType.INT64),
    ],
    online=True,
    batch_source=user_hourly_purchases,
    tags={},
)
