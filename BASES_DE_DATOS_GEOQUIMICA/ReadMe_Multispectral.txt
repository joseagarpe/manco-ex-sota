This file provides metadata to the raw multispectral image files.

TABLE OF CONTENTS
A. OVERVIEW
B. SPECIFICATIONS
C. DIRECTORY STRUCTURE
D. REFERENCES
E. DISCLAIMERS


A. OVERVIEW

The U.S. Geological Survey (USGS) deployed a 3D Robotics Solo multirotor small unoccupied aircraft system on June 21, 2018, to collect multispectral imagery data using a MicaSense RedEdge 3 camera at the USGS National Crude Oil Spill Fate and Natural Attenuation Research Site near Bemidji, Minnesota, USA. Imagery data were collected during surveys flown at two distinct heights above ground above areas of interest, approximately 200 feet and 400 feet above ground surface.

The RedEdge 3 collects simultaneous images in five spectral bands (blue, green, red, red edge, and near-infrared) and automatically georeferences the imagery with aircraft latitude, longitude, and altitude (Reference Frame: WGS84; Geoid: EGM96). The date, time, and location data are embedded within the metadata for each individual .tif file.

No ground control points were used during the field survey.


B. SPECIFICATIONS

Camera: MicaSense RedEdge 3
Focal Length: 5.5 mm
Resolution: 1280 x 960 pixels

Spectral Bands:
Band 1: Blue, center wavelength 475 nanometers, bandwidth  20 nanometers (FWHM, full width at half maximum)
Band 2: Green, center wavelength 560 nanometers, bandwidth  20 nanometers (FWHM, full width at half maximum)
Band 3: Red, center wavelength 668 nanometers, bandwidth  10 nanometers (FWHM, full width at half maximum)
Band 4: Near Infrared (IR), center wavelength 840 nanometers, bandwidth 40 nanometers (FWHM, full width at half maximum)
Band 5: Red Edge, Center Wavelength 717 nanometers, bandwidth 10 nanometers (FWHM, full width at half maximum)


C. DIRECTORY STRUCTURE
Multispectral data are divided into two compressed files, based on survey flight heights above ground (Multispectral_200ft-focusarea and Multispectral_400ft-focusarea). A survey may consist of one or more flights.

Each survey directory includes:

calibration-panel: Subdirectory with images of the RedEdge 3 calibration panel.

images: Subdirectory with original unprocessed imagery .tif data. Non-useful images such as during launch and landing were removed. The default RedEdge file names were pre-pended with the survey date (YYYYMMDD), site name, camera (MI for MicaSense RedEdge 3), and reference to the specific survey. Note that the final digit in the filename (prior to the file extension) is assigned by the camera and refers to the spectral band for that image.

AltText.csv: Comma separated values (CSV) file with two columns, FilePathAndName and AltText. Information for each .tif file is provided as a separate row. File is provided to meet Alt Text imagery accessibility requirements.


D. REFERENCES

3D Robotics, 2015, Solo User Manual V8, 73 p.

Delin, G.N., Essaid, H.I., Cozzarelli, I.M., Lahvis, M.H. and Bekins, B.A., 1998, Ground water contamination by crude oil near Bemidji, Minnesota, U.S. Geological Survey Fact Sheet 084-98, https://doi.org/10.3133/fs08498

MicaSense, 2015, MicaSense RedEdge 3 Multispectral Camera User Manual (Rev 06 – October 2015), 33 p, accessed online 11 May 2023 at https://support.micasense.com/hc/en-us/article_attachments/204648307/RedEdge_User_Manual_06.pdf


E. USGS DISCLAIMERS

Any use of trade, firm, or product names is for descriptive purposes only and does not imply endorsement by the U.S. Government.

Unless otherwise stated, all data, metadata and related materials are considered to satisfy the quality standards relative to the purpose for which the data were collected. Although these data and associated metadata have been reviewed for accuracy and completeness and approved for release by the U.S. Geological Survey (USGS), no warranty expressed or implied is made regarding the display or utility of the data for other purposes, nor on all computer systems, nor shall the act of distribution constitute any such warranty.


###
