import kagglehub

# Download latest version
path = kagglehub.dataset_download("prasad22/global-economy-indicators")

print("Path to dataset files:", path)