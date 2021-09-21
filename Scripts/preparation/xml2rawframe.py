import argparse
from glob import glob
import xmltodict
import json
import os
from tqdm import tqdm
from copy import deepcopy
import shutil

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert the annotations to the COCO format')
    parser.add_argument('--dataset_directory', type=str)
    parser.add_argument('--output_directory', type=str)
    config = parser.parse_args()
    
    labels = {'RuleBreak': {'WrongLane', 'WrongTurn', 'TrafficLight'}, 'LaneChanging': {'True'}, 'OverTaking': {'True'}, 'Yield': {'True'}, 'Cutting': {'True'}, 'LaneChanging(m)': {'True'}}
    labels_mapping = {'RuleBreak': 0, 'LaneChanging': 1, 'OverTaking': 2, 'Yield': 3, 'Cutting': 4, 'LaneChanging(m)': 1}
    bad_videos = []
    scene_counter = 1

    dataset_directory = config.dataset_directory
    output_directory = config.output_directory

    bad_vid = False

    scene_frames = []
    annotations = set() 

    for directory in tqdm(glob(dataset_directory + '/*/')):
        if bad_vid:
            bad_vid = False
            bad_videos.append(directory)
            continue

        if len(scene_frames) != 0:
            if len(annotations) > 0:
                path = os.path.join(output_directory + '/Scenes', '{0:06d}'.format(scene_counter))
                os.mkdir(path)
                for i, frame in enumerate(scene_frames):
                    shutil.copy(file[:-3] + 'JPG', output_directory + '/Scenes/{0:06d}/'.format(scene_counter) + 'img_{0:05d}.jpg'.format(i+1))
                with open(output_directory + '/annotations.txt', 'a') as f:
                    ann = [str(s) for s in annotations]
                    ann.sort()
                    ann_string = " ".join(ann)
                    print(output_directory + '/Scenes/{0:06d}'.format(scene_counter) + ' ' + str(len(scene_frames)) + ' ' + ann_string, file=f)

                scene_counter += 1
            scene_frames = []
            annotations = set()  

        for file in sorted(glob(directory + 'Annotations/*.xml')):
            if os.stat(file).st_size == 0:
                bad_vid = True
                break

            with open(file) as fd:
                doc = xmltodict.parse(fd.read())['annotation']

                if 'object' not in doc:
                    bad_vid = True
                    break

                if not isinstance(doc['object'], list):
                    obj = doc['object']

                    if obj['name'] != 'EgoVehicle':
                        continue

                    frame_annotations = set()    

                    for attr in obj['attributes']['attribute']:
                        if 'GPSData' in attr:
                            continue

                        if attr['name'] in labels:
                            if attr['value'] in labels[attr['name']]:
                                frame_annotations.add(labels_mapping[attr['name']])

                    if len(scene_frames) == 0:
                        scene_frames.append(file)
                        annotations = deepcopy(frame_annotations)
                    elif frame_annotations == annotations:
                        scene_frames.append(file)
                    else:
                        if len(annotations) > 0:
                            path = os.path.join(output_directory + '/Scenes', '{0:06d}'.format(scene_counter))
                            os.mkdir(path)
                            for i, frame in enumerate(scene_frames):
                                shutil.copy(file[:-3] + 'JPG', output_directory + '/Scenes/{0:06d}/'.format(scene_counter) + 'img_{0:05d}.jpg'.format(i+1))
                            with open(output_directory + '/annotations.txt', 'a') as f:
                                ann = [str(s) for s in annotations]
                                ann.sort()
                                ann_string = " ".join(ann)
                                print(output_directory + '/Scenes/{0:06d}'.format(scene_counter) + ' ' + str(len(scene_frames)) + ' ' + ann_string, file=f)

                            scene_counter += 1
                        scene_frames = []
                        annotations = set()
                        scene_frames.append(file)
                        annotations = deepcopy(frame_annotations)

                    continue

                for obj in doc['object']:
                    if obj['name'] != 'EgoVehicle':
                        continue

                    frame_annotations = set()    

                    for attr in obj['attributes']['attribute']:
                        if 'GPSData' in attr:
                            continue

                        if attr['name'] in labels:
                            if attr['value'] in labels[attr['name']]:
                                frame_annotations.add(labels_mapping[attr['name']])

                    if len(scene_frames) == 0:
                        scene_frames.append(file)
                        annotations = deepcopy(frame_annotations)
                    elif frame_annotations == annotations:
                        scene_frames.append(file)
                    else:
                        if len(annotations) > 0:
                            path = os.path.join(output_directory + '/Scenes', '{0:06d}'.format(scene_counter))
                            os.mkdir(path)
                            for i, frame in enumerate(scene_frames):
                                shutil.copy(file[:-3] + 'JPG', output_directory + '/Scenes/{0:06d}/'.format(scene_counter) + 'img_{0:05d}.jpg'.format(i+1))
                            with open(output_directory + '/annotations.txt', 'a') as f:
                                ann = [str(s) for s in annotations]
                                ann.sort()
                                ann_string = " ".join(ann)
                                print(output_directory + '/Scenes/{0:06d}'.format(scene_counter) + ' ' + str(len(scene_frames)) + ' ' + ann_string, file=f)

                            scene_counter += 1
                        scene_frames = []
                        annotations = set()
                        scene_frames.append(file)
                        annotations = deepcopy(frame_annotations)

    print('Bad Videos:', bad_videos)     
