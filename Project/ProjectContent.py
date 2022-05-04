from Project.Traces.TracesContent import TracesContent
from sklearn import svm
import matplotlib.pyplot as plt


class ProjectContent(object):
    def __init__(self):
        self.clf = None
        self.proj_path = None
        self.traces = TracesContent()

    def create_project(self, proj_path):
        self.proj_path = proj_path

    def svm_train(self, train_data, results):
        self.clf = svm.SVC()
        self.clf.fit(train_data, results)


if __name__ == "__main__":
    my_project = ProjectContent()
    my_project.traces.add_trace("data/Traces-fix key & fix plaintext/ht/50T800S/", 1)
    my_project.traces.add_trace("data/Traces-fix key & fix plaintext/no_ht/50T800S/", 0)
    my_project.ml_test("svm", my_project.traces.waves, my_project.traces.htflag, 0.7)
