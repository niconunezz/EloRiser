# EloRiser
![Chess AI](C:\Users\nicod\OneDrive\Escritorio\Coding\EloRiser\assets\training_loss.PNG)

# Chess AI with Convolutional Neural Networks

This project implements a neural network model to learn and play chess using PyTorch. The model takes a 14x8x8 board representation as input and predicts the next move.

## Model Architecture

The neural network consists of:
- Convolutional layers to process the board state
- Fully connected layers for move prediction
- Output layer with around 1840 units representing possible moves

## Data Representation

- Input: 14x8x8 tensor
   - First 12 planes: Piece positions (both colors)
   - 13th plane: Legal move destinations
   - 14th plane: Legal move origins
- Output: One-hot encoded vector of 1840 possible moves

## Key Files

- `train.py`: Main training script
- `model.py`: Neural network architecture definition
- `data.py`: Functions for data loading and preprocessing
- `agent.py`: Script to see the model plays vs itself

## Usage

1. Install requirements:
    ```
    pip install -r requirements.txt
    ```

2. Train the model:
    ```
    python train.py
    ```

3. See the model play:
    ```
      agent.ipynb
    ```

## Future Improvements

- Upload the model in a way that people can play against it
- Fine-tune for better decision making at the final rounds of the game

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
# Chess AI with Convolutional Neural Networks

This project implements a neural network model to learn and play chess using PyTorch. The model takes a 14x8x8 board representation as input and predicts the next move.

## Model Architecture

The neural network consists of:
- Convolutional layers to process the board state
- Fully connected layers for move prediction
- Output layer with around 1840 units representing possible moves

## Data Representation

- Input: 14x8x8 tensor
  - First 12 planes: Piece positions (both colors)
  - 13th plane: Legal move destinations
  - 14th plane: Legal move origins
- Output: One-hot encoded vector of 1840 possible moves

## Key Files

- `train.py`: Main training script
- `model.py`: Neural network architecture definition
- `data.py`: Functions for data loading and preprocessing
- `agent.py`: Script to see the model plays vs itself

## Usage

1. Install requirements:
   ```
   pip install -r requirements.txt
   ```

2. Train the model:
   ```
   python train.py
   ```

3. See the model play:
   ```
    agent.ipynb
   ```

## Future Improvements

- Upload the model in a way that people can play against it
- Fine-tune for better decision making at the final rounds of the game

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).