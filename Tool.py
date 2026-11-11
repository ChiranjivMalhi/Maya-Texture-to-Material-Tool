selectedObject = cmds.ls(selection=True)
selected_textures = cmds.fileDialog2(fm=4, okc="Set")
textureMapping = {
"BaseColor": ".baseColor",
"Metallic": ".metalness",
"Metalness": ".metalness",
"Roughness": ".specularRoughness"
}
shaderName = selectedObject[0]
# Create Shader and SG Nodes
shader_node = cmds.shadingNode('aiStandardSurface', asShader=True,
name=shaderName + "_Material")
sg_node = cmds.sets(renderable=True, noSurfaceShader=True, empty=True,
name=shaderName + "SG")
# Connect Them
cmds.connectAttr('%s.outColor' % shader_node, '%s.surfaceShader' % sg_node)
# Loop through selected texture maps
for texture in selected_textures:
# Generate File Nodes
fileNode = cmds.shadingNode('file', name='fileTexture_' + shaderName +
'_' + texture, asTexture=True)
cmds.setAttr(fileNode + '.fileTextureName', texture, type="string")
# Detect Texture map type
textureType = texture.split("/")[-1].split("_")[-1].split(".")[0]
# Connect Nodes
if textureType == "Normal":
# Add Normal Map node
normalMapNode = cmds.shadingNode('aiNormalMap', asTexture=True)
cmds.connectAttr(fileNode + '.outColor', normalMapNode + ".input",
force=True)
cmds.connectAttr(normalMapNode + '.outValue', shader_node +
".normalCamera", force=True)
else:
outputMode = ".outColor" if textureType == "BaseColor" else ".outAlpha"
cmds.connectAttr(fileNode + outputMode, shader_node +
textureMapping[textureType], force=True)
# Set Material to selected element
cmds.select(selectedObject)
cmds.hyperShade(a=shader_node, assign=True)