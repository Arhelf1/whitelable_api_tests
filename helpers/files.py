class Files:

    @staticmethod
    def validate_file_data(data):

        error_count = 0

        for d in data:
            if len(d['data']) > 0:
                pass
            else:
                print('\n/Files/FindByDoc method return empty <DATA> field | {0} |'.format(d))
                error_count += 1

        if error_count > 0:
            return False
        else:
            return True

    @staticmethod
    def get_response_data(data):

        _document_id = [d['documentId'] for d in data]
        _id = [d['id'] for d in data]
        return _id, _document_id
