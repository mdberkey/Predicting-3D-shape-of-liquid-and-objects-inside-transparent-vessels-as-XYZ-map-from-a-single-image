"""
A template for creating a DLHub-compatible description of a model.

The places where you need to fill in information are marked with "TODO" comments
"""

# TODO: Import a metadata template appropriate for your type of model
#  See:
from dlhub_sdk.models.servables.python import PythonStaticMethodModel
from dlhub_sdk.utils.schemas import validate_against_dlhub_schema
import json

# Read in model from disk
# TODO: Fill in options specific to this type of model
model_info = PythonStaticMethodModel.create_model('module', 'function')

# Define the name and title for the model
model_info.set_title("A short title for the servable")
model_info.set_name("mberkey")

# TODO: Verify authors and affiliations
model_info.set_authors(["Berkey, Michael"], [["UW-Madison"]])

# TODO: Describe the scientific purpose of the model
model_info.set_domains(["some", "pertinent", "fields"])
model_info.set_abstract("A longer description of the model")

# TODO: Add references for the model
# model_info.add_related_identifier("DOI", "10.", "IsDescribedBy")  # Example: Paper describing the model

# TODO: Describe the computational environment
# Basic route: Add a specific Python requirement
# model.add_requirement('numpy', 'detect')
# Advanced: Include repo2docker config files in submission
# model.parse_repo2docker_configuration()  # You can specify a different path for config files

# TODO: Describe the inputs and outputs of the model
#  This is not required for some model types (e.g., TensorFlow), delete if needed
model_info.set_inputs('string', 'Your name')
model_info.set_outputs('string', 'A greeting: "Hello <your name>!"')

# Check the schema against a DLHub Schema
validate_against_dlhub_schema(model_info.to_dict(), 'servable')

# Save the metadata
with open('dlhub.json', 'w') as fp:
    json.dump(model_info.to_dict(save_class_data=True), fp, indent=2)
