import os
import random
import shutil

def create_sampled_dataset(source_dir="/kaggle/input/fashion-anchor-cloth-pairs/", target_dir="/kaggle/working/sampled_fashion_dataset", samples_per_category=100):
    """
    Create a smaller dataset by sampling 100 images from each category
    """
    
    # Create target directory
    os.makedirs(target_dir, exist_ok=True)
    
    # Categories and their paths
    categories = {
        'bags': ['bags_dataset/bags_dataset/men_bags/cloths', 
                'bags_dataset/bags_dataset/women_bags/cloths'],
        'dress': ['dress_dataset/dress_dataset/cloths'],
        'pants': ['pants_dataset/pants_dataset/men_pants/cloths',
                 'pants_dataset/pants_dataset/women_pants/cloths'],
        'shorts': ['shorts_dataset/shorts_dataset/men_shorts/cloths',
                  'shorts_dataset/shorts_dataset/women_shorts/cloths'],
        'upperwear': ['upperwear_dataset/upperwear_dataset/men_top/cloths',
                     'upperwear_dataset/upperwear_dataset/women_top/cloths']
    }
    
    for category, paths in categories.items():
        print(f"\nProcessing {category}...")
        
        # Create category directory in target
        category_dir = os.path.join(target_dir, category)
        os.makedirs(category_dir, exist_ok=True)
        
        # Collect all images from all subcategories
        all_images = []
        for path in paths:
            full_path = os.path.join(source_dir, path)
            if os.path.exists(full_path):
                images = [f for f in os.listdir(full_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
                all_images.extend([(os.path.join(full_path, img), img) for img in images])
        
        # Sample images
        if len(all_images) > samples_per_category:
            sampled_images = random.sample(all_images, samples_per_category)
        else:
            sampled_images = all_images
            print(f"Warning: Only {len(all_images)} images available for {category}")
        
        # Copy sampled images
        for src_path, img_name in sampled_images:
            dst_path = os.path.join(category_dir, img_name)
            shutil.copy2(src_path, dst_path)
            
        print(f"Copied {len(sampled_images)} images for {category}")

    print("\nDataset sampling completed!")

# Run the function
if __name__ == "__main__":
    create_sampled_dataset()