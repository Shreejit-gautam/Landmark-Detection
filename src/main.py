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
cc = sitk.ConnectedComponent(bone_mask)
# Finding Two Largest components
relabeled = sitk.RelabelComponent(cc, sortByObjectSize=True)
two_largest = sitk.BinaryThreshold(relabeled, lowerThreshold=1, upperThreshold=2, insideValue=1, outsideValue=0)
n_after_cc = int(sitk.GetArrayViewFromImage(two_largest).sum())
print(f"After keeping 2 largest components: {n_after_cc:,} voxels")