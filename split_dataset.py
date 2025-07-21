import os
import shutil
import random

# Set paths
original_dataset_dir = "PlantVillage"  # Your original dataset folder
base_dir = "dataset"  # Where train/val folders will go

train_ratio = 0.8  # 80% for training

# Make train/val directories
train_dir = os.path.join(base_dir, "train")
val_dir = os.path.join(base_dir, "val")

# Create directories if not exist
for folder in [train_dir, val_dir]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Get all class names (i.e., folder names)
classes = os.listdir(original_dataset_dir)

for class_name in classes:
    class_dir = os.path.join(original_dataset_dir, class_name)
    if not os.path.isdir(class_dir):
        continue

    images = os.listdir(class_dir)
    random.shuffle(images)

    train_count = int(len(images) * train_ratio)
    train_images = images[:train_count]
    val_images = images[train_count:]

    # Make class subfolders
    os.makedirs(os.path.join(train_dir, class_name), exist_ok=True)
    os.makedirs(os.path.join(val_dir, class_name), exist_ok=True)

    # Copy images
    for img in train_images:
        src = os.path.join(class_dir, img)
        dst = os.path.join(train_dir, class_name, img)
        shutil.copyfile(src, dst)

    for img in val_images:
        src = os.path.join(class_dir, img)
        dst = os.path.join(val_dir, class_name, img)
        shutil.copyfile(src, dst)

print("✅ Dataset split complete.")
