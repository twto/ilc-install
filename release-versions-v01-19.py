###########################################
#
# iLCSoft versions for installing a current HEAD
# version of the ilcsoft packages.
# The external base tools need to be installed
#
# DESY ilcsoft team
###########################################
import datetime

# --------- ilcsoft release version ------------------------------------------
ilcsoft_release='v01-19-05'
# ----------------------------------------------------------------------------

#-----------------------
# we now always build with c++11 ?
use_cpp11 = True


#===============================================================================
# use a compiler that knows c++11, run
#
# before starting the installation
#================================================================================



# --------- install dir ------------------------------------------------------
# ===========================================================
# Modify this path to where you want to install the software
# ===========================================================
#

#ilcsoft_install_prefix = ilcsoft_afs_path[ arch ]
#ilcsoft_install_prefix = "/cvmfs/ilc.desy.de/sw/x86_64_gcc48_sl6/"
ilcsoft_install_prefix = "/ilcsoft/"

# ----------------------------------------------------------------------------
#--- the ilcsoft_release is now automatically appended in release-ilcsoft.cfg
#     but not in release-base.cfg !!

#append_version_to_install_prefix = False
#if(append_version_to_install_prefix):
#    ilcsoft_install_dir = os.path.join(ilcsoft_install_prefix , ilcsoft_release )

# ----------------------------------------------------------------------------


# --------- ilcsoft home -----------------------------------------------------
# ===========================================================
# Modify this path to where you want ilcinstall to look
# for pre-installed (base) packages
# typically this would be left to ilcsoft_install_prefix
# or set to an /afs or /cvmfs base installation that you
# want to use
# ===========================================================

ilcPath = ilcsoft_install_prefix
# ----------------------------------------------------------------------------


#--------------------------------------------------------------------------
#ilcPatchPath = "/afs/desy.de/project/ilcsoft/sw/x86_64_gcc41_sl5/v01-15"



# ======================= PACKAGES WITH NO INSTALL SUPPORT ===================

# these packages need to be pre-installed for your system
# please adjust the path variables accordingly

# ----- mysql --------------------------------------------------------
MySQL_version = "5.7.21"
#MySQL_path = ilcPath + "/mysql/" + MySQL_version

#if( ilcsoft_afs_path[ arch ].find('_ub') > 0 ):
MySQL_path = "/usr"


#------ boost headers files ------------------------------------------
#Boost_path = ilcPath+"/../boost/1.58.0"
Boost_path = "/usr"

#------ Eigen headers files ------------------------------------------
#Eigen_path =  ilcPath+"/../Eigen/3.2.9"
Eigen_path =  "/usr"

##########################################################################################
#
#  end of user configuration section
#  only make changes below if you know what you are doing ...
#
##########################################################################################


# ======================= PACKAGE VERSIONS ===================================

#Geant4_version =  "10.02.p02"
#CLHEP_version =  "2.3.1.1"

Geant4_version =  "10.03.p02"
CLHEP_version =  "2.3.4.3"

#ROOT_version = "6.08.06"
ROOT_version = "6.12.04"

GSL_version = "2.1"

QT_version = "5.9.4"

CMake_version = "3.6.3"

FastJet_version = "3.2.0"

FastJetcontrib_version = "1.024"

CED_version = "v01-09-02"
# -------------------------------------------

LCIO_version = "v02-11"

GEAR_version = "v01-07"

CondDBMySQL_version = "CondDBMySQL_ILC-0-9-6"

ILCUTIL_version = "v01-03"

MarlinFastJet_version = "v00-05"


# -------------------------------------------

KalTest_version = "v02-03"

KalDet_version = "v01-14"

aidaTT_version = "v00-08"

DDKalTest_version = "v01-04"

MarlinTrk_version = "v02-06"

MarlinTrkProcessors_version = "v02-09-01"

Clupatra_version = "v01-02"

KiTrack_version = "v01-08"

KiTrackMarlin_version = "v01-11"

FCalClusterer_version = "v00-06"

ForwardTracking_version = "v01-13"

ConformalTracking_version = "v01-04"

LICH_version = "v00-01"

# -------------------------------------------

GBL_version = "V02-01-01" #"V02-00-00"

LCCD_version = "v01-04"

RAIDA_version = "v01-08"

MarlinUtil_version = "v01-14"

Marlin_version = "v01-15-02"

MarlinDD4hep_version = "v00-05"

MarlinReco_version = "v01-22"

ILDPerformance_version = "v01-04"
ClicPerformance_version = "v02-00-00" # "v00-01"
#ILDConfig_version = "HEAD"


LCFIVertex_version = "v00-07-04"
LCFIPlus_version = "v00-06-07"


MarlinKinfit_version = "v00-05"
MarlinKinfitProcessors_version = "v00-03"

PandoraPFANew_version   = "v03-06-00"
DDMarlinPandora_version = "v00-09-01"
PandoraAnalysis_version = "v02-00-00"

CEDViewer_version = "v01-15"

Overlay_version = "v00-20"

PathFinder_version = "v00-06-01"

MarlinTPC_version = "v01-03"

LCTuple_version = "v01-10"

BBQ_version = "v00-01-03"

Druid_version = "2.2"

Garlic_version = "v3.0.4"

DD4hep_version = "v01-05"
DD4hepExamples_version = "v01-05"

lcgeo_version = "v00-15-03"

Physsim_version = "v00-04"


# xerces-c (needed by geant4 for building gdml support - required by mokka)
XERCESC_ROOT_DIR = ilcPath + "/xercesc/3.2.0"

XercesC_version = "3.2.0"
