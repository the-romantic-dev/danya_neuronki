from config import filename
from data.class_random_shapes_generator import RandomShapeGenerator

if __name__ == '__main__':
    generator = RandomShapeGenerator(num_shapes=2, image_width=100, image_height=100,
                                     min_shape_size=20,
                                     max_shape_size=50)
    print(generator.generate_shapes())
    generator.save_image(f'{filename(0)}')