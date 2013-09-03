from __future__ import division
import tornado.ioloop
import tornado.web
import time
from ping_handler2 import PingTools
import re
import os
ms_under_100 = re.compile(r'=\d{2}\.?\d?\s')  # like '=22.2 ms' or '=22 ms'
ms_100_200 = re.compile(r'=1[\d]{2}\.?\d?\s')
ms_200_500 = re.compile(r'=[2-4]\d{2}\.?\d?\s')
ms_500_1000 = re.compile(r'=[5-9][\d]{2}\.?\d?\s')
ms_above_1k = re.compile(r'=[\d]{4}\.?\d?\s')


class UploadFileHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("upload-file.html")

    def post(self):
        file_dict_list = self.request.files['upl']
        #for file_dict in file_dict_list:
        file_dict = file_dict_list[0]
        filename = file_dict["filename"]
        f = open("D:/ftpUpload/ping_logs/%s" % filename, "wb")
        f.write(file_dict["body"])
        time.sleep(1)

        f.close()
        #begin ping test
        pingObject = PingTools("D:/ftpUpload/ping_logs/%s" % filename)
        result_list1 = pingObject.pingResultList(ms_under_100)
        results1 = pingObject.resultHandler(result_list1)

        result_list2 = pingObject.pingResultList(ms_100_200)
        results2 = pingObject.resultHandler(result_list2)

        result_list3 = pingObject.pingResultList(ms_200_500)
        results3 = pingObject.resultHandler(result_list3)

        result_list4 = pingObject.pingResultList(ms_500_1000)
        results4 = pingObject.resultHandler(result_list4)

        result_list5 = pingObject.pingResultList(ms_above_1k)
        results5 = pingObject.resultHandler(result_list5)

        allcount = results1[1] + results2[1] + results3[1] + results4[1] + results5[1]
        alltimes = results1[0] + results2[0] + results3[0] + results4[0] + results5[0]

        avgtimes = alltimes/allcount
        all100 = results1[1]/allcount
        all100 = all100*100
        all100 = '%.2f' % all100
        
        if results1[1] != 0 and results2[1] != 0 and results3[1] != 0 and results4[1] != 0 and results5[1] != 0:
            
            result_under_100 = results1[0]/results1[1]  # this line have bug,if results[1] value is zero...
            result_100_200 = results2[0]/results2[1]
            result_200_500 =  results3[0]/results3[1]
            result_500_1000 =  results4[0]/results4[1]
            result_above_1k =  results5[0]/results5[1]
            self.render("result.html",
                        filenames = filename,
                        under100count = results1[1],
                        under100avg = result_under_100,

                        count100_200 = results2[1],
                        avg100_200 = result_100_200,

                        count200_500 = results3[1],
                        avg200_500 = result_200_500,

                        count500_1000 = results4[1],
                        avg500_1000 = result_500_1000,

                        count_1k = results5[1],
                        avg_1k = result_above_1k,

                        allcounts = allcount,
                        avgtimess = avgtimes,
                        all100s = all100,
            )
        else:
            self.render("error.html")


settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),  # use static path,for bootstrap framework
    "debug": True,  # auto reload
}
application = tornado.web.Application([
    (r"/upload", UploadFileHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
