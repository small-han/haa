import numpy as np
import os

class Traces (object):
    
    def __init__(self):
        self.num=0
        self.waves=[]
        self.keys=[]
        self.textin=[]
        self.textout=[]
    
    def add_trace(self,path):
        files_name=self.detect_name(path)
        self.trace_data=np.load(path+files_name["traces"])

    def detect_name(self, path):
        filelist =os.listdir(path)
        files_name = {}
        for i in filelist:
            if "knownkey" in i:
                files_name["knownkey"] = i
            elif "textin" in i:
                files_name["textin"] = i
            elif "textout" in i:
                files_name["textout"] = i
            elif "traces" in i:
                files_name["traces"] = i
            else:
                pass
        assert "knownkey" in files_name ,"未找到knownkey"
        assert "textin" in files_name ,"未找到textin"
        assert "textout" in files_name ,"未找到textout"
        assert "traces" in files_name ,"未找到traces"
        return files_name
