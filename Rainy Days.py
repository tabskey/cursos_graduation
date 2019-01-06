# -*- coding: utf-8 -*-
"""

@author: 749403
"""

import pandas
import pandasql


def num_rainy_days(filename):
    
    
    weather_data = pandas.read_csv(filename)

    q = """
    SELECT COUNT(*) FROM weather_data WHERE rain = 1;
    """

    #Execute your SQL command against the pandas frame
    rainy_days = pandasql.sqldf(q.lower(), locals())
    return rainy_days