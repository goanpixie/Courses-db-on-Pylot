"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('Course')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        extracts=self.models['Course'].extract()
        print extracts
        return self.load_view('index.html', extracts=extracts)


    def create(self):
        add=self.models['Course'].create(request.form)
        return redirect('/')

    def remove_form(self,id):

        extracts_one=self.models['Course'].extract_one_record(id)
        print extracts_one
        return self.load_view('remove_form.html', extracts_one=extracts_one, id=id)

    def delete_record(self,id):
        delete_one=self.models['Course'].delete_record(id)
        print delete_one
        return redirect('/')





