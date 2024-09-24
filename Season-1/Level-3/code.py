# Welcome to Secure Code Game Season-1/Level-3!

# You know how to play by now, good luck!

import os
from flask import Flask, request

### Unrelated to the exercise -- Starts here -- Please ignore
app = Flask(__name__)
@app.route("/")
def source():
    TaxPayer('foo', 'bar').get_tax_form_attachment(request.args["input"])
    TaxPayer('foo', 'bar').get_prof_picture(request.args["input"])
### Unrelated to the exercise -- Ends here -- Please ignore

class TaxPayer:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.prof_picture = None
        self.tax_form_attachment = None

    def safe_path(self, path):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.normpath(os.path.join(base_dir, path))
        if base_dir !=  os.path.commonpath([base_dir, file_path]):
            return None
        return str(file_path)

    # returns the path of an optional profile picture that users can set
    def get_prof_picture(self, path=None):
        # setting a profile picture is optional
        if not path:
            pass

        # defends against path traversal attacks
        if path.startswith('/') or path.startswith('..'):
            return None

        # builds path
        prof_picture_path = self.safe_path(path)

        # assume that image is returned on screen after this
        return prof_picture_path

    # returns the path of an attached tax form that every user should submit
    def get_tax_form_attachment(self, path=None):
        
        tax_data_path = self.safe_path(path)
        if not path:
            raise Exception("Error: Tax form is required for all users")

        # assume that tax data is returned on screen after this
        return tax_data_path