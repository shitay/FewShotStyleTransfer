[![License CC BY-NC-SA 4.0](https://img.shields.io/badge/license-CC4.0-blue.svg)](LICENSE.md)
![Python 3.7](https://img.shields.io/badge/python-3.7-green.svg)


## Training

Once the animal face dataset is prepared, you can train an animal face translation model by running.

```bash
python train.py --config configs/funit_animals.yaml --multigpus
```

The training results including the checkpoints and intermediate results will be stored in `outputs/funit_animals`.

For custom dataset, you would need to write an new configuration file. Please create one based on the [example config file](configs/painter_by_numbers.yaml).

## Testing pretrained model

To test the pretrained model, please first create a folder `pretrained` under the root folder. Then, we need to downlowad the pretrained models via the [link](https://drive.google.com/open?id=1CsmSSWyMngtOLUL5lI-sEHVWc2gdJpF9) and save it in `pretrained`. Untar the file `tar xvf pretrained.tar.gz`.

Now, we can test the translation
```bash
python test_k_shot.py --config configs/funit_animals.yaml --ckpt pretrained/animal149_gen.pt --input images/input_content.jpg --class_image_folder images/n02138411 --output images/output.jpg
```
