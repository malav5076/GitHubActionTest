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
filename = 'data.yaml'

# Data to write to YAML
data = {
    'name': 'John Doe',
    'age': 30,
    'occupation': 'Software Engineer',
    'languages': ['Python', 'Java', 'JavaScript'],
    'contact': {
        'email': 'john.doe@example.com',
        'phone': '123-456-7890'
    }
}

# Write data to YAML file
write_yaml(filename, data)
data2 = read_yaml(filename)
print(data2['contact'])
print(f'Wrote initial data to {filename}')


