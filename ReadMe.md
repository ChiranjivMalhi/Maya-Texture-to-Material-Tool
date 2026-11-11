# Maya Texture-to-Material Tool

## Introduction

This Python script automates material setup in Autodesk Maya. It creates an Arnold `aiStandardSurface` material, identifies base color, metalness, roughness, and normal maps by their filenames, and connects them to the corresponding shader inputs.

I wrote this tool to speed up my texturing workflow by automating the manual process of creating and connecting shader nodes. The script can be adapted to support different naming conventions and additional texture maps.

## How to Use

1. Open Maya with Arnold enabled. Paste the script into the **Python** tab of the Script Editor and save it as a shelf button.
   
   <img width="974" height="513" alt="image" src="https://github.com/user-attachments/assets/69f2d6e9-cc3e-40ec-8f8a-984faf2528c8" />

2. Select the object you want to texture and click the tool’s shelf button.
   
   <img width="974" height="516" alt="image" src="https://github.com/user-attachments/assets/ae4354fd-edfb-4f4b-8f43-81a4da8a609f" />

3. In the file dialog, select your texture maps and click **Set**. Use filenames that end in `_BaseColor`, `_Metallic` or `_Metalness`, `_Roughness`, and `_Normal` before the file extension.
   
   <img width="974" height="518" alt="image" src="https://github.com/user-attachments/assets/c050c871-2064-45cf-9645-dc846ebe8dea" />

4. The script creates the `aiStandardSurface` material, connects the texture maps, and assigns the material to the selected object.
   
   <img width="974" height="519" alt="image" src="https://github.com/user-attachments/assets/36283196-92cc-42c0-b245-ffa35cf8e8a6" />

## Rendered Result
<img width="974" height="513" alt="image" src="https://github.com/user-attachments/assets/bdd9583e-8490-4732-81a9-74def7aa0b35" />

