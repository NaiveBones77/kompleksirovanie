import pandas as pd
import numpy as np
from pylab import*
import scaleogram as scg
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Заменяя вейвлеты можно исследовать зависимость временного разрешения от масштаба
#По умолчанию используется вейвлет 'cmor1-1.5'
#scg.set_default_wavelet('cmor1-1.5')
#scg.set_default_wavelet('cgau5')
#scg.set_default_wavelet('cgau1')
#scg.set_default_wavelet('shan0.5-2')
#scg.set_default_wavelet('mexh')

#удалить аномальные данные
df = df[(df.day>=1) & (df.day<=31) & (df.births.values > 1000)]

# преобразование дат
datetime = pd.to_datetime(df[['year', 'month', 'day']], errors='coerce')
df.insert(0, 'datetime', datetime)

datetime_lim = [ df.datetime.min(), df.datetime.max() ]
years_lim = [ df.datetime.min().year, df.datetime.max().year ]
births = df[['datetime', 'births']].groupby('datetime').sum().squeeze()
def set_x_yearly(ax, days, start_year=1969):
    xlim  = (np.round([0, days]) / 365).astype(np.int32)
    ticks = np.arange(xlim[0], xlim[1])
    ax.set_xticks(ticks*365)
    ax.set_xticklabels(start_year + ticks)

fig = figure(figsize=(12,2))
lines = plot(births.index, births.values/1000, '-')
xlim(datetime_lim)

ylabel("Nb of birthes [k]"); title("Total births per day in the US (CDC)");
xlim = xlim()

ax = scg.cws(births, figsize=(13.2, 4), xlabel="Year", ylabel="Nb of Day")
set_x_yearly(ax, len(births))
show()