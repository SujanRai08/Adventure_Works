import logging

# Configure logging
logging.basicConfig(
    filename='pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def pipeline_step(step_name):
    try:
        logging.info(f"Starting {step_name}")
        # Simulate step
        logging.info(f"Completed {step_name}")
    except Exception as e:
        logging.error(f"Error in {step_name}: {str(e)}")

pipeline_step("Extract")
pipeline_step("Transform")
pipeline_step("Load")
