import yaml

# Function to write data to YAML file
def write_yaml(filename, data):
    with open(filename, 'w') as file:
        yaml.dump(data, file)

# Function to read data from YAML file
def read_yaml(filename):
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)
    return data

# Filename
filename = ""


# Write data to YAML file
data2 = read_yaml(filename)
print(data2['name'])
print(f'Wrote initial data to {filename}')


