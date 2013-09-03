from __future__ import division

import re
#under line is contact
re_list = [
    re.compile(r'\d{2}\.[\d] '),
    re.compile(r'=1[\d]{2}\.[\d] '),
    re.compile(r'=[2-4][\d]{2}\.[\d] '),
    re.compile(r'=[5-9][\d]{2}\.[\d] '),
    re.compile(r'=[\d]{4}\.[\d] ')
]
ms_under_100, ms_100_200 ,ms_200_500 ,ms_500_1000 ,ms_above_1k =  re_list[0],re_list[1],re_list[2],re_list[3],re_list[4]
file_name = r"D:\ping_logs.txt"
class PingTools:
    def __init__(self, file_path, ping_re):
        self.file_object = file_path
        self.ping_object = ping_re
    def pingResultList(self):
        try:
            the_file_lines = open(self.file_object)
            the_result_list = []
            for the_line in the_file_lines:
                result_line = re.findall(self.ping_object, the_line)
                the_result_list.extend(result_line)
            the_file_lines.close()
            return the_result_list
        except IOError:
            raise IOError

    def resultHandler(self):
        result_list = self.pingResultList()
        sum_time = 0
        sum_count = 0
        for value in result_list:
            ping_time = value.strip('=').strip(' ')
            sum_time += float(ping_time)
            sum_count += 1
        return [sum_time,sum_count]
class Handler:
    def __init__(self):
        pass
    def showResult(self, list1, list2, list3, list4, list5,deviceID):
        print "device id: " + deviceID
        print "=============== under 100 ================"
        print list1[0]/list1[1]
        print list1[1]
        print "=============== 100 ~ 200 ================"
        print list2[0]/list2[1]
        print list2[1]
        print "=============== 200 ~ 500 ================"
        print list3[0]/list3[1]
        print list3[1]
        print "=============== 500 ~ 1000 ================"
        print list4[0]/list4[1]
        print list4[1]
        print "=============== above 1000 ================"
        print list5[0]/list5[1]
        print list5[1]
        print "=============== all result ================"
        print list1[1] + list2[1] + list3[1] + list4[1] + list5[1]
        print (list1[0] + list2[0] + list3[0] + list4[0] + list5[0])/(list1[1] + list2[1] + list3[1] + list4[1] + list5[1])
        print "Item number under 100ms count/all count "
        print list1[1]/(list1[1] + list2[1] + list3[1] + list4[1] + list5[1])
#method invoke!
pingObject1 = PingTools(file_name,ms_under_100)
results1 = pingObject1.pingResultList()
pingObject2 = PingTools(file_name,ms_100_200)
results2 = pingObject2.pingResultList()
pingObject3 = PingTools(file_name,ms_200_500)
results3 = pingObject3.pingResultList()
pingObject4 = PingTools(file_name,ms_500_1000)
results4 = pingObject4.pingResultList()
pingObject5 = PingTools(file_name,ms_above_1k)
results5 = pingObject5.pingResultList()
h1 = Handler()
h1.showResult(results1,results2,results3,results4,results5,"none")