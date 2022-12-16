class Spam:

    @staticmethod
    def to_file(path, data):
        with open(path, 'w') as f:
            f.write(data)

    @staticmethod
    def from_file(path):
        with open(path, 'r') as f:
            data = f.read()
            return data

    @staticmethod
    def comparator(from_file, current_build):
        if len(from_file) == len(current_build):
            if len(set(current_build).intersection(from_file)) == len(current_build):
                pass
            if len(set(current_build).difference(from_file)) > 0:
                return False
        else:
            return False
