Publication containing results from models in this model archive:
---------------------------
Warren, Ean, and Bekins, B. A., 2018, Relative Contributions of Microbial 
and Infrastructure Heat at a Crude Oil-Contaminated Site: Journal of 
Contaminant Hydrology, vol. 211, April 2018, p. 94-103, 
https://doi.org/10.1016/j.jconhyd.2018.03.011

Model archive:
---------------------
Warren, Ean, and Bekins, B. A., 2018, SUTRA model simulations used to evaluate 
heat flow from microbial activity at a crude oil-contaminated site, 
https://doi.org/10.5066/F7N58KKX 
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
   12/10/2017 Model archive created to conform to the structure specified
              for public release of groundwater flow and transport models.
   01/11/2018 Model archive update based on Hedeff Essaid's review of model
              archive.
   04/17/2018 Model archive update with final information for Warren2018_JCH

-------------------------------------------------------------------------------

    Warren2018_JCH/
        Description: 
        -----------
        The underlying folders contain all of the input and output files for 
the simulations described in the journal article and the modified version of 
SUTRA (v 2.2) source code and executable used to run the model simulations. The
modified code allows for spatially-variable thermal properties and density and 
viscosity variation with temperature.
        
        Descriptions of the data in each subfolder are given to facilitate 
understanding of this model archive. File descriptions are provided for
select files to provide additional information that may be of use for
understanding this data model archive. 
              
        Support is provided for correcting errors in the data release and 
clarification of the modeling conducted by the U.S. Geological Survey. Users
are encouraged to review the complete manuscript of Warren and Bekins (2018) 
(https://doi.org/10.1016/j.jconhyd.2018.03.011) to understand the purpose, 
construction, and limitations of this model.

        Reconstructing the data release from the online data release:
        -------------------------------------------------------------
        This data release is available from:

            https://doi.org/10.5066/F7N58KKX

        The models will run successfully only if the original folder 
structure is correctly restored. Otherwise, the SUTRA executable can be
placed in the same folder as the input files for it to run properly. The data
release is compressed to reduce download time and storage.

        The highest-level folder structure of the original data release is:

            Warren2018_JCH\
                \ancillary\
                \bin\
                \georef\
                \model\
                \output\
                \source\

        To reconstruct the data release on the user's computer running the 
Windows operating system:

        The models will run successfully only if the original directory 
structure is correctly restored. The data release is broken into several pieces
to reduce the likelihood of download timeouts. Small files (readme.txt and 
modelgeoref.txt) are available as uncompressed files. All other files are 
zipped at the subdirectory level. For example, the files in the "georef"
subdirectory are zipped into a zip file named "georef.zip". All zip files 
should be unzipped into a directory with the same name as the zip file name 
without the .zip extension. 

    The full folder structure of the data release and the compressed files 
associated with each subfolder are listed below.                  

        System requirements:
        --------------------

        The models contained in this data release were run using the 
sutra_2_2_EW.exe executable in the bin\ folder in this data release. 
sutra_2_2_EW.exe was compiled using the Microsoft Visual Studio 2010 
development environment (10.0.30319.1) and the Intel Visual Fortran Composer
XE 2013 SP1 Update 1 (14.0.1.139) on a 64-bit Windows 8 operating system.

        Each model requires approximately 50 MB of available Random Access 
Memory (RAM) while running.

        The models have been run successfully on computers running the 64-bit 
Windows 8 and 10 Enterprise operating systems.


        Running the model(s):
        ---------------------

        The simulations can be run by double clicking the batch file:

            RUNSUTRA.bat

        in the subfolder of model\ that contains the input files of interest. 
This will open a command line (terminal) window and execute the model found
in bin\. 

        For example, for the model2 simulation go to the model\model2\ 
subfolder and double-click: 

            RUNSUTRA.bat

        to run the model2 scenario simulation. 

        The output from the simulation will be created in the same subfolder 
containing the input files. For example, model2 scenario simulation results
are saved to the model\model2 subfolder. These files can be compared to the
output files given in the output\output.model2 subfolder.

        Files: 
        -----
        readme.txt : This file documents the structure, directories and 
files, and instructions on how to run the model for this data release.
        modelgeoref.txt : ASCII file with the four corners of the model domain.


        ancillary\

            Description and Content: 
            -----------
            This folder contains the documentation to run modified SUTRA 2.2
simulations and a listing of modifications to the SUTRA 2.2 code that allows 
for spatially-variable thermal properties and density and viscosity variation 
with temperature. The modified version no longer accepts SUTRA 2.2 input files.
For these files to work, .inp input files must be modified to remove the
"#Start_inp11B" field by inserting a "#" before each line.


            Filename                Contents
            --------------          ----------
            DataDescriptions.txt    Descriptions of data and how the data were 
                                    used in Warren and Bekins (2018)
            ModelDescriptions.txt   File of descriptions of model runs and 
                                    where results were used in Warren and 
                                    Bekins (2018)
            Notes_SUTRA_2_2.pdf     Release notes for SUTRA 2.2

            DataArchive\

                Description and Content: 
                -----------
                This folder includes files with all annual average 
temperature data that were compared to model output. The locations of the 
observation sites are shown in Figures 1 and 5b of Warren and Bekins (2018).

                Filename                            Contents
                --------------                      ----------
                DataArchiveBackupGroundwater.csv    Average annual groundwater 
                                                    temperatures at 0.5 m  and 
                                                    4.0 m below water table. 
                DataArchiveBackupBkgd1Unsat.csv     Average annual unsaturated 
                                                    zone temperatures at Bkgd1
                DataArchiveBackupBkgd2Unsat.csv     Average annual unsaturated 
                                                    zone temperatures at Bkgd2
                DataArchiveBackupOil1Unsat.csv      Average annual unsaturated 
                                                    zone temperatures at Oil1
                DataArchiveBackupOil2Unsat.csv      Average annual unsaturated 
                                                    zone temperatures at Oil2


        bin\

            Description: 
            -----------
            A modified SUTRA (v 2.2) executable file used to run the 
scenarios documented in  Warren and Bekins (2018) 
(https://doi.org/10.1016/j.jconhyd.2018.03.011). The modifications were to 
allow for spatially-variable thermal properties and density and viscosity 
variation with temperature. The executable was compiled for the 64-bit Windows
8 Operating System. 


        georef\

            Description: 
            -----------
            This folder contains a shapefile showing the land-surface trace of 
the two vertical cross-sectional model domains documented in Warren and Bekins 
(2018) (https://doi.org/10.1016/j.jconhyd.2018.03.011) .


        model\

            Description: 
            -----------
            This folder contains 12 subfolders corresponding to the 2 
simulated background and contaminated model scenarios plus simulations to 
examine parameter sensitivity and the contributions of each heat source. Each 
subfolder contains all of the model scenario input files necessary to run the 
simulation. The filenames are specific for that simulation. Input parameters 
are described in ancillary\Notes_SUTRA_2_2.pdf. 
        The files in the subdirectories are:

        .ics                  Initial conditions
        .inp                  Main input
        Observationkey.txt    Empty file
        RUNSUTRA.BAT          Batch file to run simulation
        SUTRA.FIL             File assignments
        usgs.model.reference  ASCII text file containing data to register the
                              model in space and time

            Filename        Model subfolder     Scenario
            --------------  ------------------  ----------
            CasePO-170912h  model\model1\       Background case with pipelines 
                                                set to 24 °C
            Case-170912k    model\model2\       Base contaminated case
            Case-171127a    model\model3\       Base contaminated case with 
                                                1e-11 m2 permeability
            Case-171127b    model\model4\       Base contaminated case with 
                                                1e-10 m2 permeability
            Case-170912l    model\model5\       Base contaminated case with 
                                                microbial heating only
            Case-170912m    model\model6\       Base contaminated case with 
                                                methane oxidation heating only
            Case-170912n    model\model7\       Base contaminated case with 
                                                iron-reducing heating only
            Case-170912o    model\model8\       Base contaminated model space 
                                                before pipelines
            Case-170912p    model\model9\       Base contaminated model space 
                                                before pipelines without 
                                                geothermal heating
            Case-170912q    model\model10\      Base contaminated case without 
                                                microbial heating
            Case-170922a    model\model11\      Base contaminated case with 1/2
                                                recharge in lower elevation 
                                                area
            Case-170922b   model\model12\       Base contaminated case with 50%
                                                more recharge in lower elevation 
                                                area


        output\

            Description: 
            -----------
            This folder contains 12 subfolders corresponding to the 2 
simulated background and contaminated model scenarios plus simulations to 
examine parameter sensitivity and the contributions of each heat source. The 
filenames are specific for that simulation. Details of output file types can be
found in the SUTRA 2.2 release notes in ancillary\Notes_SUTRA_2_2.pdf. The file
extensions are:

        .ele    Elementwise results
        .lst    Main results listing
        .nod    Nodewise results
        .obs    Observation results
        .rst    Restart file
        .smy    Simulation summary or file assignment errors

            Filename        Output subfolder        Scenario
            --------------  ------------------      ----------
            CasePO-170912h  output\output.model1\   Background case with 
                                                    pipelines set to 24 °C
            Case-170912k    output\output.model2\   Base contaminated case
            Case-171127a    output\output.model3\   Base contaminated case with
                                                    1e-11 m2 permeability
            Case-171127b    output\output.model4\   Base contaminated case with
                                                    1e-10 m2 permeability
            Case-170912l    output\output.model5\   Base contaminated case with
                                                    microbial heating only
            Case-170912m    output\output.model6\   Base contaminated case with
                                                    methane oxidation heating 
                                                    only
            Case-170912n    output\output.model7\   Base contaminated case with
                                                    iron-reducing heating only
            Case-170912o    output\output.model8\   Base contaminated model 
                                                    space before pipelines
            Case-170912p    output\output.model9\   Base contaminated model 
                                                    space before pipelines 
                                                    without geothermal heating
            Case-170912q    output\output.model10\  Base contaminated case 
                                                    without microbial heating
            Case-170922a    output\output.model11\  Base contaminated case with
                                                    1/2 recharge in lower 
                                                    elevation area
            Case-170922b    output\output.model12\  Base contaminated case with
                                                    50% more recharge in lower 
                                                    elevation area


        source\

            Description: 
            -----------
            Modified Fortran source files for SUTRA (v 2.2) under SUTRA\ 
subfolder. The modifications were to allow for spatially-variable thermal 
properties and density and viscosity variation with temperature. Lines of code 
that were changed from published source code are marked with "Ean". The release
notes for SUTRA 2.2 are found in ancillary\ subfolder. A listing of the 
modifications to SUTRA 2.2 code can be found in code_changes.txt in this 
folder.

Disclaimers
------------

Unless otherwise stated, all data, metadata and related materials are 
considered to satisfy the quality standards relative to the purpose for which 
the data were collected. Although these data and associated metadata have 
been reviewed for accuracy and completeness and approved for release by the 
U.S. Geological Survey (USGS), no warranty expressed or implied is made 
regarding the display or utility of the data for other purposes, nor on all 
computer systems, nor shall the act of distribution constitute any such 
warranty.

Any use of trade, firm, or product names is for descriptive purposes only and 
does not imply endorsement by the U.S. Government.

This software has been approved for release by the U.S. Geological Survey 
(USGS). Although the software has been subjected to rigorous review, the USGS 
reserves the right to update the software as needed pursuant to further 
analysis and review. No warranty, expressed or implied, is made by the USGS 
or the U.S. Government as to the functionality of the software and related 
material nor shall the fact of release constitute any such warranty. 
Furthermore, the software is released on condition that neither the USGS nor 
the U.S. Government shall be held liable for any damages resulting from its 
authorized or unauthorized use.

Although these data have been processed successfully on a computer system at 
the U.S. Geological Survey (USGS), no warranty expressed or implied is made 
regarding the display or utility of the data for other purposes, nor on all 
computer systems, nor shall the act of distribution constitute any such 
warranty. The USGS or the U.S. Government shall not be held liable for 
improper or incorrect use of the data described and/or contained herein.