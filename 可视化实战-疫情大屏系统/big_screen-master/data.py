#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from test import *


class SourceDataDemo:

    def __init__(self):
        confirmed, cured = word_global()
        self.title = '全球疫情数据可视化系统'
        self.counter = {'name': '确诊人数', 'value': confirmed}
        self.counter2 = {'name': '治愈人数', 'value': cured}
        list_countries = countries_global()
        self.echart1_data = {
            'title': '确诊人数最多的国家',
            'data': [
                {"name": list_countries[0][0], "value": list_countries[0][1]},
                {"name": list_countries[1][0], "value": list_countries[1][1]},
                {"name": list_countries[2][0], "value": list_countries[2][1]},
                {"name": list_countries[3][0], "value": list_countries[3][1]},
                {"name": list_countries[4][0], "value": list_countries[4][1]},
                {"name": list_countries[5][0], "value": list_countries[5][1]},
                {"name": list_countries[6][0], "value": list_countries[6][1]},
            ]
        }
        list_use = use_global()
        self.echart2_data = {
            'title': '美国确诊最高的省份',
            'data': [
                {"name": list_use[0][0], "value": list_use[0][1]},
                {"name": list_use[1][0], "value": list_use[1][1]},
                {"name": list_use[2][0], "value": list_use[2][1]},
                {"name": list_use[3][0], "value": list_use[3][1]},
                {"name": list_use[4][0], "value": list_use[4][1]},
                {"name": list_use[5][0], "value": list_use[5][1]},
                {"name": list_use[6][0], "value": list_use[6][1]},
            ]
        }
        list_continents = continents_global()
        self.echarts3_1_data = {
            'title': '北美洲确诊国家',
            'data': [
                {"name": list_continents[0][0][0], "value": list_continents[0][0][1]},
                {"name": list_continents[0][1][0] , "value": list_continents[0][1][1]},
                {"name": list_continents[0][2][0] , "value": list_continents[0][2][1]},
                {"name": list_continents[0][3][0] , "value": list_continents[0][3][1]},
                {"name": list_continents[0][4][0] , "value": list_continents[0][4][1]},
                {"name": list_continents[0][5][0] , "value": list_continents[0][5][1]},
            ]
        }
        self.echarts3_2_data = {
            'title': '亚洲确诊国家',
            'data': [
                {"name": list_continents[1][0][0], "value": list_continents[1][0][1]},
                {"name": list_continents[1][1][0], "value": list_continents[1][1][1]},
                {"name": list_continents[1][2][0], "value": list_continents[1][2][1]},
                {"name": list_continents[1][3][0], "value": list_continents[1][3][1]},
                {"name": list_continents[1][4][0], "value": list_continents[1][4][1]},
                {"name": list_continents[1][5][0], "value": list_continents[1][5][1]},
            ]
        }
        self.echarts3_3_data = {
            'title': '欧洲确诊国家',
            'data': [
                {"name": list_continents[2][0][0], "value": list_continents[2][0][1]},
                {"name": list_continents[2][1][0], "value": list_continents[2][1][1]},
                {"name": list_continents[2][2][0], "value": list_continents[2][2][1]},
                {"name": list_continents[2][3][0], "value": list_continents[2][3][1]},
                {"name": list_continents[2][4][0], "value": list_continents[2][4][1]},
                {"name": list_continents[2][5][0], "value": list_continents[2][5][1]},
            ]
        }
        list_use_chain = use_china_global()
        self.echart4_data = {
            'title': '中美疫情对比',
            'data': [
                {"name": "中国", "value": list_use_chain[1]},
                {"name": "美国", "value": list_use_chain[0]},
            ],
            'xAxis': ['1天', '2天前', '3天前', '4天前', '5天前', '6天前', '7天前'],
        }

        list_chain = china_global()
        self.echart5_data = {
            'title': '中国疫情最新确诊最高的省份',
            'data': [
                {"name": list_chain[0][0], "value":list_chain[0][1]},
                {"name": list_chain[1][0], "value":list_chain[1][1]},
                {"name": list_chain[2][0], "value":list_chain[2][1]},
                {"name": list_chain[3][0], "value":list_chain[3][1]},
                {"name": list_chain[4][0], "value":list_chain[4][1]},
                {"name": list_chain[5][0], "value":list_chain[5][1]},
                {"name": list_chain[6][0], "value":list_chain[6][1]},
                {"name": list_chain[7][0], "value":list_chain[7][1]},
            ]
        }
        list_statistics = statistics_global()
        self.echart6_data = {
            'title': '全球疫情状况',
            'data': [
                {"name": "current", "value": list_statistics[0], "value2": int(100000000-int(list_statistics[0])), "color": "01", "radius": ['59%', '70%']},
                {"name": "cure", "value": list_statistics[1], "value2": int(100000000-int(list_statistics[1])), "color": "02", "radius": ['49%', '60%']},
                {"name": "dead", "value": list_statistics[2], "value2": int(10000000-int(list_statistics[2])), "color": "03", "radius": ['39%', '50%']},
                {"name": "incr", "value": list_statistics[3], "value2": int(1000000-int(list_statistics[3])), "color": "04", "radius": ['29%', '40%']},

            ]
        }
        list_map = map_chian()
        self.map_1_data = {
            'symbolSize': 1000,
            'data': list_map
        }

    @property
    def echart1(self):
        data = self.echart1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echart2(self):
        data = self.echart2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echarts3_1(self):
        data = self.echarts3_1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_2(self):
        data = self.echarts3_2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_3(self):
        data = self.echarts3_3_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart4(self):
        data = self.echart4_data
        echart = {
            'title': data.get('title'),
            'names': [i.get("name") for i in data.get('data')],
            'xAxis': data.get('xAxis'),
            'data': data.get('data'),
        }
        return echart

    @property
    def echart5(self):
        data = self.echart5_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart6(self):
        data = self.echart6_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def map_1(self):
        data = self.map_1_data
        echart = {
            'symbolSize': data.get('symbolSize'),
            'data': data.get('data'),
        }
        return echart


class SourceData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        self.title = '全球疫情数据可视化系统'

