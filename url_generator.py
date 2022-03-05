import os
import sys
import numpy as np
sys.path.append('/home/brayan/mnsun/')
from utils import check_dir

levels = ["200","850"]
MODELS = {"BOM":{"reforecast":{"perturbed":{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,61.5+1,1) ,"M" : np.arange(1,32+1,1)}},
                                            "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,61.5+1,1) ,"M" : np.arange(1,32+1,1)}},
                                            "sfc_precip"           :{"tp"  :{"L1": np.arange(1,62+1,1)     ,"M" : np.arange(1,32+1,1)}},
                                            "sfc_pressure"         :{"msl" :{"L1": np.arange(1,62+1,1)     ,"M" : np.arange(1,32+1,1)}},
                                            "sfc_temperature"      :{"wtmp":{"LA": np.arange(0.5,61.5+1,1) ,"M" : np.arange(1,32+1,1)}},
                                            "pressure_level_1"     :{"q"   :{"L1": np.arange(1,62+1,1)     ,"M" : np.arange(1,32+1,1),"P2":levels}},
                                            "pressure_level_2"     :{"gh"  :{"L1": np.arange(1,62+1,1)     ,"M" : np.arange(1,32+1,1),"P":levels},
                                                                     "t"   :{"L1": np.arange(1,62+1,1)     ,"M" : np.arange(1,32+1,1),"P":levels}
                                                                     },
                                            "pressure_level_wind"  :{"u"   :{"L1": np.arange(1,62+1,1)     ,"M" : np.arange(1,32+1,1),"P":levels},
                                                                     "v"   :{"L1": np.arange(1,62+1,1)     ,"M" : np.arange(1,32+1,1),"P":levels}
                                                                     },                                                            
                                            },
                               "control"  :{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,61.5+1,1)}},
                                            "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,61.5+1,1)}},
                                            "sfc_precip"           :{"tp"  :{"L1": np.arange(1,62+1,1)}},
                                            "sfc_pressure"         :{"msl" :{"L1": np.arange(1,62+1,1)}},
                                            "sfc_temperature"      :{"wtmp":{"LA": np.arange(0.5,61.5+1,1)}},
                                            "pressure_level_1"     :{"q"   :{"L1": np.arange(1,62+1,1),"P2":levels}},
                                            "pressure_level_2"     :{"gh"  :{"L1": np.arange(1,62+1,1),"P":levels},
                                                                     "t"   :{"L1": np.arange(1,62+1,1),"P":levels}
                                                                     },
                                            "pressure_level_wind"  :{"u"   :{"L1": np.arange(1,62+1,1),"P":levels},
                                                                     "v"   :{"L1": np.arange(1,62+1,1),"P":levels}
                                                                     },                                                            
                                            }
                              },
                 
                 "forecast"  :{"perturbed":{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,61.5+1,1) ,"M" : np.arange(1,32+1,1)}},
                                            "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,61.5+1,1) ,"M" : np.arange(1,32+1,1)}},
                                            "sfc_precip"           :{"tp"  :{"L1": np.arange(1,62+1,1)     ,"M" : np.arange(1,32+1,1)}},
                                            "sfc_pressure"         :{"msl" :{"L1": np.arange(1,62+1,1)     ,"M" : np.arange(1,32+1,1)}},
                                            "sfc_temperature"      :{"wtmp":{"LA": np.arange(0.5,61.5+1,1) ,"M" : np.arange(1,32+1,1)}},
                                            "pressure_level_1"     :{"q"   :{"L1": np.arange(1,62+1,1)     ,"M" : np.arange(1,32+1,1),"P2":levels}},
                                            "pressure_level_2"     :{"gh"  :{"L1": np.arange(1,62+1,1)     ,"M" : np.arange(1,32+1,1),"P":levels},
                                                                     "t"   :{"L1": np.arange(1,62+1,1)     ,"M" : np.arange(1,32+1,1),"P":levels}
                                                                     },
                                            "pressure_level_wind"  :{"u"   :{"L1": np.arange(1,62+1,1)     ,"M" : np.arange(1,32+1,1),"P":levels},
                                                                     "v"   :{"L1": np.arange(1,62+1,1)     ,"M" : np.arange(1,32+1,1),"P":levels}
                                                                     },                                                            
                                            },
                               "control"  :{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,61.5+1,1)}},
                                            "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,61.5+1,1)}},
                                            "sfc_precip"           :{"tp"  :{"L1": np.arange(1,62+1,1)}},
                                            "sfc_pressure"         :{"msl" :{"L1": np.arange(1,62+1,1)}},
                                            "sfc_temperature"      :{"wtmp":{"LA": np.arange(0.5,61.5+1,1)}},
                                            "pressure_level_1"     :{"q"   :{"L1": np.arange(1,62+1,1),"P2":levels}},
                                            "pressure_level_2"     :{"gh"  :{"L1": np.arange(1,62+1,1),"P":levels},
                                                                     "t"   :{"L1": np.arange(1,62+1,1),"P":levels}
                                                                     },
                                            "pressure_level_wind"  :{"u"   :{"L1": np.arange(1,62+1,1),"P":levels},
                                                                     "v"   :{"L1": np.arange(1,62+1,1),"P":levels}
                                                                     },                                                            
                                            }
                              },
                },         
          "CMA/.BCC-CPS-S2Sv1":{"reforecast":{"perturbed":{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,59.5+1,1),"M" : np.arange(1,3+1,1)}},
                                                           "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,59.5+1,1),"M" : np.arange(1,3+1,1)}},
                                                           "sfc_precip"           :{"tp"  :{"L1": np.arange(1,60+1,1)    ,"M" : np.arange(1,3+1,1)}},
                                                           "sfc_pressure"         :{"msl" :{"L": np.arange(0,60+1,1)     ,"M" : np.arange(1,3+1,1)}},
                                                           "sfc_temperature"      :{"wtmp":{"LA": np.arange(0.5,59.5+1,1),"M" : np.arange(1,3+1,1)}},
                                                           "10m_above_ground"     :{"10u"   :{"L": np.arange(0,60+1,1)     ,"M" : np.arange(1,3+1,1)},
                                                                                    "10v"   :{"L": np.arange(0,60+1,1)     ,"M" : np.arange(1,3+1,1)}
                                                                                    },                                               
                                                           "pressure_level_1"     :{"q"   :{"L": np.arange(0,62+1,1),"M" : np.arange(1,3+1,1),"P2":levels}},
                                                           "pressure_level_2"     :{"gh"  :{"L": np.arange(0,62+1,1),"M" : np.arange(1,3+1,1),"P":levels},
                                                                                    "t"   :{"L": np.arange(0,62+1,1),"M" : np.arange(1,3+1,1),"P":levels}
                                                                                    },
                                                           "pressure_level_wind"  :{"u"   :{"L": np.arange(0,60+1,1),"M" : np.arange(1,3+1,1),"P":levels},
                                                                                    "v"   :{"L": np.arange(0,60+1,1),"M" : np.arange(1,3+1,1),"P":levels}
                                                                                    },                                                            
                                                           },
                                              "control"  :{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,59.5+1,1)}},
                                                           "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,59.5+1,1)}},
                                                           "sfc_precip"           :{"tp"  :{"L1": np.arange(1,60+1,1)    }},
                                                           "sfc_pressure"         :{"msl" :{"L": np.arange(0,60+1,1)     }},
                                                           "sfc_temperature"      :{"wtmp":{"LA": np.arange(0.5,59.5+1,1)}},
                                                           "10m_above_ground"     :{"10u"   :{"L": np.arange(0,60+1,1)     },
                                                                                    "10v"   :{"L": np.arange(0,60+1,1)     }
                                                                                    },                                               
                                                           "pressure_level_1"     :{"q"   :{"L": np.arange(0,62+1,1),"P2":levels}},
                                                           "pressure_level_2"     :{"gh"  :{"L": np.arange(0,62+1,1),"P":levels},
                                                                                    "t"   :{"L": np.arange(0,62+1,1),"P":levels}
                                                                                    },
                                                           "pressure_level_wind"  :{"u"   :{"L": np.arange(0,60+1,1),"P":levels},
                                                                                    "v"   :{"L": np.arange(0,60+1,1),"P":levels}
                                                                                    },                                                            
                                                           }
                                             },

                                "forecast"  :{"perturbed":{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,59.5+1,1),"M" : np.arange(1,3+1,1)}},
                                                           "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,59.5+1,1),"M" : np.arange(1,3+1,1)}},
                                                           "sfc_precip"           :{"tp"  :{"L1": np.arange(1,60+1,1)    ,"M" : np.arange(1,3+1,1)}},
                                                           "sfc_pressure"         :{"msl" :{"L": np.arange(0,60+1,1)     ,"M" : np.arange(1,3+1,1)}},
                                                           "sfc_temperature"      :{"wtmp":{"LA": np.arange(0.5,59.5+1,1),"M" : np.arange(1,3+1,1)}},
                                                           "10m_above_ground"     :{"10u"   :{"L": np.arange(0,60+1,1)     ,"M" : np.arange(1,3+1,1)},
                                                                                    "10v"   :{"L": np.arange(0,60+1,1)     ,"M" : np.arange(1,3+1,1)}
                                                                                    },                                               
                                                           "pressure_level_1"     :{"q"   :{"L": np.arange(0,62+1,1),"M" : np.arange(1,3+1,1),"P2":levels}},
                                                           "pressure_level_2"     :{"gh"  :{"L": np.arange(0,62+1,1),"M" : np.arange(1,3+1,1),"P":levels},
                                                                                    "t"   :{"L": np.arange(0,62+1,1),"M" : np.arange(1,3+1,1),"P":levels}
                                                                                    },
                                                           "pressure_level_wind"  :{"u"   :{"L": np.arange(0,60+1,1),"M" : np.arange(1,3+1,1),"P":levels},
                                                                                    "v"   :{"L": np.arange(0,60+1,1),"M" : np.arange(1,3+1,1),"P":levels}
                                                                                    },                                                            
                                                           },
                                              "control"  :{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,59.5+1,1)}},
                                                           "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,59.5+1,1)}},
                                                           "sfc_precip"           :{"tp"  :{"L1": np.arange(1,60+1,1)    }},
                                                           "sfc_pressure"         :{"msl" :{"L": np.arange(0,60+1,1)     }},
                                                           "sfc_temperature"      :{"wtmp":{"LA": np.arange(0.5,59.5+1,1)}},
                                                           "10m_above_ground"     :{"10u"   :{"L": np.arange(0,60+1,1)     },
                                                                                    "10v"   :{"L": np.arange(0,60+1,1)     }
                                                                                    },                                               
                                                           "pressure_level_1"     :{"q"   :{"L": np.arange(0,62+1,1),"P2":levels}},
                                                           "pressure_level_2"     :{"gh"  :{"L": np.arange(0,62+1,1),"P":levels},
                                                                                    "t"   :{"L": np.arange(0,62+1,1),"P":levels}
                                                                                    },
                                                           "pressure_level_wind"  :{"u"   :{"L": np.arange(0,60+1,1),"P":levels},
                                                                                    "v"   :{"L": np.arange(0,60+1,1),"P":levels}
                                                                                    },                                                            
                                                           }
                                             }
                               },                   
          "CMA/.BCC-CPS-S2Sv2":{"reforecast":{"perturbed":{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,59.5+1,1),"M" : np.arange(1,3+1,1)}},
                                                           "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,59.5+1,1),"M" : np.arange(1,3+1,1)}},
                                                           "sfc_precip"           :{"tp"  :{"L1": np.arange(1,60+1,1)    ,"M" : np.arange(1,3+1,1)}},
                                                           "sfc_pressure"         :{"msl" :{"L": np.arange(0,60+1,1)     ,"M" : np.arange(1,3+1,1)}},
                                                           "sfc_temperature"      :{"wtmp":{"LA": np.arange(0.5,59.5+1,1),"M" : np.arange(1,3+1,1)}},
                                                           "10m_above_ground"     :{"10u"   :{"L": np.arange(0,60+1,1)     ,"M" : np.arange(1,3+1,1)},
                                                                                    "10v"   :{"L": np.arange(0,60+1,1)     ,"M" : np.arange(1,3+1,1)}
                                                                                    },                                               
                                                           "pressure_level_1"     :{"q"   :{"L": np.arange(0,62+1,1),"M" : np.arange(1,3+1,1),"P2":levels}},
                                                           "pressure_level_2"     :{"gh"  :{"L": np.arange(0,62+1,1),"M" : np.arange(1,3+1,1),"P":levels},
                                                                                    "t"   :{"L": np.arange(0,62+1,1),"M" : np.arange(1,3+1,1),"P":levels}
                                                                                    },
                                                           "pressure_level_wind"  :{"u"   :{"L": np.arange(0,60+1,1),"M" : np.arange(1,3+1,1),"P":levels},
                                                                                    "v"   :{"L": np.arange(0,60+1,1),"M" : np.arange(1,3+1,1),"P":levels}
                                                                                    },                                                            
                                                           },
                                              "control"  :{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,59.5+1,1)}},
                                                           "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,59.5+1,1)}},
                                                           "sfc_precip"           :{"tp"  :{"L1": np.arange(1,60+1,1)    }},
                                                           "sfc_pressure"         :{"msl" :{"L": np.arange(0,60+1,1)     }},
                                                           "sfc_temperature"      :{"wtmp":{"LA": np.arange(0.5,59.5+1,1)}},
                                                           "10m_above_ground"     :{"10u"   :{"L": np.arange(0,60+1,1)     },
                                                                                    "10v"   :{"L": np.arange(0,60+1,1)     }
                                                                                    },                                               
                                                           "pressure_level_1"     :{"q"   :{"L": np.arange(0,62+1,1),"P2":levels}},
                                                           "pressure_level_2"     :{"gh"  :{"L": np.arange(0,62+1,1),"P":levels},
                                                                                    "t"   :{"L": np.arange(0,62+1,1),"P":levels}
                                                                                    },
                                                           "pressure_level_wind"  :{"u"   :{"L": np.arange(0,60+1,1),"P":levels},
                                                                                    "v"   :{"L": np.arange(0,60+1,1),"P":levels}
                                                                                    },                                                            
                                                           }
                                             },

                                "forecast"  :{"perturbed":{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,59.5+1,1),"M" : np.arange(1,3+1,1)}},
                                                           "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,59.5+1,1),"M" : np.arange(1,3+1,1)}},
                                                           "sfc_precip"           :{"tp"  :{"L1": np.arange(1,60+1,1)    ,"M" : np.arange(1,3+1,1)}},
                                                           "sfc_pressure"         :{"msl" :{"L": np.arange(0,60+1,1)     ,"M" : np.arange(1,3+1,1)}},
                                                           "sfc_temperature"      :{"wtmp":{"LA": np.arange(0.5,59.5+1,1),"M" : np.arange(1,3+1,1)}},
                                                           "10m_above_ground"     :{"10u"   :{"L": np.arange(0,60+1,1)     ,"M" : np.arange(1,3+1,1)},
                                                                                    "10v"   :{"L": np.arange(0,60+1,1)     ,"M" : np.arange(1,3+1,1)}
                                                                                    },                                               
                                                           "pressure_level_1"     :{"q"   :{"L": np.arange(0,62+1,1),"M" : np.arange(1,3+1,1),"P2":levels}},
                                                           "pressure_level_2"     :{"gh"  :{"L": np.arange(0,62+1,1),"M" : np.arange(1,3+1,1),"P":levels},
                                                                                    "t"   :{"L": np.arange(0,62+1,1),"M" : np.arange(1,3+1,1),"P":levels}
                                                                                    },
                                                           "pressure_level_wind"  :{"u"   :{"L": np.arange(0,60+1,1),"M" : np.arange(1,3+1,1),"P":levels},
                                                                                    "v"   :{"L": np.arange(0,60+1,1),"M" : np.arange(1,3+1,1),"P":levels}
                                                                                    },                                                            
                                                           },
                                              "control"  :{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,59.5+1,1)}},
                                                           "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,59.5+1,1)}},
                                                           "sfc_precip"           :{"tp"  :{"L1": np.arange(1,60+1,1)    }},
                                                           "sfc_pressure"         :{"msl" :{"L": np.arange(0,60+1,1)     }},
                                                           "sfc_temperature"      :{"wtmp":{"LA": np.arange(0.5,59.5+1,1)}},
                                                           "10m_above_ground"     :{"10u"   :{"L": np.arange(0,60+1,1)     },
                                                                                    "10v"   :{"L": np.arange(0,60+1,1)     }
                                                                                    },                                               
                                                           "pressure_level_1"     :{"q"   :{"L": np.arange(0,62+1,1),"P2":levels}},
                                                           "pressure_level_2"     :{"gh"  :{"L": np.arange(0,62+1,1),"P":levels},
                                                                                    "t"   :{"L": np.arange(0,62+1,1),"P":levels}
                                                                                    },
                                                           "pressure_level_wind"  :{"u"   :{"L": np.arange(0,60+1,1),"P":levels},
                                                                                    "v"   :{"L": np.arange(0,60+1,1),"P":levels}
                                                                                    },                                                            
                                                           }
                                             }
                               },   
          "CNRM":{"reforecast":{"perturbed":{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,60.5+1,1),"M" : np.arange(1,14+1,1)}},
                                             "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,60.5+1,1),"M" : np.arange(1,14+1,1)}},
                                             "sfc_precip"           :{"tp"  :{"L1": np.arange(1,61+1,1)    ,"M" : np.arange(1,14+1,1)}},
                                             "sfc_pressure"         :{"msl" :{"L": np.arange(0,61+1,1)     ,"M" : np.arange(1,14+1,1)}},
                                             "sfc_temperature"      :{"wtmp":{"LA": np.arange(0.5,60.5+1,1),"M" : np.arange(1,14+1,1)}},
                                             "10m_above_ground"     :{"10u"   :{"L": np.arange(0,61+1,1)     ,"M" : np.arange(1,14+1,1)},
                                                                      "10v"   :{"L": np.arange(0,61+1,1)     ,"M" : np.arange(1,14+1,1)}
                                                                      },                                               
                                             "pressure_level_1"     :{"q"   :{"L": np.arange(0,61+1,1),"M" : np.arange(1,14+1,1),"P2":levels}},
                                             "pressure_level_2"     :{"gh"  :{"L": np.arange(0,61+1,1),"M" : np.arange(1,14+1,1),"P":levels},
                                                                      "t"   :{"L": np.arange(0,61+1,1),"M" : np.arange(1,14+1,1),"P":levels}
                                                                      },
                                             "pressure_level_wind"  :{"u"   :{"L": np.arange(0,61+1,1),"M" : np.arange(1,14+1,1),"P":levels},
                                                                      "v"   :{"L": np.arange(0,61+1,1),"M" : np.arange(1,14+1,1),"P":levels}
                                                                      },                                                            
                                             },
                                "control"  :{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,60.5+1,1)}},
                                             "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,60.5+1,1)}},
                                             "sfc_precip"           :{"tp"  :{"L1": np.arange(1,61+1,1)    }},
                                             "sfc_pressure"         :{"msl" :{"L": np.arange(0,61+1,1)     }},
                                             "sfc_temperature"      :{"wtmp":{"LA": np.arange(0.5,60.5+1,1)}},
                                             "10m_above_ground"     :{"10u"   :{"L": np.arange(0,61+1,1)     },
                                                                      "10v"   :{"L": np.arange(0,61+1,1)     }
                                                                      },                                               
                                             "pressure_level_1"     :{"q"   :{"L": np.arange(0,61+1,1),"P2":levels}},
                                             "pressure_level_2"     :{"gh"  :{"L": np.arange(0,61+1,1),"P":levels},
                                                                      "t"   :{"L": np.arange(0,61+1,1),"P":levels}
                                                                      },
                                             "pressure_level_wind"  :{"u"   :{"L": np.arange(0,61+1,1),"P":levels},
                                                                      "v"   :{"L": np.arange(0,61+1,1),"P":levels}
                                                                      },                                                            
                                             }
                               },
                  "forecast"  :{"perturbed":{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,31.5+1,1),"M" : np.arange(1,50+1,1)}},
                                             "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,31.5+1,1),"M" : np.arange(1,50+1,1)}},
                                             "sfc_precip"           :{"tp"  :{"L1": np.arange(1,32+1,1)    ,"M" : np.arange(1,50+1,1)}},
                                             "sfc_pressure"         :{"msl" :{"L": np.arange(0,32+1,1)     ,"M" : np.arange(1,50+1,1)}},
                                             "sfc_temperature"      :{"wtmp":{"LA": np.arange(0.5,31.5+1,1),"M" : np.arange(1,50+1,1)}},
                                             "10m_above_ground"     :{"10u"   :{"L": np.arange(0,32+1,1)     ,"M" : np.arange(1,50+1,1)},
                                                                      "10v"   :{"L": np.arange(0,32+1,1)     ,"M" : np.arange(1,50+1,1)}
                                                                      },                                               
                                             "pressure_level_1"     :{"q"   :{"L": np.arange(0,32+1,1),"M" : np.arange(1,50+1,1),"P2":levels}},
                                             "pressure_level_2"     :{"gh"  :{"L": np.arange(0,32+1,1),"M" : np.arange(1,50+1,1),"P":levels},
                                                                      "t"   :{"L": np.arange(0,32+1,1),"M" : np.arange(1,50+1,1),"P":levels}
                                                                      },
                                             "pressure_level_wind"  :{"u"   :{"L": np.arange(0,32+1,1),"M" : np.arange(1,50+1,1),"P":levels},
                                                                      "v"   :{"L": np.arange(0,32+1,1),"M" : np.arange(1,50+1,1),"P":levels}
                                                                      },                                                            
                                             },
                                "control"  :{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,31.5+1,1)}},
                                             "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,31.5+1,1)}},
                                             "sfc_precip"           :{"tp"  :{"L1": np.arange(1,32+1,1)    }},
                                             "sfc_pressure"         :{"msl" :{"L": np.arange(0,32+1,1)     }},
                                             "sfc_temperature"      :{"wtmp":{"LA": np.arange(0.5,31.5+1,1)}},
                                             "10m_above_ground"     :{"10u"   :{"L": np.arange(0,32+1,1)     },
                                                                      "10v"   :{"L": np.arange(0,32+1,1)     }
                                                                      },                                               
                                             "pressure_level_1"     :{"q"   :{"L": np.arange(0,32+1,1),"P2":levels}},
                                             "pressure_level_2"     :{"gh"  :{"L": np.arange(0,32+1,1),"P":levels},
                                                                      "t"   :{"L": np.arange(0,32+1,1),"P":levels}
                                                                      },
                                             "pressure_level_wind"  :{"u"   :{"L": np.arange(0,32+1,1),"P":levels},
                                                                      "v"   :{"L": np.arange(0,32+1,1),"P":levels}
                                                                      },                                                            
                                             }
                               }
                 },        
          "ISAC":{"reforecast":{"control"  :{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,30.5+1,1)}},
                                             "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,30.5+1,1)}},
                                             "sfc_precip"           :{"tp"  :{"L": np.arange(0,31+1,1)    }},
                                             "sfc_pressure"         :{"msl" :{"L": np.arange(0,31+1,1)     }},
                                             "sfc_temperature"      :{"wtmp":{"LA": np.arange(0.5,30.5+1,1)}},
                                             "10m_above_ground"     :{"10u"   :{"L": np.arange(0,31+1,1)     },
                                                                      "10v"   :{"L": np.arange(0,31+1,1)     }
                                                                      },                                               
                                             "pressure_level_2"     :{"gh"  :{"L": np.arange(0,31+1,1),"P":levels},
                                                                      "t"   :{"L": np.arange(0,31+1,1),"P":levels}
                                                                      },
                                             "pressure_level_wind"  :{"u"   :{"L": np.arange(0,31+1,1),"P":levels},
                                                                      "v"   :{"L": np.arange(0,31+1,1),"P":levels}
                                                                      },                                                            
                                             }
                               },
                  "forecast"  :{"perturbed":{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,30.5+1,1),"M" : np.arange(1,40+1,1)}},
                                             "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,30.5+1,1),"M" : np.arange(1,40+1,1)}},
                                             "sfc_precip"           :{"tp"  :{"L": np.arange(0,31+1,1)    ,"M" : np.arange(1,40+1,1)}},
                                             "sfc_pressure"         :{"msl" :{"L": np.arange(0,31+1,1)     ,"M" : np.arange(1,40+1,1)}},
                                             "sfc_temperature"      :{"wtmp":{"LA": np.arange(0.5,30.5+1,1),"M" : np.arange(1,40+1,1)}},
                                             "10m_above_ground"     :{"10u"   :{"L": np.arange(0,31+1,1)     ,"M" : np.arange(1,40+1,1)},
                                                                      "10v"   :{"L": np.arange(0,31+1,1)     ,"M" : np.arange(1,40+1,1)}
                                                                      },                                               
                                             "pressure_level_2"     :{"gh"  :{"L": np.arange(0,31+1,1),"M" : np.arange(1,40+1,1),"P":levels},
                                                                      "t"   :{"L": np.arange(0,31+1,1),"M" : np.arange(1,40+1,1),"P":levels}
                                                                      },
                                             "pressure_level_wind"  :{"u"   :{"L": np.arange(0,31+1,1),"M" : np.arange(1,40+1,1),"P":levels},
                                                                      "v"   :{"L": np.arange(0,31+1,1),"M" : np.arange(1,40+1,1),"P":levels}
                                                                      },                                                            
                                             },
                                "control"  :{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,30.5+1,1),"M" : np.arange(1,40+1,1)}},
                                             "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,30.5+1,1),"M" : np.arange(1,40+1,1)}},
                                             "sfc_precip"           :{"tp"  :{"L": np.arange(0,31+1,1)    ,"M" : np.arange(1,40+1,1)}},
                                             "sfc_pressure"         :{"msl" :{"L": np.arange(0,31+1,1)     ,"M" : np.arange(1,40+1,1)}},
                                             "sfc_temperature"      :{"wtmp":{"LA": np.arange(0.5,30.5+1,1),"M" : np.arange(1,40+1,1)}},
                                             "10m_above_ground"     :{"10u"   :{"L": np.arange(0,31+1,1)     ,"M" : np.arange(1,40+1,1)},
                                                                      "10v"   :{"L": np.arange(0,31+1,1)     ,"M" : np.arange(1,40+1,1)}
                                                                      },                                               
                                             "pressure_level_2"     :{"gh"  :{"L": np.arange(0,31+1,1),"M" : np.arange(1,40+1,1),"P":levels},
                                                                      "t"   :{"L": np.arange(0,31+1,1),"M" : np.arange(1,40+1,1),"P":levels}
                                                                      },
                                             "pressure_level_wind"  :{"u"   :{"L": np.arange(0,31+1,1),"M" : np.arange(1,40+1,1),"P":levels},
                                                                      "v"   :{"L": np.arange(0,31+1,1),"M" : np.arange(1,40+1,1),"P":levels}
                                                                      },                                                            
                                             }
                               }
                 },           
          "JMA":{"reforecast":{"perturbed":{"2m_above_ground"      :{"2t"  :{"LA": np.arange(1,33+1,1)    ,"M" : np.arange(1,4+1,1)}},
                                            "atmos_column"         :{"tcc" :{"LA": np.arange(1,33+1,1)    ,"M" : np.arange(1,4+1,1)}},
                                            "sfc_precip"           :{"tp"  :{"L": np.arange(0.5,32.5+1,1) ,"M" : np.arange(1,4+1,1)}},
                                            "sfc_pressure"         :{"msl" :{"L": np.arange(0.5,32.5+1,1) ,"M" : np.arange(1,4+1,1)}},
                                            "sfc_temperature"      :{"wtmp":{"LA": np.arange(1,33+1,1)    ,"M" : np.arange(1,4+1,1)}},
                                            "10m_above_ground"     :{"10u"   :{"L": np.arange(0.5,32.5+1,1) ,"M" : np.arange(1,4+1,1)},
                                                                     "10v"   :{"L": np.arange(0.5,32.5+1,1) ,"M" : np.arange(1,4+1,1)}
                                                                     },                                               
                                            "pressure_level_1"     :{"q"   :{"L": np.arange(0.5,32.5+1,1),"M" : np.arange(1,4+1,1),"P2":levels}},
                                            "pressure_level_2"     :{"gh"  :{"L": np.arange(0.5,32.5+1,1),"M" : np.arange(1,4+1,1),"P":levels},
                                                                     "t"   :{"L": np.arange(0.5,32.5+1,1),"M" : np.arange(1,4+1,1),"P":levels}
                                                                     },
                                            "pressure_level_wind"  :{"u"   :{"L": np.arange(0.5,32.5+1,1),"M" : np.arange(1,4+1,1),"P":levels},
                                                                     "v"   :{"L": np.arange(0.5,32.5+1,1),"M" : np.arange(1,4+1,1),"P":levels}
                                                                     },                                                            
                                            },
                                "control"  :{"2m_above_ground"      :{"2t"  :{"LA": np.arange(1,33+1,1)}},
                                             "atmos_column"         :{"tcc" :{"LA": np.arange(1,33+1,1)}},
                                             "sfc_precip"           :{"tp"  :{"L": np.arange(0.5,32.5+1,1)    }},
                                             "sfc_pressure"         :{"msl" :{"L": np.arange(0.5,32.5+1,1)     }},
                                             "sfc_temperature"      :{"wtmp":{"LA": np.arange(1,33+1,1)}},
                                             "10m_above_ground"     :{"10u"   :{"L": np.arange(0.5,32.5+1,1)     },
                                                                      "10v"   :{"L": np.arange(0.5,32.5+1,1)     }
                                                                      },                                               
                                             "pressure_level_1"     :{"q"   :{"L": np.arange(0.5,32.5+1,1),"P2":levels}},
                                             "pressure_level_2"     :{"gh"  :{"L": np.arange(0.5,32.5+1,1),"P":levels},
                                                                      "t"   :{"L": np.arange(0.5,32.5+1,1),"P":levels}
                                                                      },
                                             "pressure_level_wind"  :{"u"   :{"L": np.arange(0.5,32.5+1,1),"P":levels},
                                                                      "v"   :{"L": np.arange(0.5,32.5+1,1),"P":levels}
                                                                      },                                                            
                                             }
                               },
                  "forecast"  :{"perturbed":{"2m_above_ground"      :{"2t"  :{"LA": np.arange(1,33+1,1)    ,"M" : np.arange(1,24+1,1)}},
                                             "atmos_column"         :{"tcc" :{"LA": np.arange(1,33+1,1)    ,"M" : np.arange(1,24+1,1)}},
                                             "sfc_precip"           :{"tp"  :{"L": np.arange(0.5,32.5+1,1) ,"M" : np.arange(1,24+1,1)}},
                                             "sfc_pressure"         :{"msl" :{"L": np.arange(0.5,32.5+1,1) ,"M" : np.arange(1,24+1,1)}},
                                             "sfc_temperature"      :{"wtmp":{"LA": np.arange(1,33+1,1)    ,"M" : np.arange(1,24+1,1)}},
                                             "10m_above_ground"     :{"10u"   :{"L": np.arange(0.5,32.5+1,1) ,"M" : np.arange(1,24+1,1)},
                                                                      "10v"   :{"L": np.arange(0.5,32.5+1,1) ,"M" : np.arange(1,24+1,1)}
                                                                      },                                               
                                             "pressure_level_1"     :{"q"   :{"L": np.arange(0.5,32.5+1,1),"M" : np.arange(1,24+1,1),"P2":levels}},
                                             "pressure_level_2"     :{"gh"  :{"L": np.arange(0.5,32.5+1,1),"M" : np.arange(1,24+1,1),"P":levels},
                                                                      "t"   :{"L": np.arange(0.5,32.5+1,1),"M" : np.arange(1,24+1,1),"P":levels}
                                                                      },
                                             "pressure_level_wind"  :{"u"   :{"L": np.arange(0.5,32.5+1,1),"M" : np.arange(1,24+1,1),"P":levels},
                                                                      "v"   :{"L": np.arange(0.5,32.5+1,1),"M" : np.arange(1,24+1,1),"P":levels}
                                                                      },                                                            
                                             },
                                "control"  :{"2m_above_ground"      :{"2t"  :{"LA": np.arange(1,33+1,1)}},
                                             "atmos_column"         :{"tcc" :{"LA": np.arange(1,33+1,1)}},
                                             "sfc_precip"           :{"tp"  :{"L": np.arange(0.5,32.5+1,1)    }},
                                             "sfc_pressure"         :{"msl" :{"L": np.arange(0.5,32.5+1,1)     }},
                                             "sfc_temperature"      :{"wtmp":{"LA": np.arange(1,33+1,1)}},
                                             "10m_above_ground"     :{"10u"   :{"L": np.arange(0.5,32.5+1,1)     },
                                                                      "10v"   :{"L": np.arange(0.5,32.5+1,1)     }
                                                                      },                                               
                                             "pressure_level_1"     :{"q"   :{"L": np.arange(0.5,32.5+1,1),"P2":levels}},
                                             "pressure_level_2"     :{"gh"  :{"L": np.arange(0.5,32.5+1,1),"P":levels},
                                                                      "t"   :{"L": np.arange(0.5,32.5+1,1),"P":levels}
                                                                      },
                                             "pressure_level_wind"  :{"u"   :{"L": np.arange(0.5,32.5+1,1),"P":levels},
                                                                      "v"   :{"L": np.arange(0.5,32.5+1,1),"P":levels}
                                                                      },                                                            
                                             }
                               }
                 },          
          "KMA":{"reforecast":{"perturbed":{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,59.5+1,1)    ,"M" : np.arange(1,3+1,1)}},
                                            "sfc_precip"           :{"tp"  :{"L1": np.arange(1,60+1,1) ,"M" : np.arange(1,3+1,1)}},
                                            "sfc_pressure"         :{"msl" :{"L1": np.arange(1,60+1,1) ,"M" : np.arange(1,3+1,1)}},
                                            "10m_above_ground"     :{"10u"   :{"L1": np.arange(1,60+1,1) ,"M" : np.arange(1,3+1,1)},
                                                                     "10v"   :{"L1": np.arange(1,60+1,1) ,"M" : np.arange(1,3+1,1)}
                                                                     },                                               
                                            "pressure_level_2"     :{"gh"  :{"L": np.arange(0,60+1,1),"M" : np.arange(1,3+1,1),"P":levels},
                                                                     "t"   :{"L": np.arange(0,60+1,1),"M" : np.arange(1,3+1,1),"P":levels}
                                                                     },
                                            "pressure_level_wind"  :{"u"   :{"L": np.arange(0,60+1,1),"M" : np.arange(1,3+1,1),"P":levels},
                                                                     "v"   :{"L": np.arange(0,60+1,1),"M" : np.arange(1,3+1,1),"P":levels}
                                                                     },                                                            
                                            },
                                "control"  :{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,59.5+1,1) }},
                                            "sfc_precip"           :{"tp"  :{"L1": np.arange(1,60+1,1) }},
                                            "sfc_pressure"         :{"msl" :{"L1": np.arange(1,60+1,1) }},
                                            "10m_above_ground"     :{"10u"   :{"L1": np.arange(1,60+1,1) },
                                                                     "10v"   :{"L1": np.arange(1,60+1,1) }
                                                                     },                                               
                                            "pressure_level_2"     :{"gh"  :{"L": np.arange(0,60+1,1),"P":levels },
                                                                     "t"   :{"L": np.arange(0,60+1,1),"P":levels }
                                                                     },
                                            "pressure_level_wind"  :{"u"   :{"L": np.arange(0,60+1,1),"P":levels},
                                                                     "v"   :{"L": np.arange(0,60+1,1),"P":levels}
                                                                     },                                                            
                                            }
                               },
                  "forecast"  :{"perturbed":{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,59.5+1,1)    ,"M" : np.arange(1,3+1,1)}},
                                            "sfc_precip"           :{"tp"  :{"L1": np.arange(1,60+1,1) ,"M" : np.arange(1,3+1,1)}},
                                            "sfc_pressure"         :{"msl" :{"L1": np.arange(1,60+1,1) ,"M" : np.arange(1,3+1,1)}},
                                            "10m_above_ground"     :{"10u"   :{"L1": np.arange(1,60+1,1) ,"M" : np.arange(1,3+1,1)},
                                                                     "10v"   :{"L1": np.arange(1,60+1,1) ,"M" : np.arange(1,3+1,1)}
                                                                     },                                               
                                            "pressure_level_2"     :{"gh"  :{"L": np.arange(0,60+1,1),"M" : np.arange(1,3+1,1),"P":levels},
                                                                     "t"   :{"L": np.arange(0,60+1,1),"M" : np.arange(1,3+1,1),"P":levels}
                                                                     },
                                            "pressure_level_wind"  :{"u"   :{"L": np.arange(0,60+1,1),"M" : np.arange(1,3+1,1),"P":levels},
                                                                     "v"   :{"L": np.arange(0,60+1,1),"M" : np.arange(1,3+1,1),"P":levels}
                                                                     },                                                            
                                            },
                                "control"  :{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,59.5+1,1) }},
                                            "sfc_precip"           :{"tp"  :{"L1": np.arange(1,60+1,1) }},
                                            "sfc_pressure"         :{"msl" :{"L1": np.arange(1,60+1,1) }},
                                            "10m_above_ground"     :{"10u"   :{"L1": np.arange(1,60+1,1) },
                                                                     "10v"   :{"L1": np.arange(1,60+1,1) }
                                                                     },                                               
                                            "pressure_level_2"     :{"gh"  :{"L": np.arange(0,60+1,1),"P":levels },
                                                                     "t"   :{"L": np.arange(0,60+1,1),"P":levels }
                                                                     },
                                            "pressure_level_wind"  :{"u"   :{"L": np.arange(0,60+1,1),"P":levels},
                                                                     "v"   :{"L": np.arange(0,60+1,1),"P":levels}
                                                                     },                                                            
                                            }
                               }
                 },              
          "NCEP":{"reforecast":{"perturbed":{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,43.5+1,1),"M" : np.arange(1,3+1,1)}},
                                             "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,43.5+1,1),"M" : np.arange(1,3+1,1)}},
                                             "sfc_precip"           :{"tp"  :{"L1": np.arange(1,44+1,1)     ,"M" : np.arange(1,3+1,1)}},
                                             "sfc_pressure"         :{"msl" :{"L": np.arange(0,44+1,1)     ,"M" : np.arange(1,3+1,1)}},
                                             "sfc_temperature"      :{"wtmp":{"LB": np.arange(1.5,43.5+1,1),"M" : np.arange(1,3+1,1)}},
                                             "10m_above_ground"     :{"10u"   :{"L": np.arange(0,44+1,1)     ,"M" : np.arange(1,3+1,1)},
                                                                      "10v"   :{"L": np.arange(0,44+1,1)     ,"M" : np.arange(1,3+1,1)}
                                                                      },                                               
                                             "pressure_level_1"     :{"q"   :{"L": np.arange(0,44+1,1)     ,"M" : np.arange(1,3+1,1),"P2":levels}},
                                             "pressure_level_2"     :{"gh"  :{"L": np.arange(0,44+1,1)     ,"M" : np.arange(1,3+1,1),"P":levels},
                                                                      "t"   :{"L": np.arange(0,44+1,1)     ,"M" : np.arange(1,3+1,1),"P":levels}
                                                                      },
                                             "pressure_level_wind"  :{"u"   :{"L": np.arange(0,44+1,1)     ,"M" : np.arange(1,3+1,1),"P":levels},
                                                                      "v"   :{"L": np.arange(0,44+1,1)     ,"M" : np.arange(1,3+1,1),"P":levels}
                                                                      },                                                            
                                             },
                                 "control"  :{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,43.5+1,1)}},
                                              "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,43.5+1,1)}},
                                              "sfc_precip"           :{"tp"  :{"L1": np.arange(1,44+1,1)     }},
                                              "sfc_pressure"         :{"msl" :{"L": np.arange(0,44+1,1)     }},
                                              "sfc_temperature"      :{"wtmp":{"LB": np.arange(1.5,43.5+1,1)}},
                                              "10m_above_ground"     :{"10u"   :{"L": np.arange(0,44+1,1)     },
                                                                       "10v"   :{"L": np.arange(0,44+1,1)     }
                                                                       },                                               
                                              "pressure_level_1"     :{"q"   :{"L": np.arange(0,44+1,1)     ,"P2":levels}},
                                              "pressure_level_2"     :{"gh"  :{"L": np.arange(0,44+1,1)     ,"P":levels},
                                                                       "t"   :{"L": np.arange(0,44+1,1)     ,"P":levels}
                                                                       },
                                              "pressure_level_wind"  :{"u"   :{"L": np.arange(0,44+1,1)     ,"P":levels},
                                                                       "v"   :{"L": np.arange(0,44+1,1)     ,"P":levels}
                                                                       },                                                            
                                              }
                                },
                  "forecast"  :{"perturbed":{"2m_above_ground"      :{"2t"  :{"LB": np.arange(1.5,43.5+1,1),"M" : np.arange(1,15+1,1)}},
                                             "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,43.5+1,1),"M" : np.arange(1,15+1,1)}},
                                             "sfc_precip"           :{"tp"  :{"L1": np.arange(1,44+1,1)    ,"M" : np.arange(1,15+1,1)}},
                                             "sfc_pressure"         :{"msl" :{"L": np.arange(0,44+1,1)     ,"M" : np.arange(1,15+1,1)}},
                                             "sfc_temperature"      :{"wtmp":{"LB": np.arange(1.5,43.5+1,1),"M" : np.arange(1,15+1,1)}},
                                             "10m_above_ground"     :{"10u"   :{"L1": np.arange(1,44+1,1)    ,"M" : np.arange(1,15+1,1)},
                                                                      "10v"   :{"L1": np.arange(1,44+1,1)    ,"M" : np.arange(1,15+1,1)}
                                                                      },                                               
                                             "pressure_level_1"     :{"q"   :{"L": np.arange(0,44+1,1)     ,"M" : np.arange(1,15+1,1),"P2":levels}},
                                             "pressure_level_2"     :{"gh"  :{"L": np.arange(0,44+1,1)     ,"M" : np.arange(1,15+1,1),"P":levels},
                                                                      "t"   :{"L": np.arange(0,44+1,1)     ,"M" : np.arange(1,15+1,1),"P":levels}
                                                                      },
                                             "pressure_level_wind"  :{"u"   :{"L": np.arange(0,44+1,1)     ,"M" : np.arange(1,15+1,1),"P":levels},
                                                                      "v"   :{"L": np.arange(0,44+1,1)     ,"M" : np.arange(1,15+1,1),"P":levels}
                                                                      },                                                            
                                             },
                                 "control"  :{"2m_above_ground"      :{"2t"  :{"LA": np.arange(0.5,43.5+1,1)}},
                                              "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,43.5+1,1)}},
                                              "sfc_precip"           :{"tp"  :{"L1": np.arange(1,44+1,1)     }},
                                              "sfc_pressure"         :{"msl" :{"L": np.arange(0,44+1,1)     }},
                                              "sfc_temperature"      :{"wtmp":{"LB": np.arange(1.5,43.5+1,1)}},
                                              "10m_above_ground"     :{"10u"   :{"L": np.arange(0,44+1,1)     },
                                                                       "10v"   :{"L": np.arange(0,44+1,1)     }
                                                                       },                                               
                                              "pressure_level_1"     :{"q"   :{"L": np.arange(0,44+1,1)     ,"P2":levels}},
                                              "pressure_level_2"     :{"gh"  :{"L": np.arange(0,44+1,1)     ,"P":levels},
                                                                       "t"   :{"L": np.arange(0,44+1,1)     ,"P":levels}
                                                                       },
                                              "pressure_level_wind"  :{"u"   :{"L": np.arange(0,44+1,1)     ,"P":levels},
                                                                       "v"   :{"L": np.arange(0,44+1,1)     ,"P":levels}
                                                                       },                                                            
                                              }
                                }
                 },      
          "UKMO":{"reforecast":{"perturbed":{"1p5m_above_ground"    :{"2t"  :{"LA": np.arange(0.5,59.5+1,1),"M" : np.arange(1,3+1,1)}},
                                             "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,59.5+1,1),"M" : np.arange(1,3+1,1)}},
                                             "sfc_precip"           :{"tp"  :{"L1": np.arange(1,60+1,1)    ,"M" : np.arange(1,3+1,1)}},
                                             "sfc_pressure"         :{"msl" :{"L": np.arange(0,60+1,1)     ,"M" : np.arange(1,3+1,1)}},
                                             "sfc_temperature"      :{"wtmp":{"LA": np.arange(0.5,59.5+1,1),"M" : np.arange(1,3+1,1)}},
                                             "10m_above_ground"     :{"10u"   :{"L1": np.arange(1,60+1,1)    ,"M" : np.arange(1,3+1,1)},
                                                                      "10v"   :{"L1": np.arange(1,60+1,1)    ,"M" : np.arange(1,3+1,1)}
                                                                      },                                               
                                             "pressure_level_1"     :{"q"   :{"L": np.arange(0,60+1,1)     ,"M" : np.arange(1,3+1,1),"P2":levels}},
                                             "pressure_level_2"     :{"gh"  :{"L": np.arange(0,60+1,1)     ,"M" : np.arange(1,3+1,1),"P":levels},
                                                                      "t"   :{"L": np.arange(0,60+1,1)     ,"M" : np.arange(1,3+1,1),"P":levels}
                                                                      },
                                             "pressure_level_wind"  :{"u"   :{"L": np.arange(0,60+1,1)     ,"M" : np.arange(1,3+1,1),"P":levels},
                                                                      "v"   :{"L": np.arange(0,60+1,1)     ,"M" : np.arange(1,3+1,1),"P":levels}
                                                                      },                                                            
                                             },
                                "control"  :{"1p5m_above_ground"    :{"2t"  :{"LA": np.arange(0.5,59.5+1,1)}},
                                             "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,59.5+1,1)}},
                                             "sfc_precip"           :{"tp"  :{"L1": np.arange(1,60+1,1)    }},
                                             "sfc_pressure"         :{"msl" :{"L": np.arange(0,60+1,1)     }},
                                             "sfc_temperature"      :{"wtmp":{"LA": np.arange(0.5,59.5+1,1)}},
                                             "10m_above_ground"     :{"10u"   :{"L1": np.arange(1,60+1,1)    },
                                                                      "10v"   :{"L1": np.arange(1,60+1,1)    }
                                                                      },                                               
                                             "pressure_level_1"     :{"q"   :{"L": np.arange(0,60+1,1)     ,"P2":levels}},
                                             "pressure_level_2"     :{"gh"  :{"L": np.arange(0,60+1,1)     ,"P":levels},
                                                                      "t"   :{"L": np.arange(0,60+1,1)     ,"P":levels}
                                                                      },
                                             "pressure_level_wind"  :{"u"   :{"L": np.arange(0,60+1,1)     ,"P":levels},
                                                                      "v"   :{"L": np.arange(0,60+1,1)     ,"P":levels}
                                                                      },                                                            
                                             }
                               },
                  "forecast"  :{"perturbed":{"1p5m_above_ground"    :{"2t"  :{"LA": np.arange(0.5,59.5+1,1),"M" : np.arange(1,3+1,1)}},
                                             "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,59.5+1,1),"M" : np.arange(1,3+1,1)}},
                                             "sfc_precip"           :{"tp"  :{"L1": np.arange(1,60+1,1)    ,"M" : np.arange(1,3+1,1)}},
                                             "sfc_pressure"         :{"msl" :{"L": np.arange(0,60+1,1)     ,"M" : np.arange(1,3+1,1)}},
                                             "sfc_temperature"      :{"wtmp":{"LA": np.arange(0.5,59.5+1,1),"M" : np.arange(1,3+1,1)}},
                                             "10m_above_ground"     :{"10u"   :{"L1": np.arange(1,60+1,1)    ,"M" : np.arange(1,3+1,1)},
                                                                      "10v"   :{"L1": np.arange(1,60+1,1)    ,"M" : np.arange(1,3+1,1)}
                                                                      },                                               
                                             "pressure_level_1"     :{"q"   :{"L": np.arange(0,60+1,1)     ,"M" : np.arange(1,3+1,1),"P2":levels}},
                                             "pressure_level_2"     :{"gh"  :{"L": np.arange(0,60+1,1)     ,"M" : np.arange(1,3+1,1),"P":levels},
                                                                      "t"   :{"L": np.arange(0,60+1,1)     ,"M" : np.arange(1,3+1,1),"P":levels}
                                                                      },
                                             "pressure_level_wind"  :{"u"   :{"L": np.arange(0,60+1,1)     ,"M" : np.arange(1,3+1,1),"P":levels},
                                                                      "v"   :{"L": np.arange(0,60+1,1)     ,"M" : np.arange(1,3+1,1),"P":levels}
                                                                      },                                                            
                                             },
                                "control"  :{"1p5m_above_ground"    :{"2t"  :{"LA": np.arange(0.5,59.5+1,1)}},
                                             "atmos_column"         :{"tcc" :{"LA": np.arange(0.5,59.5+1,1)}},
                                             "sfc_precip"           :{"tp"  :{"L1": np.arange(1,60+1,1)    }},
                                             "sfc_pressure"         :{"msl" :{"L": np.arange(0,60+1,1)     }},
                                             "sfc_temperature"      :{"wtmp":{"LA": np.arange(0.5,59.5+1,1)}},
                                             "10m_above_ground"     :{"10u"   :{"L1": np.arange(1,60+1,1)    },
                                                                      "10v"   :{"L1": np.arange(1,60+1,1)    }
                                                                      },                                               
                                             "pressure_level_1"     :{"q"   :{"L": np.arange(0,60+1,1)     ,"P2":levels}},
                                             "pressure_level_2"     :{"gh"  :{"L": np.arange(0,60+1,1)     ,"P":levels},
                                                                      "t"   :{"L": np.arange(0,60+1,1)     ,"P":levels}
                                                                      },
                                             "pressure_level_wind"  :{"u"   :{"L": np.arange(0,60+1,1)     ,"P":levels},
                                                                      "v"   :{"L": np.arange(0,60+1,1)     ,"P":levels}
                                                                      },                                                            
                                             }
                               }
                 },                    
         }

key        = "8ce7889cae88571d734728da60220887b54e6fe6b34b0c69d103cf5d15a5dfb46efad7aba040f67308d612df7d10d63a2be93915"
dataset    = ["10m_above_ground"]
BASE       = "https://iridl.ldeo.columbia.edu/SOURCES/.ECMWF/.S2S/.{MODEL_NAME}/.{TYPE_SIMULATION}/.{TYPE_INIT}/.{VARIABLE_CATEGORY}/.{VARIABLE_SUBCATEGORY}"
OUTPUT_DIR = "/media/brayan/DATA/S2S/raw_data"
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
                            if 2 == len(des):
                                for y,l in enumerate(v_5[des[1]]): #number M
                                    if 3 == len(des):
                                        for z,p in enumerate(v_5[des[2]]):   #number P levels
                                            url      = IRI_DES + f"/{des[0]}/({str(m)})/VALUES/{des[1]}/({str(l)})/VALUES/{des[2]}/({p})/VALUES/data.nc"
                                            pathfile = OUTPUT_DIR+"/"+dir_model+"/"+type_sim+"/"+type_ini+"/"+f"{var_cat}.{sub_cat}"+"/"+ \
                                                       f"{var_cat}_{sub_cat}"+"_"+des[0]+str(x)+"_"+des[1]+str(y)+"_"+des[2]+str(z)+".nc"
                                            f.write(comm_line.format(URL = url, PATHFILE = pathfile)+ "\n")
                                    else:
                                        url      = IRI_DES + f"/{des[0]}/({str(m)})/VALUES/{des[1]}/({str(l)})/VALUES/data.nc"
                                        pathfile = OUTPUT_DIR+"/"+dir_model+"/"+type_sim+"/"+type_ini+"/"+f"{var_cat}.{sub_cat}"+"/"+ \
                                                   f"{var_cat}_{sub_cat}"+"_"+des[0]+str(x)+"_"+des[1]+str(y)+".nc"
                                        f.write(comm_line.format(URL = url, PATHFILE = pathfile)+ "\n")                                        
                            else:
                                url      = IRI_DES + f"/{des[0]}/({str(m)})/VALUES/data.nc"
                                pathfile = OUTPUT_DIR+"/"+dir_model+"/"+type_sim+"/"+type_ini+"/"+f"{var_cat}.{sub_cat}"+"/"+ \
                                           f"{var_cat}_{sub_cat}"+"_"+des[0]+str(x)+".nc"
                                f.write(comm_line.format(URL = url, PATHFILE = pathfile)+ "\n")                                                 

