import SimpleITK as sitk
input_path = "Original_mask\left_knee.nii"
#Reading file
ct = sitk.ReadImage(input_path, sitk.sitkFloat32)
spacing = ct.GetSpacing()
print(f"Loaded CT — voxel spacing = {spacing} mm")
bone_mask = sitk.BinaryThreshold(
    ct,
    lowerThreshold=300,
    upperThreshold=10000,       # >> any plausible HU
    insideValue=1,
    outsideValue=0
)

n_voxels = int(sitk.GetArrayViewFromImage(bone_mask).sum())
print(f"Thresholded mask contains {n_voxels:,} voxels")