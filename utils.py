# helpful functions for quickstart notebook

def subtypes_19B():
    ## 19B: 20748 & 20754
    a19B = [648518346514102494,648518346486521220,648518346494714101,648518346478566484,648518346493928590,648518346470397694,648518346490917155,648518346504054568,648518346489701849]
    
    b19B = [648518346472404745,648518346479754484,648518346479342290,648518346487572459,648518346480778973,648518346483219108,648518346477884397,648518346483217060,648518346475327073,648518346488672497,648518346472234034,648518346531249690,648518346494550071,648518346494010144,648518346491866991,648518346489713715,648518346511922879,648518346495649680,648518346491071521,648518346489473477,648518346502350931,648518346483215780,648518346489477829,648518346491922827,648518346517260837,648518346491631377,648518346491785583,648518346499962623,648518346489680844,648518346496520316,648518346491967762,648518346512598430,648518346486115682,648518346489339225,648518346495703696,648518346511177781,648518346489936858,648518346509978918,648518346496601602,648518346500367797,648518346492959152,648518346524103941,648518346491545662,648518346517386564,648518346488723185,648518346494015776,648518346504389868,648518346501803882,648518346465002357,648518346526162391,648518346496084029,648518346517372458,648518346495238070,648518346494726315,648518346489629783,648518346493076032,648518346494104311,648518346504760454,648518346496711396,648518346498000794,648518346493976889,648518346491604648,648518346492086316,648518346489731379,648518346501084950,648518346493750264,648518346500054534,648518346483664559,648518346494543927,648518346503917152,648518346502313043,648518346480970330]
    return [a19B, b19B]


def NT_labels(premotor_df):
    ## add neurotransmitter info to premotor df
    ## From Lacin et. al., 2019
    GABA_list = ['11B', '0A', '6A', '3B', '5B', '19A', '6B', '12B', '13B', '13A','9A','1B']
    Glu_list = ['2A', '16B', '8A', '21A', '14A', '24B_'] #'15B', 
    ACh_list = ['17A', '12A', '8B', '19B', '11A', '7B', '23B', '18B', '1A', '20A', '4B', '3A', '22A','10B','PSI']
    
    premotor_df['sign'] = 'unknown'
    premotor_df.loc[premotor_df['cell_type'].isin(GABA_list), 'sign'] = 'inh'
    premotor_df.loc[premotor_df['cell_type'].isin(Glu_list), 'sign'] = 'inh'
    premotor_df.loc[premotor_df['cell_type'].isin(ACh_list), 'sign'] = 'exc'
    premotor_df.loc[premotor_df['classification_system'].isin(['sensory']), 'sign'] = 'exc'
    
    return premotor_df

def make_json(seg_ids, hidden_ids):
    formatted_ids = [str(x) for x in seg_ids]
    formatted_hidden_ids = [str(x) for x in hidden_ids]
    state = {
    "layers": [
     {
       "source": "precomputed://gs://lee-lab_female-adult-nerve-cord/alignmentV4/em/rechunked",
       "type": "image",
       "blend": "default",
       "shaderControls": {},
       "name": "FANC EM"
     },
     {
       "type": "segmentation",
       "mesh": "graphene://https://cave.fanc-fly.com/segmentation/table/mar2021_prod",
       "selectedAlpha": 0.4,
       "colorSeed": 3788587020,
       "segments": formatted_ids,
       "hiddenSegments": formatted_hidden_ids,
       "skeletonRendering": {
         "mode2d": "lines_and_points",
         "mode3d": "lines"
       },
       "name": "3d reconstructions"
     },
     {
       "type": "segmentation",
       "mesh": "precomputed://gs://lee-lab_female-adult-nerve-cord/alignmentV4/volume_meshes/meshes",
       "objectAlpha": 0.1,
       "hideSegmentZero": False,
       "ignoreSegmentInteractions": True,
       "segmentColors": {
         "1": "#bfbfbf",
         "2": "#d343d6"
       },
       "segments": [
         "1",
         "2"
       ],
       "skeletonRendering": {
         "mode2d": "lines_and_points",
         "mode3d": "lines"
       },
       "name": "region outlines"
     }
   ],
   "navigation": {
     "pose": {
       "position": {
         "voxelSize": [
           4.300000190734863,
           4.300000190734863,
           45
         ],
         "voxelCoordinates": [38734, 148426, 2200
         ]
       }
     },
     "zoomFactor": 12
   },
   "showAxisLines": False,
   "showDefaultAnnotations": False,
   "perspectiveZoom": 6062.41070084089,
   "showSlices": False,
   "gpuMemoryLimit": 4000000000,
   "systemMemoryLimit": 4000000000,
   "concurrentDownloads": 64,
   "jsonStateServer": "https://global.daf-apis.com/nglstate/api/v1/post",
   "selectedLayer": {
     "layer": "published FANC neurons",
     "visible": True
   },
   "layout": "xy-3d"
     }
    return state
