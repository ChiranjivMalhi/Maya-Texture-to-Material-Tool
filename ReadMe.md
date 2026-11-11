Introduction

The purpose of this Python code is to apply texture maps to a selected object using the Arnold
Shader aiStandardSurface in Autodesk Maya. It automatically connects texture nodes for base
color, metalness, roughness, and normal maps to their corresponding attributes in the
aiStandardSurface shader. I wrote this code to improve efficiency in the 3D modeling and
texturing pipeline by automating the manual process of creating and connecting these nodes
individually. The code can be adjusted easily to handle different naming conventions and support
for other texture maps can be added as well.

Working
Add the script to the script editor and save it to the shelf.

Select an object and click on the node wrangler script icon on the shelf

A dialog box will appear. Select the texture maps with the appropriate naming convention and
click set.

The material aiStandardSurface will be made with the desired connections and it will be applied
to the selected object.

This would be the result after rendering.