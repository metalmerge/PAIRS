import roboflow

rf = roboflow.Roboflow(api_key=YOUR_API_KEY_HERE)

project = rf.workspace().project("PROJECT_ID")
model = project.version("1").model

# optionally, change the confidence and overlap thresholds
# values are percentages
model.confidence = 50
model.overlap = 25

# predict on a local image
prediction = model.predict("YOUR_IMAGE.jpg")

# Predict on a hosted image via file name
# prediction = model.predict("YOUR_IMAGE.jpg", hosted=True)

# Predict on a hosted image via URL
# prediction = model.predict("https://...", hosted=True)

# Plot the prediction in an interactive environment
prediction.plot()

# Convert predictions to JSON
prediction.json()
