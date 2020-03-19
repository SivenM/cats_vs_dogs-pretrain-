import os, shutil

# Пути к каталогу с распаковынными исходными наборами данных
original_dataset_dir = 'kaggle_original data'


# Каталог для сохранения выделенного небольшого набора
base_dir = 'cats_dogs_small'
os.mkdir(base_dir)

# Каталоги дляобучающего, проверочного и контрольго поднаборов
train_dir = os.path.join(base_dir, 'train')
os.mkdir(train_dir)
validation_dir = os.path.join(base_dir, 'validation')
os.mkdir(validation_dir)
test_dir = os.path.join(base_dir, 'test')
os.mkdir(test_dir)

# Каталог для обучяющих изображений с кругами
train_cats_dir = os.path.join(train_dir, 'cats')
os.mkdir(train_cats_dir)

# Каталог для обучающих изображений с квадратами
train_dogs_dir = os.path.join(train_dir, 'dogs')
os.mkdir(train_dogs_dir)

# Каталог для проверочных изображений с кругами
validation_cats_dir = os.path.join(validation_dir, 'cats')
os.mkdir(validation_cats_dir)

# Каталог для проверочных изображений с квадратами
validation_dogs_dir = os.path.join(validation_dir, 'dogs')
os.mkdir(validation_dogs_dir)

# Каталог для тестовых изображений с кругами
test_cats_dir = os.path.join(test_dir, 'cats')
os.mkdir(test_cats_dir)

# Каталог для тестовых изображений с квадратами
test_dogs_dir = os.path.join(test_dir, 'dogs')
os.mkdir(test_dogs_dir)

# Копирование первых 1000 изображений с кругами в каталог train_cats_dir
fnames = ['cat.{}.jpg'.format(i) for i in range(1000)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, fname)
    dst = os.path.join(train_cats_dir, fname)
    shutil.copyfile(src, dst)

# Копирование следующих 500 изображений с кругами в каталог validation_cats_dir
fnames = ['cat.{}.jpg'.format(i) for i in range(1000, 1500)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, fname)
    dst = os.path.join(validation_cats_dir, fname)
    shutil.copyfile(src, dst)

# Копирование следующих 500 изображений с кругами в каталог test_cats_dir
fnames = ['cat.{}.jpg'.format(i) for i in range(1500, 2000)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, fname)
    dst = os.path.join(test_cats_dir, fname)
    shutil.copyfile(src, dst)

# Копирование первых 1000 изображений с квадратами в каталог train_dogs_dir
fnames = ['dog.{}.jpg'.format(i) for i in range(1000)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, fname)
    dst = os.path.join(train_dogs_dir, fname)
    shutil.copyfile(src, dst)

# Копирование следующих 500 изображений с кругами в каталог validation_dogs_dir
fnames = ['dog.{}.jpg'.format(i) for i in range(1000, 1500)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, fname)
    dst = os.path.join(validation_dogs_dir, fname)
    shutil.copyfile(src, dst)

# Копирование следующих 500 изображений с кругами в каталог test_dogs_dir
fnames = ['dog.{}.jpg'.format(i) for i in range(1500, 2000)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, fname)
    dst = os.path.join(test_dogs_dir, fname)
    shutil.copyfile(src, dst)