# # pubsub.py
# from google.cloud import pubsub_v1
# import os

# # Configure Pub/Sub Client (uses default credentials)
# def publish_message(topic_name, message):
#     project_id = 'dotted-marking-444412-s5'  # Replace with your Google Cloud project ID
#     topic_path = f"projects/{dotted-marking-444412-s5}/topics/{topic_name}"
    
#     publisher = pubsub_v1.PublisherClient()
#     future = publisher.publish(topic_path, message.encode('utf-8'))
    
#     print(f"Message published: {future.result()}")
