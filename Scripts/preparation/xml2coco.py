import argparse
from glob import glob
import xmltodict
import json
import os
from tqdm import tqdm

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert the annotations to the COCO format')
    parser.add_argument('--dataset_directory', type=str)
    parser.add_argument('--output_directory', type=str)
    config = parser.parse_args()

    bad_videos = []
    category_counter = 1
    image_counter = 1
    annotation_counter = 1

    images = []
    annotations = []
    categories = []

    categories_dict = {}

    dataset_directory = config.dataset_directory

    bad_vid = False

    for directory in tqdm(glob(dataset_directory + '/*/')):
        if bad_vid:
            bad_vid = False
            bad_videos.append(directory)
            continue

        for file in glob(directory + 'Annotations/*.xml'):
            if os.stat(file).st_size == 0:
                bad_vid = True
                break

            with open(file) as fd:
                doc = xmltodict.parse(fd.read())['annotation']

                if 'object' not in doc:
                    bad_vid = True
                    break

                image = {'id': image_counter, 'width': int(doc['size']['width']), 'height': int(doc['size']['height']), 'file_name': file[:-3] + 'JPG'}
                images.append(image)

                if not isinstance(doc['object'], list):
                    obj = doc['object']

                    if obj['name'] == 'Pedestrain':
                        obj['name'] = 'Pedestrian'

                    if obj['name'] == 'EgoVehicle':
                        continue

                    x = int(float(obj['bndbox']['xmin']))
                    y = int(float(obj['bndbox']['ymin']))
                    width = int(float(obj['bndbox']['xmax'])) - x
                    height = int(float(obj['bndbox']['ymax'])) - y

                    if obj['name'] not in categories_dict:
                        categories_dict[obj['name']] = category_counter
                        categories.append({'id': category_counter, 'name': obj['name']})
                        category_counter += 1

                    annotations.append({'id': annotation_counter, 'image_id': image_counter, 'category_id': categories_dict[obj['name']], 'area': width * height, 'bbox': [x, y, width, height], "iscrowd": 0})
                    annotation_counter += 1

                    continue

                for obj in doc['object']:
                    if obj['name'] == 'EgoVehicle':
                        continue

                    if obj['name'] == 'Pedestrain':
                        obj['name'] = 'Pedestrian'    

                    x = int(float(obj['bndbox']['xmin']))
                    y = int(float(obj['bndbox']['ymin']))
                    width = int(float(obj['bndbox']['xmax'])) - x
                    height = int(float(obj['bndbox']['ymax'])) - y

                    if obj['name'] not in categories_dict:
                        categories_dict[obj['name']] = category_counter
                        categories.append({'id': category_counter, 'name': obj['name']})
                        category_counter += 1

                    annotations.append({'id': annotation_counter, 'image_id': image_counter, 'category_id': categories_dict[obj['name']], 'area': width * height, 'bbox': [x, y, width, height], "iscrowd": 0})
                    annotation_counter += 1

                image_counter += 1

    with open(config.output_directory + '/annotations.json', 'w') as fd:
        json.dump({'images': images, 'annotations': annotations, 'categories': categories}, fd, indent = 1)  

    print('Bad Videos:', bad_videos)         



