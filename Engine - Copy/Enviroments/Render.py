class Renderer:
    def __init__(self,Application):
        self.Application = Application
        self.Context = Application.Context
        self.Mesh = Application.Mesh
        self.Scene = Application.Scene

        self.Texture = self.Mesh.Texture.Textures['DepthTexture']
        self.Depth = self.Context.framebuffer(depth_attachment=self.Texture)

    def RenderShadow(self):
        self.Depth.clear()
        self.Depth.use()
        for Object in self.Scene.Objects:
            Object.RenderShadow()

    def RenderEnviroment(self):
        self.Application.Context.screen.use()
        for Object in self.Scene.Objects:
            Object.Render()
        self.Scene.Skybox.Render()

    def Render(self):
        self.Scene.Update()
        self.RenderShadow()
        self.RenderEnviroment()

    def Destroy(self):
        self.Depth.release()