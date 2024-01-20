#version 330 core
out vec4 fragColor;

in vec4 clipCoords;

uniform samplerCube TextureSkybox;
uniform mat4 ProjectionInverseView;


void main() {
    vec4 worldCoords = ProjectionInverseView * clipCoords;
    vec3 texCubeCoord = normalize(worldCoords.xyz / worldCoords.w);
    fragColor = texture(TextureSkybox, texCubeCoord);
}