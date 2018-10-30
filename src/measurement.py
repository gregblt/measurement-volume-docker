import json
import nibabel as nib
import numpy as np
import sys
import os

def print_volume(roi,img,voxel_vol):
	mask= img == int(roi['label']) 
	masked_cc = np.ma.array(img, mask=np.logical_not(mask),fill_value = 0)
	vol=len(masked_cc.compressed())*voxel_vol
	print("volume:",vol," mm3 in roi",roi["roi"])
	return {"roi":roi["roi"],"value":vol,"measurement_type":"Volume","unit":"mm3"}

label_vol_path=sys.argv[1]
lut_path=sys.argv[2]

try:
	os.mkdir("output")
except:
	pass

lut=[]
meas=[]

with open(lut_path, 'r') as f: 
	lut=json.load(f)

# Load mask
cc_parc_img = nib.load(label_vol_path)
cc_parc_data = cc_parc_img.get_data()
# Arrange the array to be in RAS+ space
ornt=nib.orientations.axcodes2ornt(nib.aff2axcodes(cc_parc_img.affine))
cc_parc_data=nib.orientations.apply_orientation(cc_parc_data, ornt)

vxl_size=cc_parc_img.get_header().get_zooms()

for roi in lut:
	meas.append(print_volume(roi,cc_parc_data,vxl_size[0]*vxl_size[1]*vxl_size[2]))

with open('output/measurement.json', 'w') as f: 
	json.dump(meas,f,indent=4, separators=(',', ': '))

