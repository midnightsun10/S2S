#!/usr/bin/env python

import os
import sys
import numpy as np
sys.path.append('/home/brayan/mnsun/')
from utils import check_dir

levels = np.array([200,850])

MODELS = {"NCEP":{"reforecast":{"perturbed":{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,43.5+1,1),"M" : np.arange(1,3+1,1)}},
                                             "sfc_precip"           :{"tp"  :{"L1": np.arange(1,44+1,1)     ,"M" : np.arange(1,3+1,1)}},
                                             "sfc_temperature"      :{"wtmp":{"LB": np.arange(1.5,43.5+1,1),"M" : np.arange(1,3+1,1)}},
                                             "10m_above_ground"     :{"10u"   :{"L": np.arange(0,44+1,1)     ,"M" : np.arange(1,3+1,1)},
                                                                      "10v"   :{"L": np.arange(0,44+1,1)     ,"M" : np.arange(1,3+1,1)}
                                                                      },                                               
                                             "pressure_level_1"     :{"q"   :{"L": np.arange(0,44+1,1)     ,"M" : np.arange(1,3+1,1),"P2":levels}},
                                             "pressure_level_2"     :{
                                                                      "t"   :{"L": np.arange(0,44+1,1)     ,"M" : np.arange(1,3+1,1),"P":levels}
                                                                      },
                                             "pressure_level_wind"  :{"u"   :{"L": np.arange(0,44+1,1)     ,"M" : np.arange(1,3+1,1),"P":levels},
                                                                      "v"   :{"L": np.arange(0,44+1,1)     ,"M" : np.arange(1,3+1,1),"P":levels}
                                                                      },                                                            
                                             },
                                 "control"  :{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,43.5+1,1)}},
                                              "sfc_precip"           :{"tp"  :{"L1": np.arange(1,44+1,1)     }},
                                              "sfc_temperature"      :{"wtmp":{"LB": np.arange(1.5,43.5+1,1)}},
                                              "10m_above_ground"     :{"10u"   :{"L": np.arange(0,44+1,1)     },
                                                                       "10v"   :{"L": np.arange(0,44+1,1)     }
                                                                       },                                               
                                              "pressure_level_1"     :{"q"   :{"L": np.arange(0,44+1,1)     ,"P2":levels}},
                                              "pressure_level_2"     :{
                                                                       "t"   :{"L": np.arange(0,44+1,1)     ,"P":levels}
                                                                       },
                                              "pressure_level_wind"  :{"u"   :{"L": np.arange(0,44+1,1)     ,"P":levels},
                                                                       "v"   :{"L": np.arange(0,44+1,1)     ,"P":levels}
                                                                       },                                                            
                                              }
                                },
                 }
         }

key        = "235bb28ecdb1d4620a68fedd2ba95470c3b4f3387a8abce33ae0fdfe65ba7b4182af162d2e828423781997fec50e625e754d530f"
dataset    = [str(os.environ["dataset"])]
BASE       = "https://iridl.ldeo.columbia.edu/SOURCES/.ECMWF/.S2S/.{MODEL_NAME}/.{TYPE_SIMULATION}/.{TYPE_INIT}/.{VARIABLE_CATEGORY}/.{VARIABLE_SUBCATEGORY}"
OUTPUT_DIR = str(os.environ["output"]) #"/home/brayan/DATA/S2S/raw_data"
comm_line  = "curl -k -b '__dlauth_id="+key+"' '{URL}' > {PATHFILE}"

for model_name, v_1 in MODELS.items():
    dir_model = model_name.split("/")[0]+model_name.split("/")[-1] if model_name[:3] == "CMA" else model_name
    check_dir(OUTPUT_DIR, dir_model)
    with open(OUTPUT_DIR+f"/{dir_model}/{dir_model}_download.txt", "w") as f:
        for type_sim, v_2 in v_1.items():
            check_dir(OUTPUT_DIR+f"/{dir_model}", type_sim)
            for type_ini, v_3 in v_2.items():
                check_dir(OUTPUT_DIR+f"/{dir_model}/{type_sim}", type_ini)
                for var_cat, v_4 in v_3.items():
                    if var_cat not in dataset:
                        continue
                    for sub_cat, v_5 in v_4.items():
                        check_dir(OUTPUT_DIR+f"/{dir_model}/{type_sim}/{type_ini}", f"{var_cat}.{sub_cat}")
                        IRI_DES = BASE.format(
                                              MODEL_NAME=model_name, TYPE_SIMULATION=type_sim, 
                                              TYPE_INIT=type_ini, VARIABLE_CATEGORY=var_cat, VARIABLE_SUBCATEGORY=sub_cat
                                             )
                        des = list(v_5.keys())
                        for x,m in enumerate(v_5[des[0]]):  #number Lead
                            if 1 == len(des):
                                url      = IRI_DES + f"/{des[0]}/({str(m)})/VALUES/data.nc"
                                pathfile = OUTPUT_DIR+"/"+dir_model+"/"+type_sim+"/"+type_ini+"/"+f"{var_cat}.{sub_cat}"+"/"+ \
                                           f"{var_cat}_{sub_cat}"+"_"+des[0]+str(x)+".nc"
                                f.write(comm_line.format(URL = url, PATHFILE = pathfile)+ "\n") 

                            else:
                                for y,l in enumerate(v_5[des[1]]): #number M
                                    if 2 == len(des):
                                        url      = IRI_DES + f"/{des[0]}/({str(m)})/VALUES/{des[1]}/({str(l)})/VALUES/data.nc"
                                        pathfile = OUTPUT_DIR+"/"+dir_model+"/"+type_sim+"/"+type_ini+"/"+f"{var_cat}.{sub_cat}"+"/"+ \
                                                   f"{var_cat}_{sub_cat}"+"_"+des[0]+str(x)+"_"+des[1]+str(y)+".nc"
                                        f.write(comm_line.format(URL = url, PATHFILE = pathfile)+ "\n")     
                                    else:
                                        for z,p in enumerate(v_5[des[2]]):   #number P levels
                                            url      = IRI_DES + f"/{des[0]}/({str(m)})/VALUES/{des[1]}/({str(l)})/VALUES/{des[2]}/({p})/VALUES/data.nc"
                                            pathfile = OUTPUT_DIR+"/"+dir_model+"/"+type_sim+"/"+type_ini+"/"+f"{var_cat}.{sub_cat}"+"/"+ \
                                                       f"{var_cat}_{sub_cat}"+"_"+des[0]+str(x)+"_"+des[1]+str(y)+"_"+des[2]+str(z)+".nc"
                                            f.write(comm_line.format(URL = url, PATHFILE = pathfile)+ "\n")                                                                                                            

