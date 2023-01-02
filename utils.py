import os
import numpy


class DataFiles():
    def __init__(self, path="data") -> None:
        classes = os.listdir(path)
        self._df = []
        for class_name in classes:
            data_filenames = os.listdir(f"{path}/{class_name}")
            for data_filename in data_filenames:
                data_basename = ".".join(data_filename.split(".")[:-1])
                self._df.append((class_name, data_basename, numpy.load(
                    f"{path}/{class_name}/{data_filename}")))

    def __iter__(self):
        return iter(self._df)


if __name__ == "__main__":
    for c, b, d in DataFiles():
        print(f"{c},{b}")
