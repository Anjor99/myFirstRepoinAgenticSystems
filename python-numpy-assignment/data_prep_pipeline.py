import numpy as np

# 1. Set Random seed for reproducibility
np.random.seed(42)

# 2. Generate a 2D dataset
num_samples=100
num_features=3

data = np.random.randn(num_samples,num_features)

# 3. Compute the mean and standard deviation per feature
mean = np.mean(data, axis=0)
std = np.std(data,axis=0)

# 4. Normalize the dataset using broadcasting
normalized = (data - mean) / std

# 5. Split training and testing data
train_size = int(0.8 * num_samples)

train_data = normalized[:train_size]
test_data = normalized[train_size:]

# 6. Modify sliced value to demonstrate view behaviour
original_value = normalized[0,0]

train_data[0,0] = 999 # modifying slice

# 7. Print required data
print(f"Original data shape : {data.shape}")
print(f"Mean shape : {mean.shape}")
print(f"Standard deviation shape : {std.shape}")
print(f"Training data shape : {train_data.shape}")
print(f"Test data shape : {test_data.shape}")
print(f"Original value : {original_value}")
print(f"Value after modification : {normalized[0,0]}")
print("Note: Modifying the slice affected the original array")