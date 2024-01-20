#version 330 core

layout (location = 0) in vec2 in_texcoord_0;
layout (location = 1) in vec3 in_normal;
layout (location = 2) in vec3 in_position;

uniform mat4 MatrixProjection;
uniform mat4 MatrixViewLight;
uniform mat4 MatrixModel;

void main(){
    mat4 ModelVertexProjection = MatrixProjection * MatrixViewLight * MatrixModel;
    gl_Position = ModelVertexProjection * vec4(in_position, 1.0);
}

