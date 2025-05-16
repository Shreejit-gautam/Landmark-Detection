import SimpleITK as sitk
input_path = "Original_mask\left_knee.nii"
#Reading file
ct = sitk.ReadImage(input_path, sitk.sitkFloat32)
spacing = ct.GetSpacing()
print(f"Loaded CT — voxel spacing = {spacing} mm")