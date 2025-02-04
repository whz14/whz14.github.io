# data processing for CPET in 20230916085045

import pandas as pd
import pwlf
import matplotlib.pyplot as plt
data = pd.read_csv('code/data/20230916085045_CPET.csv')

def lt2(vo2, vco2):
    vco2, vo2 = vco2.astype(float), vo2.astype(float)
    model = pwlf.PiecewiseLinFit(vo2, vco2)
    breaks = model.fit(2)
    print('vo2 break point, AT:', breaks)
    slopes = model.slopes
    intercepts = model.intercepts
    print("斜率:", slopes)
    print("截距:", intercepts)

    plt.scatter(vo2, vco2)
    plt.plot(sorted(vo2), model.predict(sorted(vo2)), color='red')
    # plt.plot(sorted(vo2), )
    plt.xlabel('vo2/(ml/min)')
    plt.ylabel('vco2/(ml/min)')
    plt.savefig('./code/data/AT.jpg')
    return breaks


if __name__ == '__main__':
    columns = data.columns
    meta_data = data[columns[:10]]
    detail_data = data[columns[10:]]
    vco2 = detail_data['VCO2'][2:]
    vo2 = detail_data['VO2'][2:]

    print(lt2(vo2, vco2))
