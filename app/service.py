import time
import random


def feed_service():
    """
    Simulates LinkedIn feed loading service
    """
    time.sleep(random.uniform(0.1, 0.3))
    return "Feed loaded successfully"


def profile_service():
    """
    Simulates profile data fetch service
    """
    time.sleep(random.uniform(0.1, 0.2))
    return "Profile data fetched"


def recommendation_service():
    """
    Simulates recommendation engine
    Intentional bottleneck: slower response time
    """
    time.sleep(random.uniform(0.8, 1.5))
    return "Recommendations generated"