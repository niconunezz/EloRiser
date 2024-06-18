from generate_data import *
import argparse

def main():
    parser = argparse.ArgumentParser(description='EloRiser')
    parser.add_argument('--new_data',action="store_true",
                            help='create new data')
    parser.add_argument('--training', action="store_true",
                            help='use training data')
    data = os.listdir("data/dataset")
    args = parser.parse_args()
    if not args.new_data:
        if args.training:
            data = np.load("data/dataset/train/datos.npz")
        else:
            data = np.load("data/dataset/test/datos.npz")
        x = data['x']
        y = data['y']
        print(x.shape)
        print(y.shape)
    if args.new_data:
        if args.training:
            iterations = len(os.listdir('data/train_data'))
            get_all_files(iterations)
        else:
            x,y = generate(args.training)
            save_test_data(x,y)
        
    print(f"x shape is {x.shape}")
    print(f"y shape is {y.shape}")


    
if __name__ == "__main__":
    main()