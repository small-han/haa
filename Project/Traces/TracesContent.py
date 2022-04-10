# -*- coding: UTF-8 -*-
import numpy as np
import os


# 返回路径下的文件名的字典序
def detect_name(path):
    filelist = os.listdir(path)
    files_name = {}
    for i in filelist:
        if "keylist" in i:
            files_name["keylist"] = i
        elif "textin" in i:
            files_name["textin"] = i
        elif "textout" in i:
            files_name["textout"] = i
        elif "traces" in i:
            files_name["traces"] = i
        else:
            pass
    assert "keylist" in files_name, "未找到keylist"
    assert "textin" in files_name, "未找到textin"
    assert "textout" in files_name, "未找到textout"
    assert "traces" in files_name, "未找到traces"
    return files_name


class TracesContent(object):

    def __init__(self):
        self.num = 0
        self.htflag = []
        self.waves = []
        self.keys = []
        self.textin = []
        self.textout = []

    def add_trace(self, path, htflag):
        files_name = detect_name(path)
        if self.num == 0:  # 如果原来没有numpy数组
            self.waves = np.load(path + files_name["traces"])
            self.keys = np.load(path + files_name["keylist"])
            self.textin = np.load(path + files_name["textin"])
            self.textout = np.load(path + files_name["textout"])
            if htflag == 0:
                self.htflag = np.zeros(self.waves.shape[0])
            else:
                self.htflag = np.ones(self.waves.shape[0])
        else:  # 添加新的numpy数组
            self.waves = np.vstack((self.waves, np.load(path + files_name["traces"])))
            self.keys = np.vstack((self.keys, np.load(path + files_name["keylist"])))
            self.textin = np.vstack((self.textin, np.load(path + files_name["textin"])))
            self.textout = np.vstack((self.textout, np.load(path + files_name["textout"])))
            if htflag == 0:
                self.htflag = np.hstack((self.htflag, np.zeros(self.waves.shape[0] - self.htflag.shape[0])))
            else:
                self.htflag = np.hstack((self.htflag, np.ones(self.waves.shape[0] - self.htflag.shape[0])))
        assert self.waves.shape[0] == self.keys.shape[0] == self.textin.shape[0] == \
               self.textout.shape[0] == self.htflag.shape[0], "traces长度不一样"
        self.num += len(self.waves)


if __name__ == "__main__":
    my_trace = TracesContent()
    my_trace.add_trace("../../data/Traces-fix key & fix plaintext/ht/50T200S/", 1)
    my_trace.add_trace("../../data/Traces-fix key & fix plaintext/no_ht/50T200S/", 0)
    print("hello")
