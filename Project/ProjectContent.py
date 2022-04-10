from Project.Traces.TracesContent import TracesContent
from sklearn import svm


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

    def ml_test(self, model_name, data, label, train_size):
        from sklearn.model_selection import train_test_split
        from sklearn.metrics import classification_report
        models_name = {
            "svm": svm.SVC()
        }
        train_data, test_data, train_label, test_label = train_test_split(data, label, train_size=train_size)
        self.clf = models_name[model_name]
        self.clf.fit(train_data, train_label)
        predictions = self.clf.predict(test_data)
        print(classification_report(test_label, predictions))


if __name__ == "__main__":
    my_project = ProjectContent()
    my_project.traces.add_trace("data/Traces-fix key & fix plaintext/ht/50T200S/", 1)
    my_project.traces.add_trace("data/Traces-fix key & fix plaintext/ht/50T400S/", 1)
    my_project.traces.add_trace("data/Traces-fix key & fix plaintext/ht/50T600S/", 1)
    my_project.traces.add_trace("data/Traces-fix key & fix plaintext/ht/50T800S/", 1)
    my_project.traces.add_trace("data/Traces-fix key & fix plaintext/no_ht/50T200S/", 0)
    my_project.traces.add_trace("data/Traces-fix key & fix plaintext/no_ht/50T400S/", 0)
    my_project.traces.add_trace("data/Traces-fix key & fix plaintext/no_ht/50T600S/", 0)
    my_project.traces.add_trace("data/Traces-fix key & fix plaintext/no_ht/50T800S/", 0)
    my_project.ml_test("svm", my_project.traces.waves, my_project.traces.htflag, 0.7)
