ROS code to brake the vehicle in case of network loss.

The code topic_activity_pub.py publishes on the topic /signal (this would be replaced by the actual heartbeat signal).
The subscriber in topic_activity_sub_better.py subscribed to this /signal topic.Once the publisher is shutdown or basically not publishing 
any message on /signal topic,the subscriber detects by using a timeout of 0.2 seconds,and publishes a brake=1 command indicating a stop in the vehicle.

