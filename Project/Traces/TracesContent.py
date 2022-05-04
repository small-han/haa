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
        self.data = {"train_data": None, "train_label": None, "test_data": None, "test_label": None}

    def _set_data(self, data, htflag, data_type="train"):
        if data_type + "_data" not in self.data:
            self.data[data_type + "_data"] = data
            if htflag == 0:
                self.data[data_type + "_label"] = np.zeros(data.shape[0])
            else:
                self.data[data_type + "_label"] = np.ones(data.shape[0])
        else:
            self.data[data_type + "_data"] = np.vstack((self.data[data_type + "_data"], data))
            if htflag == 0:
                self.data[data_type + "_label"] = np.hstack((self.data[data_type + "_label"], np.zeros(data.shape[0])))
            else:
                self.data[data_type + "_label"] = np.hstack((self.data[data_type + "_label"], np.ones(data.shape[0])))

    def add_trace(self, path, htflag, data_type="train"):
        files_name = detect_name(path)
        data = np.load(path + files_name["traces"])
        self._set_data(data, htflag, data_type)

    def split_data(self, train_size):
        from sklearn.model_selection import train_test_split
        all_data = np.vstack((self.data["train_data"], self.data["test_data"]))
        all_label = np.hstack((self.data["train_label"], self.data["test_label"]))
        self.data["train_data"], self.data["test_data"], self.data["train_label"], self.data["test_label"] = \
            train_test_split(all_data, all_label, train_size)



if __name__ == "__main__":
    my_trace = TracesContent()
    my_trace.add_trace("../../data/Traces-fix key & fix plaintext/ht/50T200S/", 1)
    my_trace.add_trace("../../data/Traces-fix key & fix plaintext/no_ht/50T200S/", 0)
    print("hello")
