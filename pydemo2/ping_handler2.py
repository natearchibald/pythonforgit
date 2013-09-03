#coding:utf-8
from __future__ import division

import re
#under line is contact
class PingTools:
    def __init__(self, file_path):
        self.file_object = file_path
    def pingResultList(self, ping_re):
        try:
            the_file_lines = open(self.file_object)
            the_result_list = []
            for the_line in the_file_lines:
                result_line = re.findall(ping_re, the_line)

                the_result_list.extend(result_line)
            the_file_lines.close()
            return the_result_list
        except IOError:
            raise IOError

    def resultHandler(self, result_list):
        sum_time = 0
        sum_count = 0
        for value in result_list:
            ping_time = value.strip('=').strip(' ')
            sum_time += float(ping_time)
            sum_count += 1
        return [sum_time,sum_count]
#h1 = Handler()
#h1.showResult(results1,results2,results3,results4,results5,"none")