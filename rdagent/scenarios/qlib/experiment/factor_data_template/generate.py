import qlib

qlib.init(provider_uri="~/.qlib/qlib_data/cn_data")

from qlib.data import D

instruments = D.instruments(market="active")
fields = ["$open", "$close", "$high", "$low", "$volume", "$oi", "$month", "$week", "$quarter"]
data = D.features(instruments, fields, freq="day").swaplevel().sort_index().loc["2005-12-29":].sort_index()

data.to_hdf("./daily_pv_all.h5", key="data")


fields = ["$open", "$close", "$high", "$low", "$volume", "$oi", "$month", "$week", "$quarter"]
data = D.features(
    instruments, fields, start_time="2018-01-01", end_time="2019-12-31", freq="day"
).swaplevel().sort_index()
# 获取前100个 instrument
instruments_100 = data.index.get_level_values("instrument").unique()[:100]

# 只保留这100个 instrument 的所有数据
data_100 = data[data.index.get_level_values("instrument").isin(instruments_100)].sort_index()
data_100.to_hdf("./daily_pv_debug.h5", key="data")


