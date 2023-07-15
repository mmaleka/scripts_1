import os
import shutil
import random


class Dog:
    def __init__(self, parent_folder="link to stuff"):
        print(f"Source folder for the project: {parent_folder}")
        self.train_path = os.path.join(parent_folder, "train")
        self.test_path = os.path.join(parent_folder, "test")
        self.source_folder = os.path.join(parent_folder, "digits")


    def create_test_train_folder(self):
        print(f"Creating train folder: {self.train_path}")

        # checking if the directory demo_folder 
        # exist or not.
        if not os.path.exists(self.train_path):
            
            # if the demo_folder directory is not present 
            # then create it.
            os.makedirs(self.train_path)


        print(f"Creating train folder: {self.test_path}")

        # checking if the directory demo_folder 
        # exist or not.
        if not os.path.exists(self.test_path):
            
            # if the demo_folder directory is not present 
            # then create it.
            os.makedirs(self.test_path)

        return 1
    
    def copy_files(self):
        random.seed(42)

        for label in os.listdir(self.source_folder):
            images_list = os.listdir(os.path.join(self.source_folder, label))
            random.shuffle(images_list)
            train_list = images_list[ : int(len(images_list) * .80)]
            test_list = images_list[int(len(images_list) * .80) : ]
            print(f"Label {label} - total train {len(train_list)}, total test {len(test_list)}, Total {len(images_list)}")
            for image in train_list:
                if image.endswith(".jpg"):
                    src_path = os.path.join(self.source_folder, label, image)
                    dst_path = os.path.join(self.train_path, label, image)

                    if not os.path.exists(os.path.join(self.train_path, label)):
            
                        # if the demo_folder directory is not present 
                        # then create it.
                        os.makedirs(os.path.join(self.train_path, label))

                        # Copy the files to the new folder
                        shutil.copy(src_path, dst_path)
                    else:
                        shutil.copy(src_path, dst_path)


            for image in test_list:
                if image.endswith(".jpg"):
                    src_path = os.path.join(self.source_folder, label, image)
                    dst_path = os.path.join(self.test_path, label, image)

                    if not os.path.exists(os.path.join(self.test_path, label)):
            
                        # if the demo_folder directory is not present 
                        # then create it.
                        os.makedirs(os.path.join(self.test_path, label))

                        # Copy the files to the new folder
                        shutil.copy(src_path, dst_path)
                    else:
                        shutil.copy(src_path, dst_path)
        

        return 1

    
    

d = Dog(parent_folder=r"C:\Users\mphom\OneDrive\Documents\Scanning Device\Scripts")
d.create_test_train_folder()
d.copy_files()