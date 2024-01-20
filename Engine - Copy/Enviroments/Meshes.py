from Enviroments.VertexArrayObject import VertexArray
from Enviroments.VertexBufferObject import VertexBuffer
from Enviroments.Texture import Texture

class Mesh:
    def __init__(self,Application):
        self.Application = Application
        self.VertexBufferObject = VertexBuffer(Application.Context)
        self.VertexArrayObject = VertexArray(Application.Context)
        self.Texture = Texture(Application)

    def Destroy(self):
        self.VertexArrayObject.Destroy()
        self.Texture.Destroy()