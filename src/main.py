import SimpleITK as sitk
input_path = "Original_mask\left_knee.nii"
#Reading file
ct = sitk.ReadImage(input_path, sitk.sitkFloat32)